"""Account for already captured, disjoint Codex JSONL logs; never execute a prompt."""
import argparse
import json
from pathlib import Path


def usage(text):
    """Per-turn totals only. A missing/failed/pending turn makes the sum partial."""
    total = 0
    measured = 0
    complete = True
    pending = 0
    for line in text.splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        kind = event.get("type")
        if kind == "turn.started":
            pending += 1
        elif kind in ("turn.failed", "error"):
            complete = False
        elif kind == "turn.completed":
            pending = max(0, pending - 1)
            record = event.get("usage") or {}
            values = [record.get("input_tokens"), record.get("output_tokens")]
            if not all(type(n) is int and n >= 0 for n in values):
                complete = False
                continue
            total += sum(values)
            measured += 1
    return {"tokens": total if measured else None,
            "complete": complete and pending == 0 and measured > 0,
            "measured_turns": measured}


def receipt(estimate, execution, vision=None):
    if type(estimate) is not int or estimate < 0:
        raise ValueError("estimate must be a nonnegative integer")
    actual = execution["tokens"] if execution["complete"] else None
    overhead = vision["tokens"] if vision and vision["complete"] else None
    delta = actual - estimate if actual is not None else None
    return {"estimate": estimate, "execution": execution,
            "difference": delta,
            "difference_percent": 100 * delta / estimate if delta is not None and estimate else None,
            "vision": vision,
            "combined": actual + overhead if actual is not None and overhead is not None else None}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--estimate", type=int, required=True)
    parser.add_argument("--execution", type=Path, required=True)
    parser.add_argument("--vision", type=Path)
    parser.add_argument("--disjoint", action="store_true",
                        help="Confirm supplied logs contain separate, non-overlapping model calls")
    args = parser.parse_args()
    if args.vision and (not args.disjoint or args.vision.resolve() == args.execution.resolve()):
        parser.error("Separate Vision logs require distinct paths and --disjoint")
    try:
        result = receipt(args.estimate, usage(args.execution.read_text(encoding="utf-8-sig")),
                         usage(args.vision.read_text(encoding="utf-8-sig")) if args.vision else None)
    except (ValueError, TypeError, AttributeError, OSError) as error:
        parser.error(str(error))
    result["scope"] = "Supplied logs through capture cutoff; excludes subsequent reporting calls"
    print(json.dumps(result, indent=2))
