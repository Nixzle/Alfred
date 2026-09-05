#!/usr/bin/env python3
"""Dependency-free executable harness for the Sanctum control plane."""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
import platform
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "runtime"
CAPABILITIES = RUNTIME / "capabilities.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def capability_freshness(capability, context, observed_at=None):
    """Validate trusted local evidence against the requesting execution context."""
    if capability.get('status') != 'VERIFIED':
        return 'UNVERIFIED'
    for key in ('surface', 'host_id', 'session_id'):
        if not context.get(key) or capability.get(key) != context[key]:
            return 'CONTEXT_MISMATCH'
    try:
        now = dt.datetime.fromisoformat(observed_at) if observed_at else dt.datetime.now(dt.timezone.utc)
        probe = dt.datetime.fromisoformat(capability['last_probe'])
        expiry = dt.datetime.fromisoformat(capability['expires_at'])
        if any(value.tzinfo is None for value in (now, probe, expiry)):
            return 'INVALID'
        if probe > now or expiry <= probe:
            return 'INVALID'
        if now >= expiry or (now-probe).total_seconds() > 300:
            return 'STALE'
    except (ValueError, TypeError, KeyError):
        return 'INVALID'
    return 'VERIFIED'


def surface_capability(surface: str, path: Path = CAPABILITIES) -> dict[str, Any]:
    data = load_json(path)
    return data.get("surfaces", {}).get(surface, {
        "status": "UNVERIFIED",
        "autonomous_workers": "unknown",
        "last_probe": None,
    })


def route_task(task: dict[str, Any], capability: dict[str, Any]) -> dict[str, Any]:
    mechanisms: list[str] = []
    reasons: list[str] = []

    def add(name: str, reason: str) -> None:
        if name not in mechanisms:
            mechanisms.append(name)
            reasons.append(reason)

    if task.get("research"):
        add("Cerebro", "material external/research uncertainty")
        add("Archives", "retrieve reusable doctrine before reinventing it")
    if task.get("bounded"):
        add("Scope Lock", "bounded work must not absorb adjacent improvements")
    if task.get("write"):
        if task.get("project") or task.get("consequential"):
            add("Scout First", "read current state before consequential writes")
        add("Evidence Lock", "define proof before implementation")
        add("TVA", "check task scope and timeline divergence; actual tool authority remains binding")
    if task.get("consequential"):
        add("Council of Reeds", "consequential judgment requires adversarial review")
        add("Web of Destiny", "claim strength should be checked against evidence")
    if task.get("multi_step") or task.get("write") or task.get("consequential"):
        add("Watcher", "capture route/evidence/outcome state")

    ikonn_helpful = any(task.get(k) for k in ("parallel", "isolate", "persistent", "competing"))
    autonomous = capability.get("autonomous_workers")
    freshness = capability_freshness(capability, task)
    if ikonn_helpful and autonomous is True and freshness == 'VERIFIED':
        ikonn = {
            "status": "selected",
            "reason": "autonomous workers materially help and the surface capability is verified",
        }
        add("Images of Ikonn", "autonomous worker capability is both useful and available")
    elif ikonn_helpful:
        ikonn = {
            "status": "considered_unavailable",
            "reason": "autonomous workers would materially help but are not verified available on this surface",
        }
    else:
        ikonn = {"status": "not_needed", "reason": "single-threaded execution is sufficient"}

    if not mechanisms:
        invocation = "Sanctum: Direct route."
    elif "Cerebro" in mechanisms:
        invocation = "I'm entering the Sanctum. I'm using Cerebro to increase my reach."
    elif "Scope Lock" in mechanisms:
        invocation = "I'm entering the Sanctum. Scope Lock is going on before I touch the work."
    else:
        invocation = "I'm entering the Sanctum. The route is set before execution begins."

    if ikonn["status"] == "selected":
        invocation += " Images of Ikonn are available for this route; deployment still needs scoped authority."
    elif ikonn["status"] == "considered_unavailable":
        invocation += " Images of Ikonn would help here, but this runtime has not proved it can cast them."

    return {
        "schema_version": 1,
        "generated_at": now_iso(),
        "surface": task.get("surface", "unknown"),
        "task": task,
        "capability_evidence": {
            **{key:capability.get(key) for key in ('surface','host_id','session_id','expires_at')},
            "freshness": freshness,
            "status": capability.get("status", "UNVERIFIED"),
            "last_probe": capability.get("last_probe"),
            "autonomous_workers": autonomous,
        },
        "mechanisms": mechanisms,
        "reasons": reasons,
        "ikonn": ikonn,
        "invocation": invocation,
    }


def check_guard(capsule: dict[str, Any], action: str, target: str | None) -> dict[str, Any]:
    authority = capsule.get("authority", {})
    allowed_actions = authority.get("allowed_actions", [])
    approval_actions = authority.get("approval_required_actions", [])
    scope = capsule.get("scope", {})
    allowed_targets = scope.get("allowed_targets", scope.get("write_targets", []))

    if action not in allowed_actions:
        return {"decision": "deny", "reason": f"action {action!r} is outside granted authority"}
    if target and allowed_targets and not any(fnmatch.fnmatch(target, pat) for pat in allowed_targets):
        return {"decision": "deny", "reason": f"target {target!r} is outside Scope Lock"}
    if action in approval_actions:
        return {"decision": "require_approval", "reason": f"action {action!r} requires human approval"}
    return {"decision": "allow", "reason": "action is inside declared scope and authority"}


def append_trace(path: Path, event: str, data: dict[str, Any]) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"timestamp": now_iso(), "event": event, "data": data}
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
    return record


def read_trace(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    events = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.strip():
            events.append(json.loads(raw))
    return events


def evaluate_trace(events: list[dict[str, Any]]) -> dict[str, Any]:
    failures: list[dict[str, str]] = []
    checks = 0
    passed = 0
    research_requested = False
    research_results = []
    for record in events:
        before = len(failures)
        checked_before = checks
        event = record.get("event")
        data = record.get("data", {})
        if event == "route":
            checks += 1
            manifest = data.get("manifest", data)
            task = manifest.get("task", {})
            research_requested = research_requested or bool(task.get('research'))
            mechanisms = set(manifest.get("mechanisms", []))
            if task.get("bounded") and "Scope Lock" not in mechanisms:
                failures.append({"id": "SCOPE-LOCK-001", "reason": "bounded route omitted Scope Lock"})
            if task.get("write") and "Evidence Lock" not in mechanisms:
                failures.append({"id": "EVIDENCE-LOCK-001", "reason": "write route omitted Evidence Lock"})
            if task.get("consequential") and "Council of Reeds" not in mechanisms:
                failures.append({"id": "COUNCIL-ROUTE-001", "reason": "consequential route omitted Council"})
            if task.get("research") and "Cerebro" not in mechanisms:
                failures.append({"id": "CEREBRO-ROUTE-001", "reason": "research route omitted Cerebro"})
            ikonn = manifest.get("ikonn", {})
            cap = manifest.get("capability_evidence", {})
            if ikonn.get("status") == "selected" and (cap.get("autonomous_workers") is not True or
                    capability_freshness(cap, task, manifest.get('generated_at')) != 'VERIFIED'):
                failures.append({"id": "IKONN-CAPABILITY-001", "reason": "Images selected without verified autonomous-worker capability"})
        elif event == "action":
            checks += 1
            if data.get("guard_decision") == "deny" and data.get("dispatched"):
                failures.append({"id": "TVA-GUARD-001", "reason": "denied action was dispatched"})
        elif event == "completion":
            checks += 1
            if data.get('claim')=='all_complete':
                try:
                    from .delivery import evaluate as evaluate_delivery
                except ImportError:
                    from delivery import evaluate as evaluate_delivery
                result=evaluate_delivery(data.get('acceptance',[]),data.get('results',[]))
                if result['status']!='COMPLETE':
                    failures.append({'id':'DELIVERY-CONTRACT-001','reason':', '.join(result['issues'])})
            if data.get("claim") == "runtime_verified" and data.get("verification") != "runtime":
                failures.append({"id": "CLAIM-STRENGTH-001", "reason": "runtime claim lacks runtime evidence"})
        elif event == 'research':
            try:
                from .research_quality import evaluate
            except ImportError:
                from research_quality import evaluate
            checks += 1
            result = evaluate(data.get('receipt',{}), data.get('review'))
            research_results.append(result)
            if result['status']=='FAIL':
                failures.append({'id':'RESEARCH-RECEIPT-001','reason':', '.join(result['issues'])})
        if checks>checked_before and len(failures)==before:
            passed += 1
    return {
        "checks": checks,
        "failures": failures,
        "passed": passed,
        "research_quality": research_results or 'NOT_EVALUATED',
        "scope": 'Recognized trace checks only; not a whole-task quality verdict',
        "status": ('FAIL' if failures else 'NOT_EVALUATED' if not checks else
                   'PARTIAL' if research_requested and not research_results else 'PASS'),
    }


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def lint_repo(root: Path = ROOT) -> dict[str, Any]:
    issues: list[dict[str, str]] = []
    md_files = list(root.rglob("*.md"))

    regression_ids: dict[str, str] = {}
    rid = re.compile(r"^###\s+([A-Z][A-Z0-9-]+-\d{3})\b", re.M)
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(root))
        for value in rid.findall(text):
            if value in regression_ids:
                issues.append({"id": "DUPLICATE-REGRESSION-ID", "file": rel, "detail": value})
            regression_ids[value] = rel
        if re.search(r"\bSpellbook maneuvers?\b", text, re.I):
            issues.append({"id": "TERMINOLOGY-DRIFT", "file": rel, "detail": "use Spellbooks for the collection"})
        for link in markdown_links(text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (path.parent / link.split("#", 1)[0]).resolve()
            if link and not target.exists():
                issues.append({"id": "BROKEN-LOCAL-LINK", "file": rel, "detail": link})

    bootstrap = root / "bootstrap" / "README.md"
    if bootstrap.exists() and "SANCTUM-BOOTSTRAP-V1" not in bootstrap.read_text(encoding="utf-8"):
        issues.append({"id": "BOOTSTRAP-MARKER", "file": "bootstrap/README.md", "detail": "missing SANCTUM-BOOTSTRAP-V1"})

    return {"files_checked": len(md_files), "issues": issues, "status": "PASS" if not issues else "FAIL"}


def dashboard_data(path=CAPABILITIES, context=None) -> dict[str, Any]:
    caps = load_json(path)
    context = context or {}
    lint = lint_repo()
    surfaces = []
    for name, cap in caps.get("surfaces", {}).items():
        surfaces.append({
            "surface": name,
            "status": capability_freshness(cap, {**context, 'surface':name}),
            "last_probe": cap.get("last_probe"),
            "autonomous_workers": cap.get("autonomous_workers"),
        })
    return {"generated_at": now_iso(), "surfaces": surfaces, "doctrine_lint": lint}


def dashboard_markdown(data: dict[str, Any]) -> str:
    lines = ["# Sanctum Runtime Dashboard", "", f"Generated: `{data['generated_at']}`", "", "## Surface capability freshness", "", "| Surface | Status | Last probe | Images of Ikonn capability |", "| --- | --- | --- | --- |"]
    for row in data["surfaces"]:
        lines.append(f"| {row['surface']} | {row['status']} | {row['last_probe'] or 'never'} | {row['autonomous_workers']} |")
    lint = data["doctrine_lint"]
    lines += ["", "## Doctrine lint", "", f"Status: **{lint['status']}**", f"Files checked: {lint['files_checked']}", f"Issues: {len(lint['issues'])}"]
    if lint["issues"]:
        lines += ["", "### Issues"]
        for item in lint["issues"]:
            lines.append(f"- `{item['id']}` {item.get('file', '')}: {item.get('detail', '')}")
    return "\n".join(lines) + "\n"


def task_from_args(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "description": args.task,
        "surface": args.surface,
        "host_id": args.host_id,
        "session_id": args.session_id,
        "project": args.project,
        "research": args.research,
        "consequential": args.consequential,
        "bounded": args.bounded,
        "write": args.write,
        "multi_step": args.multi_step,
        "parallel": args.parallel,
        "isolate": args.isolate,
        "persistent": args.persistent,
        "competing": args.competing,
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="sanctum")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("route")
    p.add_argument("--task", required=True)
    p.add_argument("--surface", required=True)
    p.add_argument('--capabilities', type=Path, default=CAPABILITIES)
    p.add_argument('--host-id', default=platform.node())
    p.add_argument('--session-id', default=os.environ.get('CODEX_THREAD_ID'))
    for flag in ("project", "research", "consequential", "bounded", "write", "multi-step", "parallel", "isolate", "persistent", "competing"):
        p.add_argument(f"--{flag}", action="store_true", dest=flag.replace("-", "_"))

    p = sub.add_parser("guard")
    p.add_argument("--capsule", type=Path, required=True)
    p.add_argument("--action", required=True)
    p.add_argument("--target")

    p = sub.add_parser("trace")
    p.add_argument("--event", required=True)
    p.add_argument("--data", default="{}")
    p.add_argument("--out", type=Path, default=Path(".sanctum/traces.jsonl"))

    p = sub.add_parser("eval")
    p.add_argument("--trace", type=Path, required=True)

    sub.add_parser("lint")

    p = sub.add_parser("dashboard")
    p.add_argument("--out", type=Path)
    p.add_argument('--capabilities', type=Path, default=CAPABILITIES)
    p.add_argument('--host-id', default=platform.node())
    p.add_argument('--session-id', default=os.environ.get('CODEX_THREAD_ID'))

    args = parser.parse_args()
    if args.command == "route":
        task = task_from_args(args)
        result = route_task(task, surface_capability(args.surface, args.capabilities))
    elif args.command == "guard":
        result = check_guard(load_json(args.capsule), args.action, args.target)
    elif args.command == "trace":
        result = append_trace(args.out, args.event, json.loads(args.data))
    elif args.command == "eval":
        result = evaluate_trace(read_trace(args.trace))
    elif args.command == "lint":
        result = lint_repo()
    elif args.command == "dashboard":
        result = dashboard_data(args.capabilities, {'host_id':args.host_id, 'session_id':args.session_id})
        text = dashboard_markdown(result)
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(text, encoding="utf-8")
            result = {**result, "written": str(args.out)}
        else:
            print(text, end="")
            return 0
    else:
        raise AssertionError(args.command)

    print(json.dumps(result, indent=2, sort_keys=True))
    if args.command in {"lint", "eval"} and result.get("status") != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
