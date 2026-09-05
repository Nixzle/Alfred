import tempfile
from pathlib import Path
import tarfile
import unittest

from runtime.recovery_bundle import build_bundle, verify_bundle, restore_bundle


class RecoveryBundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'source'
        self.root.mkdir()
        (self.root / 'README.md').write_text('sanctum', encoding='utf-8')
        (self.root / 'runtime').mkdir()
        (self.root / 'runtime' / 'module.py').write_text('VALUE = 1\n', encoding='utf-8')
        (self.root / '.git').mkdir()
        (self.root / '.git' / 'secret').write_text('ignore', encoding='utf-8')
        (self.root / 'private.sqlite').write_text('ignore', encoding='utf-8')
        self.bundle = Path(self.temp.name) / 'bundle.tar.gz'

    def tearDown(self):
        self.temp.cleanup()

    def test_build_verify_restore(self):
        manifest = build_bundle(self.root, self.bundle, 'abc123')
        self.assertEqual(set(manifest['files']), {'README.md', 'runtime/module.py'})
        verdict = verify_bundle(self.bundle)
        self.assertEqual(verdict['status'], 'PASS')
        self.assertEqual(verdict['revision'], 'abc123')
        destination = Path(self.temp.name) / 'restore'
        restore_bundle(self.bundle, destination)
        self.assertEqual((destination / 'README.md').read_text(), 'sanctum')
        self.assertEqual((destination / 'runtime/module.py').read_text(), 'VALUE = 1\n')

    def test_restore_refuses_overwrite(self):
        build_bundle(self.root, self.bundle, 'abc123')
        destination = Path(self.temp.name) / 'restore'
        destination.mkdir()
        (destination / 'README.md').write_text('existing')
        with self.assertRaises(FileExistsError):
            restore_bundle(self.bundle, destination)

    def test_verify_rejects_traversal_member(self):
        evil = Path(self.temp.name) / 'evil.tar.gz'
        with tarfile.open(evil, 'w:gz') as archive:
            info = tarfile.TarInfo('../escape.txt')
            info.size = 1
            import io
            archive.addfile(info, io.BytesIO(b'x'))
        with self.assertRaises(ValueError):
            verify_bundle(evil)


if __name__ == '__main__':
    unittest.main()
