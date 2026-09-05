import tempfile
from pathlib import Path
import unittest

from runtime.release_manifest import build_manifest, verify_manifest


class ReleaseManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / 'a.txt').write_text('one', encoding='utf-8')
        (self.root / 'b.txt').write_text('two', encoding='utf-8')

    def tearDown(self):
        self.temp.cleanup()

    def test_manifest_verifies_clean_tree(self):
        manifest = build_manifest(self.root, 'rev1')
        verdict = verify_manifest(self.root, manifest)
        self.assertEqual(verdict['status'], 'PASS')
        self.assertEqual(verdict['revision'], 'rev1')

    def test_manifest_detects_content_drift(self):
        manifest = build_manifest(self.root, 'rev1')
        (self.root / 'a.txt').write_text('changed', encoding='utf-8')
        verdict = verify_manifest(self.root, manifest)
        self.assertEqual(verdict['status'], 'FAIL')
        self.assertEqual(verdict['failures'][0]['file'], 'a.txt')

    def test_manifest_digest_tamper_fails(self):
        manifest = build_manifest(self.root, 'rev1')
        manifest['revision'] = 'evil'
        with self.assertRaises(ValueError):
            verify_manifest(self.root, manifest)


if __name__ == '__main__':
    unittest.main()
