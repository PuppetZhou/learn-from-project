#!/usr/bin/env python3
"""Local source-linked installation. Standard library only; never downloads code."""
import argparse
import os
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def discover(root=ROOT):
    found = {}
    for entry in sorted((root / 'skills').iterdir()):
        if entry.is_dir() and (entry / 'SKILL.md').is_file():
            if entry.is_symlink() or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', entry.name):
                raise ValueError(f'Invalid source directory: {entry}')
            found[entry.name] = entry.resolve()
    if not found:
        raise ValueError('No skills found')
    return found


def state(source, target):
    if target.is_symlink() and target.resolve() == source.resolve():
        return 'linked'
    if os.path.lexists(target):
        return 'conflict'
    return 'not installed'


def install(skills, dest, replace=False):
    dest = Path(dest).expanduser().resolve()
    # Preflight the entire selection so a known conflict cannot cause partial installation.
    for name, source in skills.items():
        target = dest / name
        if target == source or source in target.parents or target in source.parents:
            raise ValueError('Installation destination overlaps the source')
        if state(source, target) == 'conflict' and not replace:
            raise ValueError(f'Existing installation: {target}; use --replace to back it up')
    dest.mkdir(parents=True, exist_ok=True)
    backup_dir = None
    for name, source in skills.items():
        target = dest / name
        if state(source, target) == 'linked':
            print(f'Already linked: {name}')
            continue
        backup = None
        if os.path.lexists(target):
            if not replace:  # Also detect a target created since preflight.
                raise ValueError(f'Destination appeared during installation: {target}')
            if backup_dir is None:
                from datetime import datetime
                base = dest.parent / 'skill-kit-backups'
                base.mkdir(mode=0o700, exist_ok=True)
                backup_dir = Path(tempfile.mkdtemp(prefix=datetime.now().strftime('%Y%m%d-%H%M%S-'), dir=base))
            backup = backup_dir / name
            target.rename(backup)
            print(f'Backup: {backup}')
        try:
            target.symlink_to(source, target_is_directory=True)
        except OSError:
            if backup is not None and not os.path.lexists(target):
                backup.rename(target)
            raise
        print(f'Linked: {target} -> {source}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['list', 'install', 'status'])
    parser.add_argument('names', nargs='*', help='Default: all skills')
    parser.add_argument('--dest', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills')
    parser.add_argument('--replace', action='store_true', help='Back up conflicting installations before linking')
    args = parser.parse_args()
    try:
        skills = discover()
        unknown = set(args.names) - skills.keys()
        if unknown:
            raise ValueError(f'Unknown skills: {", ".join(sorted(unknown))}')
        selected = {name: source for name, source in skills.items() if not args.names or name in args.names}
        if args.command == 'install':
            install(selected, args.dest, args.replace)
        else:
            for name, source in selected.items():
                print(f'{name}: {source}' if args.command == 'list' else f'{name}: {state(source, args.dest.expanduser() / name)}')
    except (OSError, ValueError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
