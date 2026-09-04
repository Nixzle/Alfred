import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('alfred', Path(__file__).resolve().parents[1] / 'scripts/alfred.py')
alfred = importlib.util.module_from_spec(spec)
spec.loader.exec_module(alfred)


class LauncherTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve()
        self.user = self.base / 'user'
        self.root = self.base / 'package'
        self.profile = self.user / 'alfred'

    def test_personal_home_is_refused_including_ancestors(self):
        for path in (self.user / '.codex', self.user, self.user / '.codex/child'):
            with self.assertRaises(ValueError):
                alfred.profile_path({'ALFRED_HOME': str(path)}, self.user, root=self.root)

    def test_active_profile_workspace_and_package_refused(self):
        for path in (self.base / 'active', self.root, self.base / 'project'):
            with self.assertRaises(ValueError):
                alfred.profile_path({'ALFRED_HOME': str(path), 'CODEX_HOME': str(self.base / 'active')},
                                    self.user, self.base / 'project', self.root)

    def test_nonempty_unmarked_profile_is_not_overwritten(self):
        self.profile.mkdir(parents=True)
        file = self.profile / 'AGENTS.md'
        file.write_text('Existing identity')
        with self.assertRaises(ValueError):
            alfred.prepare_profile(self.profile, self.root)
        self.assertEqual(file.read_text(), 'Existing identity')

    def test_init_is_idempotent_and_config_is_preserved(self):
        alfred.prepare_profile(self.profile, self.root)
        config = self.profile / 'config.toml'
        config.write_text('model = "user-choice"\n')
        alfred.prepare_profile(self.profile, self.root)
        self.assertEqual(config.read_text(), 'model = "user-choice"\n')
        self.assertIn('You are Alfred', (self.profile / 'AGENTS.md').read_text())

    def test_modified_instructions_are_not_overwritten(self):
        alfred.prepare_profile(self.profile, self.root)
        file = self.profile / 'AGENTS.md'
        file.write_text('User changes')
        with self.assertRaises(ValueError):
            alfred.prepare_profile(self.profile, self.root)
        self.assertEqual(file.read_text(), 'User changes')

    def test_different_checkout_is_rejected(self):
        alfred.prepare_profile(self.profile, self.root)
        with self.assertRaises(ValueError):
            alfred.prepare_profile(self.profile, self.base / 'other')

    def test_environment_does_not_borrow_account_overrides(self):
        original = {'CODEX_HOME': '/personal', 'OPENAI_API_KEY': 'dummy', 'PATH': '/bin'}
        child = alfred.child_environment(original, self.profile)
        self.assertEqual(original['CODEX_HOME'], '/personal')
        self.assertNotIn('OPENAI_API_KEY', child)
        self.assertEqual(child['CODEX_HOME'], str(self.profile))
        self.assertEqual(child['PATH'], '/bin')

    def test_launch_uses_workspace_without_shell_and_preserves_exit_code(self):
        project = self.base / 'project with spaces'
        project.mkdir()
        with patch.dict(os.environ, {'ALFRED_HOME': str(self.profile)}, clear=True), \
             patch.object(alfred.Path, 'home', return_value=self.user), \
             patch.object(alfred.shutil, 'which', return_value='/bin/codex'), \
             patch.object(alfred.subprocess, 'call', return_value=7) as call:
            result = alfred.main(['run', '--workspace', str(project), '--', '--no-alt-screen'])
        self.assertEqual(result, 7)
        args, kwargs = call.call_args
        self.assertEqual(args[0][-3:], ['--cd', str(project), '--no-alt-screen'])
        self.assertNotIn('shell', kwargs)
        self.assertEqual(kwargs['env']['CODEX_HOME'], str(self.profile))

    def test_doctor_does_not_initialize_profile(self):
        with patch.dict(os.environ, {'ALFRED_HOME': str(self.profile)}, clear=True), \
             patch.object(alfred.Path, 'home', return_value=self.user), \
             patch.object(alfred.shutil, 'which', return_value='/bin/codex'):
            self.assertEqual(alfred.main(['doctor']), 0)
        self.assertFalse(self.profile.exists())


if __name__ == '__main__':
    unittest.main()
