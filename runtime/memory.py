"""Governed durable-memory candidates with explicit promotion and supersession."""
import hashlib
import json
from pathlib import Path
import sqlite3
import time

STATES = {"candidate", "promoted", "rejected", "superseded"}


def _hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


class Memory:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS entries(
          id TEXT PRIMARY KEY, scope TEXT, kind TEXT, text TEXT, source TEXT,
          observed REAL, effective REAL, state TEXT, confidence REAL,
          supersedes TEXT, digest TEXT, revision INTEGER);
        CREATE TABLE IF NOT EXISTS history(
          id TEXT, revision INTEGER, snapshot TEXT, PRIMARY KEY(id,revision));
        """)
        self.db.commit()

    def close(self):
        self.db.close()

    def add_candidate(self, id, scope, kind, text, source, observed=None, effective=None, confidence=1.0):
        values = (id, scope, kind, text, source)
        if not all(isinstance(value, str) and value and len(value) <= 4096 for value in values):
            raise ValueError("bounded memory fields required")
        if not 0 <= float(confidence) <= 1:
            raise ValueError("confidence out of range")
        observed = time.time() if observed is None else float(observed)
        effective = observed if effective is None else float(effective)
        body = dict(
            id=id, scope=scope, kind=kind, text=text, source=source,
            observed=observed, effective=effective, state="candidate",
            confidence=float(confidence), supersedes=None, digest=_hash(text), revision=1,
        )
        with self.db:
            self.db.execute("INSERT INTO entries VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", tuple(body.values()))
            self.db.execute("INSERT INTO history VALUES(?,?,?)", (id, 1, json.dumps(body, sort_keys=True)))
        return body

    def get(self, id):
        row = self.db.execute("SELECT * FROM entries WHERE id=?", (id,)).fetchone()
        if row is None:
            raise KeyError(id)
        return dict(row)

    def decide(self, id, revision, decision, *, supersedes=None):
        if decision not in {"promoted", "rejected"}:
            raise ValueError("invalid decision")
        with self.db:
            row = self.get(id)
            if row["revision"] != revision:
                raise ValueError("stale memory revision")
            if row["state"] != "candidate":
                raise ValueError("only candidates can be decided")
            if supersedes:
                old = self.get(supersedes)
                if old["state"] != "promoted":
                    raise ValueError("superseded entry must be promoted")
                if old["scope"] != row["scope"] or old["kind"] != row["kind"]:
                    raise ValueError("supersession scope/kind mismatch")
                old["state"] = "superseded"
                old["revision"] += 1
                self.db.execute(
                    "UPDATE entries SET state=?,revision=? WHERE id=?",
                    ("superseded", old["revision"], supersedes),
                )
                self.db.execute(
                    "INSERT INTO history VALUES(?,?,?)",
                    (supersedes, old["revision"], json.dumps(old, sort_keys=True)),
                )
            row["state"] = decision
            row["supersedes"] = supersedes
            row["revision"] += 1
            self.db.execute(
                "UPDATE entries SET state=?,supersedes=?,revision=? WHERE id=?",
                (decision, supersedes, row["revision"], id),
            )
            self.db.execute(
                "INSERT INTO history VALUES(?,?,?)",
                (id, row["revision"], json.dumps(row, sort_keys=True)),
            )
        return row

    def current(self, scope=None):
        query = "SELECT * FROM entries WHERE state='promoted'"
        args = []
        if scope is not None:
            query += " AND scope=?"
            args.append(scope)
        query += " ORDER BY effective,id"
        return [dict(row) for row in self.db.execute(query, args)]

    def export(self):
        entries = [dict(row) for row in self.db.execute("SELECT * FROM entries ORDER BY id")]
        history = [dict(row) for row in self.db.execute("SELECT * FROM history ORDER BY id,revision")]
        payload = {"schema_version": 1, "entries": entries, "history": history}
        payload["digest"] = _hash(json.dumps(payload, sort_keys=True, separators=(",", ":")))
        return payload
