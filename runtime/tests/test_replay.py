from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from replay import build_case, minimize, run_case, verify_case
from sanctum import evaluate_trace


class ReplayTests(unittest.TestCase):
    def test_failure_trace_becomes_replayable_case(self):
        events = [{
            'event':'route',
            'data':{'manifest':{'task':{'bounded':True},'mechanisms':[],
                                'ikonn':{},'capability_evidence':{}}},
        }]
        case = build_case(events,'scope-regression',expected_status='FAIL',source='watcher:1')
        self.assertTrue(verify_case(case))
        result = run_case(case,evaluate_trace)
        self.assertTrue(result['pass'])
        self.assertTrue(any(item['id']=='SCOPE-LOCK-001' for item in result['result']['failures']))

    def test_nonsemantic_events_are_dropped(self):
        events = [{'event':'tool_blob','data':{'secret':'nope'}},
                  {'event':'action','data':{'guard_decision':'deny','dispatched':False,'payload':'secret'}}]
        minimized = minimize(events)
        self.assertEqual(len(minimized),1)
        self.assertNotIn('payload',minimized[0]['data'])

    def test_tampered_case_is_rejected(self):
        case = build_case([{'event':'action','data':{'guard_decision':'deny','dispatched':False}}], 'x')
        case['events'][0]['data']['dispatched'] = True
        with self.assertRaises(ValueError): verify_case(case)
