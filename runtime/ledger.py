"""Local transactional task truth and metadata-only Watcher evidence.

The database belongs to the trusted orchestrator, never to worker workspaces.
SQLite transactions serialize changes; revisions reject stale writers.
"""
import argparse
import datetime as dt
import json
import sqlite3
from pathlib import Path


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


class Conflict(ValueError):
    pass


class Ledger:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path, timeout=5, isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.executescript('''
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS tasks(id TEXT PRIMARY KEY, revision INTEGER, body TEXT);
        CREATE TABLE IF NOT EXISTS history(task TEXT, revision INTEGER, body TEXT,
            PRIMARY KEY(task, revision));
        CREATE TABLE IF NOT EXISTS events(sequence INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT, task TEXT, worker TEXT, member TEXT, operation TEXT,
            event TEXT, data TEXT);
        CREATE TABLE IF NOT EXISTS effects(task TEXT, operation TEXT, fingerprint TEXT,
            status TEXT, result TEXT, PRIMARY KEY(task, operation));
        CREATE TABLE IF NOT EXISTS workers(task TEXT PRIMARY KEY, worker TEXT UNIQUE,
            workspace TEXT UNIQUE, capsule TEXT);
        ''')

    def close(self):
        self.db.close()

    def event(self, task, event, *, worker=None, member='Ultron Prime', operation=None, **data):
        # Allowlist metadata: tool payloads, exception messages, prompts and credentials
        # are never copied into telemetry. Evidence IDs are internal references.
        allowed = {'revision', 'attempt', 'decision', 'error_type', 'elapsed_ms',
                   'input_bytes', 'output_bytes', 'cost', 'currency', 'evidence_id', 'status'}
        clean = {k: v for k, v in data.items() if k in allowed}
        self.db.execute('INSERT INTO events VALUES(NULL,?,?,?,?,?,?,?)',
                        (now(), task, worker, member, operation, event, json.dumps(clean)))

    def create(self, task_id, objective, owner, acceptance, dependencies=()):
        if not all((task_id, objective, owner, acceptance)):
            raise ValueError('task ID, objective, owner and acceptance are required')
        body = dict(id=task_id, objective=objective, owner=owner, worker=None,
                    integration_owner=owner, dependencies=list(dependencies), status='pending',
                    acceptance=acceptance, evidence=[], blocker=None, next_action='Start task',
                    attempts=[], revision=1, observed_at=now(), supersedes=None)
        self.db.execute('BEGIN IMMEDIATE')
        try:
            for dependency in dependencies:
                self.get(dependency)
            self.db.execute('INSERT INTO tasks VALUES(?,?,?)', (task_id, 1, json.dumps(body)))
            self.db.execute('INSERT INTO history VALUES(?,?,?)', (task_id, 1, json.dumps(body)))
            self.event(task_id, 'task_created', revision=1)
            self.db.execute('COMMIT')
        except BaseException:
            self.db.execute('ROLLBACK')
            raise
        return body

    def get(self, task_id):
        row = self.db.execute('SELECT body FROM tasks WHERE id=?', (task_id,)).fetchone()
        if row is None:
            raise KeyError(task_id)
        return json.loads(row['body'])

    def update(self, task_id, revision, actor, **changes):
        permitted = {'status', 'worker', 'evidence', 'blocker', 'next_action', 'attempts', 'supersedes'}
        if set(changes) - permitted:
            raise ValueError('unsupported task mutation')
        self.db.execute('BEGIN IMMEDIATE')
        try:
            body = self.get(task_id)
            if body['revision'] != revision:
                raise Conflict('stale task revision')
            if actor != body['owner']:
                raise PermissionError('only task owner may update task truth')
            if body['status'] in {'complete', 'cancelled', 'superseded'}:
                raise ValueError('terminal task cannot be resumed; create a successor')
            body.update(changes)
            if body['status'] not in {'pending', 'active', 'blocked', 'complete', 'cancelled', 'superseded'}:
                raise ValueError('invalid task status')
            if body['status'] in {'active', 'complete'}:
                if any(self.get(dep)['status'] != 'complete' for dep in body['dependencies']):
                    raise ValueError('unfinished dependency')
            if body['status'] == 'complete' and not body['evidence']:
                raise ValueError('completion requires evidence')
            if body['status'] == 'blocked' and not body['blocker']:
                raise ValueError('blocked task requires blocker')
            body.update(revision=revision+1, observed_at=now())
            encoded = json.dumps(body)
            self.db.execute('UPDATE tasks SET revision=?,body=? WHERE id=?', (revision+1, encoded, task_id))
            self.db.execute('INSERT INTO history VALUES(?,?,?)', (task_id, revision+1, encoded))
            self.event(task_id, 'task_updated', revision=revision+1, status=body['status'])
            self.db.execute('COMMIT')
            return body
        except BaseException:
            self.db.execute('ROLLBACK')
            raise

    def snapshot(self):
        return [json.loads(row['body']) for row in self.db.execute('SELECT body FROM tasks ORDER BY id')]

    def trace(self, task_id):
        return [dict(row) | {'data': json.loads(row['data'])} for row in
                self.db.execute('SELECT * FROM events WHERE task=? ORDER BY sequence', (task_id,))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', default='.sanctum/control.sqlite')
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('create')
    for key in ('id', 'objective', 'owner', 'acceptance'):
        p.add_argument('--'+key, required=True)
    p.add_argument('--dependency', action='append', default=[])
    p = sub.add_parser('update')
    p.add_argument('--id', required=True)
    p.add_argument('--revision', type=int, required=True)
    p.add_argument('--actor', required=True)
    p.add_argument('--changes', type=Path, required=True, help='JSON object; local task data')
    sub.add_parser('snapshot')
    p = sub.add_parser('trace'); p.add_argument('--id', required=True)
    args = parser.parse_args()
    ledger = Ledger(args.db)
    try:
        if args.command == 'create':
            result = ledger.create(args.id, args.objective, args.owner, [args.acceptance], args.dependency)
        elif args.command == 'update':
            result = ledger.update(args.id, args.revision, args.actor,
                                   **json.loads(args.changes.read_text(encoding='utf-8')))
        elif args.command == 'trace':
            result = ledger.trace(args.id)
        else:
            result = ledger.snapshot()
        print(json.dumps(result, indent=2))
    finally:
        ledger.close()


if __name__ == '__main__':
    main()
