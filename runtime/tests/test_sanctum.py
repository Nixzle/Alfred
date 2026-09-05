import importlib.util
import unittest
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("sanctum", ROOT / "runtime" / "sanctum.py")
sanctum = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sanctum)


class SanctumRuntimeTests(unittest.TestCase):
    def test_bounded_write_route_uses_scope_and_evidence_lock(self):
        task = {"surface": "codex", "bounded": True, "write": True, "project": True}
        result = sanctum.route_task(task, {"status": "VERIFIED", "autonomous_workers": False})
        self.assertIn("Scope Lock", result["mechanisms"])
        self.assertIn("Evidence Lock", result["mechanisms"])
        self.assertIn("TVA", result["mechanisms"])

    def test_ikonn_unavailable_is_visible(self):
        task = {"surface": "codex", "parallel": True}
        result = sanctum.route_task(task, {"status": "VERIFIED", "autonomous_workers": False})
        self.assertEqual(result["ikonn"]["status"], "considered_unavailable")
        self.assertIn("Images of Ikonn would help here", result["invocation"])

    def test_ikonn_selected_only_when_verified_available(self):
        task, capability = self.fresh_capability()
        result = sanctum.route_task(task, capability)
        self.assertEqual(result["ikonn"]["status"], "selected")
        self.assertIn("Images of Ikonn", result["mechanisms"])

    def fresh_capability(self):
        task = dict(surface='codex', host_id='host', session_id='session', parallel=True)
        now = dt.datetime.now(dt.timezone.utc)
        return task, dict(status='VERIFIED', autonomous_workers=True,
                         surface='codex', host_id='host', session_id='session',
                         last_probe=now.isoformat(), expires_at=(now+dt.timedelta(minutes=5)).isoformat())

    def test_invalid_capabilities_never_select_workers(self):
        cases = [dict(status='UNVERIFIED'), dict(last_probe=None), dict(last_probe='invalid'),
                 dict(last_probe='2000-01-01T00:00:00+00:00'),
                 dict(last_probe='2999-01-01T00:00:00+00:00'), dict(expires_at=None),
                 dict(last_probe='2026-09-05T00:00:00'), dict(host_id='other'),
                 dict(session_id='other'), dict(surface='discord')]
        for change in cases:
            with self.subTest(change=change):
                task, cap = self.fresh_capability()
                cap.update(change)
                result = sanctum.route_task(task, cap)
                self.assertEqual(result['ikonn']['status'], 'considered_unavailable')

    def test_trace_rechecks_evidence_at_original_route_time(self):
        task, cap = self.fresh_capability()
        route = sanctum.route_task(task, cap)
        self.assertEqual(sanctum.evaluate_trace([dict(event='route', data=route)])['status'], 'PASS')
        route['capability_evidence']['status'] = 'UNVERIFIED'
        self.assertEqual(sanctum.evaluate_trace([dict(event='route', data=route)])['status'], 'FAIL')

    def test_guard_denies_out_of_scope_target(self):
        capsule = {
            "scope": {"allowed_targets": ["src/*.py"]},
            "authority": {"allowed_actions": ["write"]},
        }
        result = sanctum.check_guard(capsule, "write", "docs/README.md")
        self.assertEqual(result["decision"], "deny")

    def test_guard_requires_approval_when_declared(self):
        capsule = {
            "scope": {"allowed_targets": ["src/*"]},
            "authority": {
                "allowed_actions": ["deploy"],
                "approval_required_actions": ["deploy"],
            },
        }
        result = sanctum.check_guard(capsule, "deploy", "src/app")
        self.assertEqual(result["decision"], "require_approval")

    def test_eval_catches_selected_ikonn_without_capability(self):
        events = [
            {
                "event": "route",
                "data": {
                    "task": {"parallel": True},
                    "mechanisms": ["Images of Ikonn"],
                    "ikonn": {"status": "selected"},
                    "capability_evidence": {"autonomous_workers": False},
                },
            }
        ]
        result = sanctum.evaluate_trace(events)
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any(x["id"] == "IKONN-CAPABILITY-001" for x in result["failures"]))


if __name__ == "__main__":
    unittest.main()
