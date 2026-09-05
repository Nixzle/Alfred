from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from delivery import evaluate, dependency_gate
from sanctum import evaluate_trace


class DeliveryTests(unittest.TestCase):
    def test_partial_or_wrong_deployment_level_cannot_close_contract(self):
        required=[dict(id='upgrade',level='merged'),dict(id='monitor',level='live')]
        results=[dict(id='upgrade',status='complete',level='merged',evidence=['commit']),
                 dict(id='monitor',status='complete',level='tested',evidence=['test'])]
        self.assertEqual(evaluate(required,results)['status'],'INCOMPLETE')
        results[1].update(level='live',evidence=['live-probe'])
        self.assertEqual(evaluate(required,results)['status'],'COMPLETE')

    def test_missing_evidence_or_extra_item_is_not_completion(self):
        self.assertEqual(evaluate([],[])['status'],'INCOMPLETE')
        self.assertEqual(evaluate([dict(id='a',level='tested')],[dict(id='b')])['status'],'INCOMPLETE')

    def test_failure_and_unknown_prevent_dependent_action(self):
        for outcome in ('failed','unknown_outcome',None):
            self.assertEqual(dependency_gate(['commit'],{'commit':{'status':outcome}})['decision'],'BLOCK')
        self.assertEqual(dependency_gate(['commit'],{'commit':{'status':'verified_success'}})['decision'],'READY')

    def test_all_complete_trace_requires_contract(self):
        self.assertEqual(evaluate_trace([dict(event='completion',data={'claim':'all_complete'})])['status'],'FAIL')
