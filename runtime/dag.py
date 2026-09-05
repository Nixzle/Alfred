"""Deterministic dependency-graph execution state. No model calls and no effects."""
import hashlib
import json

TERMINAL = {"complete", "failed", "cancelled"}
VALID = {"pending", "ready", "running", "blocked", "complete", "failed", "cancelled"}


def _digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


class Dag:
    def __init__(self, nodes, run_id=None):
        if not isinstance(nodes, dict) or not nodes:
            raise ValueError("non-empty node map required")
        self.nodes = {}
        for name, spec in nodes.items():
            if not isinstance(name, str) or not name or len(name) > 128:
                raise ValueError("bounded node id required")
            deps = list(spec.get("depends_on", []))
            if len(deps) != len(set(deps)) or name in deps:
                raise ValueError("invalid dependencies")
            retries = int(spec.get("max_retries", 0))
            if not 0 <= retries <= 10:
                raise ValueError("max_retries out of range")
            self.nodes[name] = {
                "depends_on": deps,
                "max_retries": retries,
                "attempts": 0,
                "status": "pending",
                "evidence": [],
                "error_type": None,
            }
        for name, state in self.nodes.items():
            missing = set(state["depends_on"]) - set(self.nodes)
            if missing:
                raise ValueError(f"missing dependency for {name}: {sorted(missing)}")
        self._assert_acyclic()
        graph = {
            key: {"depends_on": value["depends_on"], "max_retries": value["max_retries"]}
            for key, value in self.nodes.items()
        }
        self.run_id = run_id or _digest(graph)[:24]
        self.sequence = 0
        self.events = []
        self._refresh()

    def _assert_acyclic(self):
        visiting, done = set(), set()

        def visit(name):
            if name in visiting:
                raise ValueError("cycle detected")
            if name in done:
                return
            visiting.add(name)
            for dep in self.nodes[name]["depends_on"]:
                visit(dep)
            visiting.remove(name)
            done.add(name)

        for name in self.nodes:
            visit(name)

    def _record(self, node, event, **data):
        self.sequence += 1
        self.events.append({
            "sequence": self.sequence,
            "run_id": self.run_id,
            "node": node,
            "event": event,
            "data": data,
        })

    def _refresh(self):
        for state in self.nodes.values():
            if state["status"] not in {"pending", "ready", "blocked"}:
                continue
            deps = [self.nodes[dep]["status"] for dep in state["depends_on"]]
            if any(status in {"failed", "cancelled"} for status in deps):
                state["status"] = "blocked"
            elif all(status == "complete" for status in deps):
                state["status"] = "ready"
            else:
                state["status"] = "pending"

    def ready(self):
        self._refresh()
        return sorted(name for name, state in self.nodes.items() if state["status"] == "ready")

    def start(self, node):
        self._refresh()
        state = self.nodes[node]
        if state["status"] != "ready":
            raise ValueError("node is not ready")
        state["attempts"] += 1
        state["status"] = "running"
        self._record(node, "started", attempt=state["attempts"])
        return state.copy()

    def finish(self, node, evidence):
        state = self.nodes[node]
        if state["status"] != "running":
            raise ValueError("node is not running")
        if not evidence:
            raise ValueError("completion requires evidence")
        state["evidence"] = list(evidence)
        state["status"] = "complete"
        state["error_type"] = None
        self._record(node, "completed", evidence=list(evidence))
        self._refresh()
        return state.copy()

    def fail(self, node, error_type):
        state = self.nodes[node]
        if state["status"] != "running":
            raise ValueError("node is not running")
        if not isinstance(error_type, str) or not error_type or len(error_type) > 128:
            raise ValueError("bounded error type required")
        state["error_type"] = error_type
        if state["attempts"] <= state["max_retries"]:
            state["status"] = "ready"
            event = "retry_ready"
        else:
            state["status"] = "failed"
            event = "failed"
        self._record(node, event, attempt=state["attempts"], error_type=error_type)
        self._refresh()
        return state.copy()

    def snapshot(self):
        self._refresh()
        return {
            "schema_version": 1,
            "run_id": self.run_id,
            "sequence": self.sequence,
            "nodes": json.loads(json.dumps(self.nodes)),
            "events": json.loads(json.dumps(self.events)),
        }

    @classmethod
    def restore(cls, snapshot):
        base = {
            key: {"depends_on": value["depends_on"], "max_retries": value["max_retries"]}
            for key, value in snapshot["nodes"].items()
        }
        obj = cls(base, run_id=snapshot["run_id"])
        obj.nodes = json.loads(json.dumps(snapshot["nodes"]))
        obj.sequence = int(snapshot["sequence"])
        obj.events = json.loads(json.dumps(snapshot["events"]))
        obj._refresh()
        return obj

    def fork(self, suffix):
        if not isinstance(suffix, str) or not suffix or len(suffix) > 32:
            raise ValueError("bounded fork suffix required")
        snap = self.snapshot()
        snap["run_id"] = f"{self.run_id}.{suffix}"
        forked = self.restore(snap)
        forked._record(None, "forked", parent_run_id=self.run_id)
        return forked
