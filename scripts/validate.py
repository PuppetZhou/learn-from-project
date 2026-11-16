#!/usr/bin/env python3
"""Check kit structure and local Markdown file links; not a semantic evaluation."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    sys.exit('PyYAML required: python -m pip install -r requirements-dev.txt')

from manage import ROOT, discover


def check(root=ROOT):
    errors = []
    skills = discover(root)
    for name, folder in skills.items():
        text = (folder / 'SKILL.md').read_text(encoding='utf-8')
        match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
        if not match:
            errors.append(f'{name}: missing YAML frontmatter')
            continue
        try:
            meta = yaml.safe_load(match[1])
            if not isinstance(meta, dict) or meta.get('name') != name:
                errors.append(f'{name}: name must match directory')
            description = meta.get('description') if isinstance(meta, dict) else None
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                errors.append(f'{name}: description must contain 1–1024 characters')
            if len(name) > 64:
                errors.append(f'{name}: name exceeds 64 characters')
            ui = yaml.safe_load((folder / 'agents/openai.yaml').read_text(encoding='utf-8'))
            interface = ui.get('interface', {}) if isinstance(ui, dict) else {}
            for field in ('display_name', 'short_description'):
                if not isinstance(interface.get(field), str) or not interface[field].strip():
                    errors.append(f'{name}: missing interface.{field}')
            if isinstance(interface.get('short_description'), str) and not 25 <= len(interface['short_description']) <= 64:
                errors.append(f'{name}: short_description must contain 25–64 characters')
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f'{name}: {exc}')
        for item in folder.rglob('*'):
            if item.is_symlink():
                errors.append(f'{item.relative_to(root)}: source package must contain real files')
    docs = [root / 'README.md', root / 'AGENTS.md', *sorted((root / 'docs').glob('*.md'))]
    docs += [p for folder in skills.values() for p in folder.rglob('*.md')]
    for doc in docs:
        if not doc.is_file():
            errors.append(f'Missing: {doc}')
            continue
        text = doc.read_text(encoding='utf-8')
        # Fenced/inline examples are not live Markdown links. Anchors and web URLs are not checked.
        text = re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text, flags=re.M | re.S)
        text = re.sub(r'`[^`\n]+`', '', text)
        for raw in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
            target = raw[1:raw.index('>')] if raw.startswith('<') and '>' in raw else raw.split()[0]
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (doc.parent / unquote(url.path)).resolve()
            scope = next((s for s in skills.values() if doc.is_relative_to(s)), root)
            if not path.is_relative_to(scope):
                errors.append(f'{doc.relative_to(root)}: local link escapes package: {target}')
            elif not path.exists():
                errors.append(f'{doc.relative_to(root)}: missing local link: {target}')
        if re.search(r'/Users/[^/\s]+/', text):
            errors.append(f'{doc.relative_to(root)}: personal absolute path in distributable documentation')
    return errors


if __name__ == '__main__':
    try:
        errors = check()
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        sys.exit(1)
    print('Validated skills, UI metadata, package boundaries and local Markdown file links.')
