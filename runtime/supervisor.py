"""Trusted supervisor controls; no remote listener and no automatic agents.

Signing keys and the ledger must remain outside worker-readable storage.
Leases require explicit recovery after expiry, never automatic takeover.
"""
import hashlib
import hmac
import json
import secrets
import time


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


class Supervisor:
    def __init__(self, ledger, key):
        if len(key) < 32:
            raise ValueError('supervisor key requires at least 32 random bytes')
        self.ledger, self.key = ledger, key
        ledger.db.executescript('''
        CREATE TABLE IF NOT EXISTS grants(id TEXT PRIMARY KEY, body TEXT, revoked INTEGER);
        CREATE TABLE IF NOT EXISTS leases(task TEXT PRIMARY KEY, holder TEXT, expires REAL,
            generation INTEGER, status TEXT);
        ''')

    def issue(self, task_id, worker, actions, targets, ttl=300, parent=None):
        if not 0 < ttl <= 3600 or not actions or not targets:
            raise ValueError('bounded authority and expiry required')
        task = self.ledger.get(task_id)
        body = dict(id=secrets.token_hex(16), task=task_id, worker=worker,
                    principal=task['owner'], actions=sorted(set(actions)),
                    targets=sorted(set(targets)), expires=time.time()+ttl, parent=None)
        if parent:
            ancestor = self.verify(parent, task_id)
            # Exact subsets intentionally avoid ambiguous glob containment.
            if not set(actions) <= set(ancestor['actions']) or not set(targets) <= set(ancestor['targets']):
                raise PermissionError('delegation may only attenuate authority')
            body.update(parent=ancestor['id'], expires=min(body['expires'], ancestor['expires']))
        self.ledger.db.execute('INSERT INTO grants VALUES(?,?,0)', (body['id'], canonical(body).decode()))
        self.ledger.event(task_id, 'grant_issued', worker=worker, member='TVA', operation=body['id'])
        return {'body':body,'signature':hmac.new(self.key,canonical(body),hashlib.sha256).hexdigest()}

    def verify(self, grant, task_id, worker=None):
        body = grant['body']
        expected = hmac.new(self.key,canonical(body),hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, grant['signature']):
            raise PermissionError('invalid grant signature')
        if body['task'] != task_id or (worker is not None and body['worker'] != worker):
            raise PermissionError('grant is bound to another task or worker')
        task = self.ledger.get(task_id)
        if task['status'] in {'complete','cancelled','superseded'} or body['principal'] != task['owner']:
            raise PermissionError('task authority is no longer active')
        current, visited = body, set()
        while current:
            if current['id'] in visited or current['expires'] <= time.time():
                raise PermissionError('expired or cyclic grant')
            visited.add(current['id'])
            row = self.ledger.db.execute('SELECT body,revoked FROM grants WHERE id=?', (current['id'],)).fetchone()
            if not row or row['revoked'] or json.loads(row['body']) != current:
                raise PermissionError('revoked or unknown grant')
            if not current['parent']:
                break
            row = self.ledger.db.execute('SELECT body FROM grants WHERE id=?',(current['parent'],)).fetchone()
            if not row:
                raise PermissionError('missing delegation parent')
            current = json.loads(row['body'])
        return body

    def revoke(self, grant_id):
        row = self.ledger.db.execute('SELECT body FROM grants WHERE id=?',(grant_id,)).fetchone()
        if row is None:
            raise KeyError(grant_id)
        self.ledger.db.execute('UPDATE grants SET revoked=1 WHERE id=?',(grant_id,))
        body = json.loads(row['body'])
        self.ledger.event(body['task'],'grant_revoked',member='TVA',operation=grant_id)

    def acquire(self, task_id, holder, ttl=30):
        if not 0 < ttl <= 300:
            raise ValueError('invalid lease duration')
        self.ledger.get(task_id)
        db = self.ledger.db
        db.execute('BEGIN IMMEDIATE')
        try:
            prior = db.execute('SELECT * FROM leases WHERE task=?',(task_id,)).fetchone()
            if prior and prior['status'] != 'released':
                raise PermissionError('lease held or expired; reconcile before takeover')
            generation = prior['generation']+1 if prior else 1
            db.execute('INSERT OR REPLACE INTO leases VALUES(?,?,?,?,?)',
                       (task_id,holder,time.time()+ttl,generation,'active'))
            self.ledger.event(task_id,'lease_acquired',worker=holder,revision=generation)
            db.execute('COMMIT')
            return generation
        except BaseException:
            db.execute('ROLLBACK'); raise

    def renew(self, task_id, holder, generation, ttl=30):
        if not 0 < ttl <= 300:
            raise ValueError('invalid lease duration')
        changed = self.ledger.db.execute('''UPDATE leases SET expires=? WHERE task=? AND holder=?
            AND generation=? AND status='active' AND expires>?''',
            (time.time()+ttl,task_id,holder,generation,time.time())).rowcount
        if changed != 1:
            raise PermissionError('stale lease fence')

    def release(self, task_id, holder, generation):
        changed = self.ledger.db.execute('''UPDATE leases SET status='released' WHERE task=?
            AND holder=? AND generation=? AND status='active' ''', (task_id,holder,generation)).rowcount
        if changed != 1:
            raise PermissionError('stale lease release')

    def dispatch(self, grant, broker, operation):
        try:
            body = self.verify(grant, broker.capsule['task_id'], broker.capsule['worker_id'])
            if operation['action'] not in body['actions'] or operation['target'] not in body['targets']:
                raise PermissionError('operation exceeds signed grant')
        except PermissionError:
            self.ledger.event(broker.capsule['task_id'],'signed_guard_denied',
                worker=broker.capsule['worker_id'],member='TVA',operation=operation['id'],decision='deny')
            raise
        return broker.execute(operation)

    def run_plan(self, grant, capsule, workspace, operations):
        from bounded_worker import run
        task_id, worker = capsule['task_id'], capsule['worker_id']
        self.verify(grant,task_id,worker)
        generation = self.acquire(task_id,worker)
        def dispatch(broker,operation):
            self.renew(task_id,worker,generation)
            return self.dispatch(grant,broker,operation)
        try:
            return run(self.ledger,capsule,workspace,operations,dispatch=dispatch)
        finally:
            self.release(task_id,worker,generation)


def require_containment(probe):
    """Only a trusted, freshly executed probe is evidence, never worker claims."""
    required = ('workspace_write','outside_write_denied','outside_read_denied',
                'network_denied','process_tree_termination')
    if any(probe.get(key) is not True for key in required):
        raise PermissionError('runtime containment not verified')
    timestamp = probe.get('observed_at', 0)
    if not 0 <= time.time()-timestamp <= 60:
        raise PermissionError('runtime probe stale')


def main():
    import argparse
    from pathlib import Path
    from ledger import Ledger
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db',required=True)
    parser.add_argument('--key',type=Path,required=True,help='Trusted supervisor-owned 32-byte key file')
    parser.add_argument('--grant',type=Path,required=True)
    parser.add_argument('--capsule',type=Path,required=True)
    parser.add_argument('--workspace',type=Path,required=True)
    parser.add_argument('--plan',type=Path,required=True)
    args=parser.parse_args()
    if args.key.resolve().is_relative_to(args.workspace.resolve()):
        raise ValueError('signing key cannot reside in worker workspace')
    ledger=Ledger(args.db)
    try:
        supervisor=Supervisor(ledger,args.key.read_bytes())
        result=supervisor.run_plan(json.loads(args.grant.read_text()),json.loads(args.capsule.read_text()),
                                   args.workspace,json.loads(args.plan.read_text()))
        print(json.dumps(result,indent=2))
        return 0 if result['blocker']=='Acceptance review required' else 1
    finally:
        ledger.close()


if __name__=='__main__':
    raise SystemExit(main())
