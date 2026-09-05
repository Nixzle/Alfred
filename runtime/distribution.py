"""Check portable Ultron semantic parity and runtime-profile completeness.

This checker proves repository/bootstrap configuration only. It does not prove that
external tools, permissions, memory reach, autonomous workers, or side-effect authority
actually exist; those remain runtime-profile evidence and must be re-probed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PORTABLE = ROOT / "bootstrap" / "PORTABLE_ULTRON.md"
BOOTSTRAP = ROOT / "bootstrap" / "README.md"
THEATRICS = ROOT / "THEATRICS.md"
MEMBERS = ROOT / "members" / "README.md"
ROOT_README = ROOT / "README.md"

PORTABLE_MARKER = "SANCTUM-PORTABLE-ULTRON-V1"
BOOTSTRAP_MARKER = "SANCTUM-BOOTSTRAP-V1"
REQUIRED_MEMBERS = (
    "Ultron Prime",
    "Cerebro v4",
    "Ultron Bots v2",
    "Images of Ikonn v2",
    "Watcher v1.1",
    "Web of Destiny",
    "TVA v1",
    "Council of Reeds",
)
REQUIRED_THEATRICAL_CONCEPTS = (
    "I'm entering the Sanctum",
    "Cerebro",
    "Mind Stone",
    "Council of Reeds",
    "Watcher",
    "Web of Destiny",
    "TVA",
    "Images of Ikonn",
    "Ultron Bots",
)
SEMANTIC_KEYS = (
    "ultron_identity",
    "member_roster",
    "sanctum_architecture",
    "prime_sense",
    "archives_spellbooks",
    "salvage_first",
    "engineering_excellence",
    "failure_harvest",
    "enforcement_vocabulary",
    "theatrics",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def repository_parity(root: Path = ROOT) -> dict[str, Any]:
    issues: list[str] = []
    files = {
        "portable": root / "bootstrap" / "PORTABLE_ULTRON.md",
        "bootstrap": root / "bootstrap" / "README.md",
        "theatrics": root / "THEATRICS.md",
        "members": root / "members" / "README.md",
        "root": root / "README.md",
    }
    missing = [name for name, path in files.items() if not path.is_file()]
    if missing:
        return {"status": "FAIL", "issues": [f"missing canonical file: {name}" for name in missing]}

    portable, bootstrap, theatrics, members, root_text = (
        read(files["portable"]), read(files["bootstrap"]), read(files["theatrics"]),
        read(files["members"]), read(files["root"]),
    )
    if PORTABLE_MARKER not in portable:
        issues.append("portable contract marker missing")
    if BOOTSTRAP_MARKER not in bootstrap or BOOTSTRAP_MARKER not in portable:
        issues.append("bootstrap marker mismatch")
    for member in REQUIRED_MEMBERS:
        if member not in members or member not in root_text or member not in portable:
            issues.append(f"member parity missing: {member}")
    for concept in REQUIRED_THEATRICAL_CONCEPTS:
        if concept not in theatrics or concept not in portable:
            issues.append(f"theatrical parity missing: {concept}")
    for phrase in ("Prime Sense", "Prime Memory", "Mindscape", "Salvage First", "Failure Harvest"):
        if phrase not in portable:
            issues.append(f"portable doctrine missing: {phrase}")
    if "DOCUMENTED" not in portable or "CHECKED" not in portable or "ENFORCED" not in portable or "OBSERVED" not in portable:
        issues.append("enforcement vocabulary missing")
    return {"status": "PASS" if not issues else "FAIL", "issues": issues}


def profile_parity(profile: dict[str, Any]) -> dict[str, Any]:
    issues: list[str] = []
    if profile.get("contract") != PORTABLE_MARKER:
        issues.append("portable contract mismatch")
    if profile.get("bootstrap") != BOOTSTRAP_MARKER:
        issues.append("bootstrap contract mismatch")
    semantic = profile.get("semantic_parity")
    if not isinstance(semantic, dict):
        issues.append("semantic_parity object required")
    else:
        for key in SEMANTIC_KEYS:
            if semantic.get(key) is not True:
                issues.append(f"semantic parity unverified: {key}")
    validation = profile.get("validation")
    if not isinstance(validation, dict):
        issues.append("validation object required")
    else:
        if not validation.get("observed_at"):
            issues.append("validation observed_at required")
        if not isinstance(validation.get("evidence"), list) or not validation.get("evidence"):
            issues.append("validation evidence required")
    for section in ("capabilities", "authority", "data_and_memory"):
        if not isinstance(profile.get(section), dict):
            issues.append(f"{section} object required")
    return {"status": "PASS" if not issues else "FAIL", "issues": issues}


def evaluate(profile: dict[str, Any] | None = None, root: Path = ROOT) -> dict[str, Any]:
    repo = repository_parity(root)
    result: dict[str, Any] = {"repository_semantic_parity": repo}
    if profile is not None:
        result["surface_profile_parity"] = profile_parity(profile)
    statuses = [value["status"] for value in result.values()]
    result["status"] = "PASS" if all(status == "PASS" for status in statuses) else "FAIL"
    result["scope"] = (
        "Semantic/bootstrap parity only. Live tools, permissions, memory/data reach, "
        "sandboxing and side-effect authority require independent runtime evidence."
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path)
    args = parser.parse_args()
    profile = json.loads(args.profile.read_text(encoding="utf-8")) if args.profile else None
    result = evaluate(profile)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
