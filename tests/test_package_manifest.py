import tempfile
from pathlib import Path
import unittest

from scripts.package_manifest import build, verify


class PackageManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / 'README.md').write_text('alfred', encoding='utf-8')
        (self.root / 'scripts').mkdir()
        (self.root / 'scripts' / 'x.py').write_text('VALUE = 1\n', encoding='utf-8')

    def tearDown(self):
        self.temp.cleanup()

    def test_manifest_passes_clean_tree(self):
        manifest = build(self.root, 'rev1')
        self.assertEqual(verify(self.root, manifest)['status'], 'PASS')

    def test_manifest_detects_change(self):
        manifest = build(self.root, 'rev1')
        (self.root / 'README.md').write_text('changed', encoding='utf-8')
        self.assertEqual(verify(self.root, manifest)['status'], 'FAIL')

    def test_manifest_rejects_tampered_revision(self):
        manifest = build(self.root, 'rev1')
        manifest['revision'] = 'other'
        with self.assertRaises(ValueError):
            verify(self.root, manifest)


if __name__ == '__main__':
    unittest.main()
