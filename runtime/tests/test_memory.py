from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from memory import Memory


class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'memory.sqlite'
        self.memory = Memory(self.path)

    def tearDown(self):
        self.memory.close()
        self.temp.cleanup()

    def test_candidate_requires_explicit_promotion(self):
        self.memory.add_candidate('a','sanctum','rule','candidate text','source',observed=1)
        self.assertEqual(self.memory.current('sanctum'), [])
        promoted = self.memory.decide('a',1,'promoted')
        self.assertEqual(promoted['state'],'promoted')
        self.assertEqual([item['id'] for item in self.memory.current('sanctum')], ['a'])

    def test_supersession_removes_old_entry_from_current_view(self):
        self.memory.add_candidate('a','sanctum','rule','old','source',observed=1)
        self.memory.decide('a',1,'promoted')
        self.memory.add_candidate('b','sanctum','rule','new','source2',observed=2)
        self.memory.decide('b',1,'promoted',supersedes='a')
        self.assertEqual(self.memory.get('a')['state'],'superseded')
        self.assertEqual([item['id'] for item in self.memory.current('sanctum')], ['b'])

    def test_stale_revision_and_cross_scope_supersession_rejected(self):
        self.memory.add_candidate('a','sanctum','rule','old','source',observed=1)
        with self.assertRaises(ValueError): self.memory.decide('a',2,'promoted')
        self.memory.decide('a',1,'promoted')
        self.memory.add_candidate('b','project','rule','new','source2',observed=2)
        with self.assertRaises(ValueError): self.memory.decide('b',1,'promoted',supersedes='a')

    def test_export_has_integrity_digest_and_history(self):
        self.memory.add_candidate('a','sanctum','rule','text','source',observed=1)
        self.memory.decide('a',1,'promoted')
        payload = self.memory.export()
        self.assertEqual(payload['schema_version'],1)
        self.assertTrue(payload['digest'])
        self.assertEqual(len(payload['history']),2)
