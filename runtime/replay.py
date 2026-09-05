"""Turn bounded Watcher trace evidence into replayable Web regression cases."""
import hashlib
import json

ALLOWED_EVENTS = {"route", "action", "completion", "research"}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def minimize(events):
    result = []
    for record in events:
        event = record.get("event")
        if event not in ALLOWED_EVENTS:
            continue
        data = record.get("data", {})
        if event == "route":
            kept = {"manifest": data.get("manifest", data)}
        elif event == "action":
            kept = {key: data.get(key) for key in ("guard_decision", "dispatched")}
        elif event == "completion":
            kept = {key: data.get(key) for key in ("claim", "verification", "acceptance", "results")}
        else:
            kept = {key: data.get(key) for key in ("receipt", "review")}
        result.append({"event": event, "data": kept})
    return result


def build_case(events, case_id, expected_status="PASS", source=None):
    if not isinstance(case_id, str) or not case_id or len(case_id) > 128:
        raise ValueError("bounded case id required")
    if expected_status not in {"PASS", "FAIL", "PARTIAL", "NOT_EVALUATED"}:
        raise ValueError("invalid expected status")
    minimized = minimize(events)
    if not minimized:
        raise ValueError("no replayable events")
    body = {
        "schema_version": 1,
        "id": case_id,
        "source": source,
        "events": minimized,
        "expected_status": expected_status,
    }
    body["digest"] = digest(body)
    return body


def verify_case(case):
    supplied = case.get("digest")
    body = {key: value for key, value in case.items() if key != "digest"}
    if not supplied or supplied != digest(body):
        raise ValueError("replay case digest mismatch")
    return True


def run_case(case, evaluator):
    verify_case(case)
    result = evaluator(case["events"])
    return {
        "id": case["id"],
        "expected": case["expected_status"],
        "observed": result["status"],
        "pass": result["status"] == case["expected_status"],
        "result": result,
    }
