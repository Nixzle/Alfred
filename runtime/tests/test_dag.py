import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from dag import Dag


class DagTests(unittest.TestCase):
    def test_dependency_order_retry_restore_and_fork(self):
        dag = Dag({'scan': {}, 'build': {'depends_on':['scan'], 'max_retries':1}, 'verify': {'depends_on':['build']}})
        self.assertEqual(dag.ready(), ['scan'])
        dag.start('scan'); dag.finish('scan', ['scan-evidence'])
        self.assertEqual(dag.ready(), ['build'])
        dag.start('build'); dag.fail('build', 'Transient')
        self.assertEqual(dag.ready(), ['build'])
        snap = dag.snapshot()
        restored = Dag.restore(snap)
        self.assertEqual(restored.ready(), ['build'])
        forked = restored.fork('alternate')
        self.assertTrue(forked.run_id.endswith('.alternate'))
        self.assertEqual(forked.events[-1]['event'], 'forked')

    def test_failed_dependency_blocks_downstream(self):
        dag = Dag({'a': {}, 'b': {'depends_on':['a']}})
        dag.start('a'); dag.fail('a', 'Fatal')
        self.assertEqual(dag.nodes['a']['status'], 'failed')
        self.assertEqual(dag.nodes['b']['status'], 'blocked')
        self.assertEqual(dag.ready(), [])

    def test_cycle_and_missing_dependency_rejected(self):
        with self.assertRaises(ValueError): Dag({'a': {'depends_on':['b']}})
        with self.assertRaises(ValueError): Dag({'a': {'depends_on':['b']}, 'b': {'depends_on':['a']}})

    def test_completion_requires_evidence(self):
        dag = Dag({'a': {}})
        dag.start('a')
        with self.assertRaises(ValueError): dag.finish('a', [])
