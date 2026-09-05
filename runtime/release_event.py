"""One-shot local validation event adapter. No watcher, model, network or dispatcher."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import time

try:
    from .presence import Attention
except ImportError:
    from presence import Attention

REQUIRED = {'tests', 'lint', 'acceptance', 'diff'}


def observe(receipt, db, project, now=None):
    """Receipt and project are trusted local owner inputs; not remote worker payloads.

    Original completion time is preserved on replay. Content digest is the incident
    identity; equivalent key ordering cannot manufacture a new event.
    """
    started = time.perf_counter()
    checks = receipt['checks']
    by_name = {c['check']: c for c in checks}
    if len(by_name) != len(checks) or set(by_name) != REQUIRED:
        raise ValueError('complete unique local release checks required')
    for check in checks:
        if type(check.get('exit_code')) is not int or type(check.get('passed')) is not bool:
            raise ValueError('typed check outcomes required')
        if check['passed'] and check['exit_code'] != 0:
            raise ValueError('inconsistent check outcome')
    passed = all(c['passed'] for c in checks)
    if receipt.get('status') != ('PASS' if passed else 'FAIL'):
        raise ValueError('inconsistent release summary')
    completed = datetime.datetime.fromisoformat(receipt['generated_at'])
    if completed.tzinfo is None:
        raise ValueError('timezone-aware completion time required')
    incident = hashlib.sha256(json.dumps(receipt, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    event = dict(source='local-validation', project=project, incident=incident,
                 kind='result' if passed else 'blocker', observed_at=completed.timestamp(),
                 revision=receipt['revision'])
    policy = dict(active_project=project, ttl_seconds=3600, investigations_per_hour=0)
    ledger = Attention(db)
    try:
        decision = ledger.evaluate(event, policy, now=now)
    finally:
        ledger.close()
    return dict(event=event, decision=decision, elapsed_ms=round((time.perf_counter()-started)*1000, 3),
                scope='Live local validation to private Presence ledger; notify is a recommendation printed to caller, not an external message')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', type=Path, required=True)
    parser.add_argument('--db', required=True)
    parser.add_argument('--project', required=True)
    args = parser.parse_args()
    print(json.dumps(observe(json.loads(args.receipt.read_text(encoding='utf-8')), args.db, args.project), indent=2))
