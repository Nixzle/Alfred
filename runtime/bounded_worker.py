"""Restartable declarative worker: no shell, imports, network or dependency installs.

Trusted supervisor supplies immutable capsule + workspace. Worker operations are
untrusted JSON data. This boundary is enforced for these built-in operations only;
it is NOT an OS sandbox for arbitrary code executing under the same account.
"""
import argparse
import datetime as dt
import fnmatch
import hashlib
import json
from pathlib import Path, PurePosixPath
import time

from ledger import Ledger, Conflict


def digest(value):
    return hashlib.sha256(value).hexdigest()


class Broker:
    def __init__(self, ledger, capsule, workspace):
        self.ledger = ledger
        self.capsule = json.loads(json.dumps(capsule))
        self.root = Path(workspace).resolve(strict=True)
        if not self.root.is_dir():
            raise ValueError('workspace must exist')
        database = Path(ledger.db.execute('PRAGMA database_list').fetchone()[2]).resolve()
        if database.is_relative_to(self.root):
            raise ValueError('control database must be outside worker workspace')
        binding = (self.capsule['task_id'], self.capsule['worker_id'], str(self.root),
                   digest(json.dumps(self.capsule, sort_keys=True).encode()))
        ledger.db.execute('BEGIN IMMEDIATE')
        try:
            existing = ledger.db.execute('SELECT * FROM workers WHERE task=?', (binding[0],)).fetchone()
            if existing and tuple(existing) != binding:
                raise Conflict('worker binding changed; create a successor')
            if not existing:
                for row in ledger.db.execute('SELECT workspace FROM workers'):
                    other = Path(row[0])
                    if self.root.is_relative_to(other) or other.is_relative_to(self.root):
                        raise Conflict('worker workspaces cannot overlap')
                ledger.db.execute('INSERT INTO workers VALUES(?,?,?,?)', binding)
            ledger.db.execute('COMMIT')
        except BaseException:
            ledger.db.execute('ROLLBACK')
            raise

    def target(self, name):
        if not isinstance(name, str) or not name or '\\' in name or ':' in name:
            raise PermissionError('invalid relative path')
        parts = PurePosixPath(name).parts
        if name.startswith('/') or any(p in {'.', '..'} for p in name.split('/')):
            raise PermissionError('path traversal denied')
        if any(p.lower() in {'.git', '.sanctum', '.env', '.ssh'} or p.lower().startswith('.env.') for p in parts):
            raise PermissionError('protected target')
        path = self.root
        for part in parts:
            path = path / part
            if path.is_symlink() or (hasattr(path, 'is_junction') and path.is_junction()):
                raise PermissionError('linked path denied')
        resolved = path.resolve()
        if not resolved.is_relative_to(self.root):
            raise PermissionError('workspace escape')
        if resolved.exists() and resolved.stat().st_nlink > 1:
            raise PermissionError('hardlinked target denied')
        return resolved

    def decide(self, operation):
        cap = self.capsule
        task = self.ledger.get(cap['task_id'])
        if task['status'] != 'active' or task['worker'] != cap['worker_id']:
            return 'deny'
        expiry = dt.datetime.fromisoformat(cap['expires_at'])
        if expiry.tzinfo is None or expiry <= dt.datetime.now(dt.timezone.utc):
            return 'deny'
        action = operation.get('action')
        # Unsupported effects stay denied even if an untrusted plan asks for them.
        if action not in {'read', 'create'} or action not in cap['allowed_actions']:
            return 'deny'
        try:
            self.target(operation.get('target'))
        except (PermissionError, ValueError, OSError):
            return 'deny'
        if not any(fnmatch.fnmatchcase(operation['target'], pattern) for pattern in cap['allowed_targets']):
            return 'deny'
        if action in cap.get('approval_required_actions', []):
            return 'require_approval'
        return 'allow'

    def execute(self, operation):
        task_id, worker = self.capsule['task_id'], self.capsule['worker_id']
        op_id = operation['id']
        if not isinstance(op_id, str) or not op_id or len(op_id) > 100:
            raise ValueError('invalid operation ID')
        fp = digest(json.dumps(operation, sort_keys=True).encode())
        start = time.monotonic()
        # Single broker transaction prevents two dispatchers from racing the same
        # operation. intent is committed before effects to expose unknown outcomes.
        self.ledger.db.execute('BEGIN IMMEDIATE')
        try:
            decision = self.decide(operation)
            self.ledger.event(task_id, 'action_guard', worker=worker, member='TVA', operation=op_id, decision=decision)
            if decision != 'allow':
                self.ledger.db.execute('COMMIT')
                raise PermissionError(decision)
            prior = self.ledger.db.execute('SELECT * FROM effects WHERE task=? AND operation=?', (task_id, op_id)).fetchone()
            if prior:
                if prior['fingerprint'] != fp:
                    raise Conflict('operation ID reused with different payload')
                if prior['status'] == 'committed':
                    self.ledger.db.execute('COMMIT')
                    return json.loads(prior['result'])
                # An interrupted create is never dispatched twice. Reconcile its
                # expected postcondition; ambiguity requires operator review.
                path = self.target(operation['target'])
                expected = operation.get('text', '').encode()
                if operation['action'] != 'create' or not path.is_file() or path.stat().st_size != len(expected) or path.read_bytes() != expected:
                    raise Conflict('unknown outcome requires reconciliation')
                result = {'sha256': digest(expected), 'bytes': len(expected), 'reconciled': True}
                self.ledger.db.execute("UPDATE effects SET status='committed',result=? WHERE task=? AND operation=?", (json.dumps(result), task_id, op_id))
                self.ledger.event(task_id, 'effect_reconciled', worker=worker, operation=op_id, evidence_id=op_id)
                self.ledger.db.execute('COMMIT')
                return result
            self.ledger.db.execute('INSERT INTO effects VALUES(?,?,?,?,?)', (task_id, op_id, fp, 'intent', '{}'))
            self.ledger.event(task_id, 'effect_intent', worker=worker, operation=op_id)
            self.ledger.db.execute('COMMIT')
        except BaseException:
            if self.ledger.db.in_transaction:
                self.ledger.db.execute('ROLLBACK')
            raise
        try:
            # Only one active supervisor per workspace is supported; outside
            # processes with same-account write access are not contained here.
            if self.decide(operation) != 'allow':
                raise PermissionError('authority no longer valid')
            path = self.target(operation['target'])
            if operation['action'] == 'create':
                data = operation['text'].encode()
                if len(data) > 1024 * 1024:
                    raise ValueError('artifact exceeds one MiB')
                # Exclusive create never overwrites user files, even after restart.
                with path.open('xb') as stream:
                    stream.write(data)
                    stream.flush()
                    import os
                    os.fsync(stream.fileno())
            else:
                with path.open('rb') as stream:
                    data = stream.read(1024 * 1024 + 1)
                if len(data) > 1024 * 1024:
                    raise ValueError('read exceeds one MiB')
            result = {'sha256': digest(data), 'bytes': len(data)}
            self.ledger.db.execute('BEGIN IMMEDIATE')
            self.ledger.db.execute("UPDATE effects SET status='committed',result=? WHERE task=? AND operation=?", (json.dumps(result), task_id, op_id))
            self.ledger.event(task_id, 'effect_committed', worker=worker, operation=op_id,
                              evidence_id=op_id, elapsed_ms=round((time.monotonic()-start)*1000), output_bytes=len(data))
            self.ledger.db.execute('COMMIT')
            return result
        except BaseException as exc:
            if self.ledger.db.in_transaction:
                self.ledger.db.execute('ROLLBACK')
            self.ledger.event(task_id, 'effect_unknown', worker=worker, operation=op_id, error_type=type(exc).__name__)
            raise


def run(ledger, capsule, workspace, operations, dispatch=None):
    if len(operations) > 50 or len({op['id'] for op in operations}) != len(operations):
        raise ValueError('plan must contain at most 50 unique operations')
    task_id = capsule['task_id']
    task = ledger.get(task_id)
    if task['status'] not in {'pending', 'blocked', 'active'}:
        raise ValueError('task is terminal')
    if task['worker'] not in {None, capsule['worker_id']}:
        raise PermissionError('different worker owns this task')
    attempts = task['attempts']
    if len(attempts) >= 3:
        raise ValueError('retry budget exhausted')
    plan_digest = digest(json.dumps(operations, sort_keys=True).encode())
    if attempts and attempts[-1]['plan_digest'] != plan_digest:
        raise Conflict('resume must use unchanged plan; create a successor for a new plan')
    broker = Broker(ledger, capsule, workspace)
    task = ledger.update(task_id, task['revision'], capsule['owner'], status='active',
        worker=capsule['worker_id'], blocker=None, next_action='Execute bounded plan',
        attempts=attempts+[{'plan_digest':plan_digest, 'started_at':dt.datetime.now(dt.timezone.utc).isoformat()}])
    ledger.event(task_id, 'delegation', worker=capsule['worker_id'], member='Images of Ikonn', attempt=len(task['attempts']))
    results = []
    try:
        for operation in operations:
            result = dispatch(broker, operation) if dispatch else broker.execute(operation)
            results.append({'operation':operation['id'], **result})
        # Execution is done; only the integration owner verifies acceptance and
        # marks complete. A worker cannot self-certify the objective.
        status, blocker, next_action = 'blocked', 'Acceptance review required', 'Review handback evidence'
    except (Exception, KeyboardInterrupt) as exc:
        status, blocker, next_action = 'blocked', type(exc).__name__, 'Reconcile evidence before resume'
        ledger.event(task_id, 'worker_stopped', worker=capsule['worker_id'], error_type=type(exc).__name__)
    task = ledger.update(task_id, task['revision'], capsule['owner'], status=status,
                         blocker=blocker, next_action=next_action, evidence=results)
    return {'task_id':task_id, 'worker_id':capsule['worker_id'], 'revision':task['revision'],
            'status':status, 'blocker':blocker, 'evidence':results, 'next_action':next_action}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--db', required=True)
    p.add_argument('--capsule', type=Path, required=True)
    p.add_argument('--workspace', type=Path, required=True)
    p.add_argument('--plan', type=Path, required=True)
    args = p.parse_args()
    ledger = Ledger(args.db)
    try:
        result = run(ledger, json.loads(args.capsule.read_text()), args.workspace, json.loads(args.plan.read_text()))
        print(json.dumps(result, indent=2))
        return 0 if result['blocker'] == 'Acceptance review required' else 1
    finally:
        ledger.close()


if __name__ == '__main__':
    raise SystemExit(main())
