import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from manage import install, state


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / 'repo/skills/example'
        self.source.mkdir(parents=True)
        (self.source / 'SKILL.md').write_text('source')
        self.dest = self.root / 'codex/skills'
        self.target = self.dest / 'example'
        self.skills = {'example': self.source}
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(self.output.__exit__, None, None, None)

    def test_install_is_idempotent_and_source_changes_are_visible(self):
        install(self.skills, self.dest)
        install(self.skills, self.dest)
        self.assertEqual(state(self.source, self.target), 'linked')
        (self.source / 'SKILL.md').write_text('new content')
        self.assertEqual((self.target / 'SKILL.md').read_text(), 'new content')
        self.assertFalse((self.dest.parent / 'skill-kit-backups').exists())

    def test_conflict_preflight_leaves_other_targets_untouched(self):
        self.target.mkdir(parents=True)
        marker = self.target / 'local.md'
        marker.write_text('local edits')
        with self.assertRaises(ValueError):
            install({'new-skill': self.source, **self.skills}, self.dest)
        self.assertFalse((self.dest / 'new-skill').exists())
        self.assertEqual(marker.read_text(), 'local edits')

    def test_replace_preserves_original_directory(self):
        self.target.mkdir(parents=True)
        (self.target / 'local.md').write_text('local edits')
        install(self.skills, self.dest, replace=True)
        copies = list((self.dest.parent / 'skill-kit-backups').glob('*/example/local.md'))
        self.assertEqual(len(copies), 1)
        self.assertEqual(copies[0].read_text(), 'local edits')
        self.assertEqual(state(self.source, self.target), 'linked')

    def test_broken_link_is_a_conflict_and_is_backed_up(self):
        self.dest.mkdir(parents=True)
        self.target.symlink_to(self.root / 'missing')
        with self.assertRaises(ValueError):
            install(self.skills, self.dest)
        install(self.skills, self.dest, replace=True)
        old = list((self.dest.parent / 'skill-kit-backups').glob('*/example'))
        self.assertEqual(len(old), 1)
        self.assertTrue(old[0].is_symlink())

    def test_link_failure_restores_old_installation(self):
        self.target.mkdir(parents=True)
        (self.target / 'local.md').write_text('keep me')
        with patch.object(Path, 'symlink_to', side_effect=OSError('test failure')):
            with self.assertRaises(OSError):
                install(self.skills, self.dest, replace=True)
        self.assertEqual((self.target / 'local.md').read_text(), 'keep me')

    def test_source_cannot_be_replaced(self):
        with self.assertRaises(ValueError):
            install(self.skills, self.source.parent, replace=True)
        self.assertEqual((self.source / 'SKILL.md').read_text(), 'source')


if __name__ == '__main__':
    unittest.main()
