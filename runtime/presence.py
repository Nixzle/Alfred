"""Replay trusted event metadata into a private attention ledger; never execute effects."""
import argparse
import hashlib
import json
from pathlib import Path
import sqlite3
import time

KNOWN_KINDS = {
    'routine', 'change', 'blocker', 'result', 'critical',
    'drift', 'opportunity', 'dependency_risk', 'stale_assumption',
    'coverage_gap', 'coordination_risk', 'efficiency_waste',
    'completion_seam', 'user_correction', 'security_anomaly',
}
WEAK_SIGNAL_KINDS = {
    'drift', 'opportunity', 'dependency_risk', 'stale_assumption',
    'coverage_gap', 'coordination_risk', 'efficiency_waste',
    'completion_seam', 'user_correction', 'security_anomaly',
}
MATERIAL_ACTIVE_KINDS = {
    'blocker', 'result', 'critical', 'dependency_risk',
    'coordination_risk', 'security_anomaly', 'completion_seam',
}
OPPORTUNITY_KINDS = {
    'opportunity', 'efficiency_waste', 'coverage_gap',
    'stale_assumption', 'user_correction',
}


def _bounded_text(value, name, max_len=128, allow_empty=False):
    if not isinstance(value, str) or len(value) > max_len or (not allow_empty and not value):
        raise ValueError(f'bounded {name} required')
    return value


def _bounded_number(value, name, low=0.0, high=1.0, default=None):
    if value is None and default is not None:
        return default
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f'numeric {name} required')
    value = float(value)
    if not low <= value <= high:
        raise ValueError(f'{name} out of range')
    return value


class Attention:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute('PRAGMA journal_mode=WAL')
        self.db.execute(
            'CREATE TABLE IF NOT EXISTS attention '
            '(key TEXT PRIMARY KEY, seen REAL, expires REAL, fingerprint TEXT, decision TEXT)'
        )
        self.db.execute('CREATE TABLE IF NOT EXISTS investigations (at REAL)')
        self.db.execute(
            'CREATE TABLE IF NOT EXISTS signals '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, project TEXT, incident TEXT, '
            'kind TEXT, family TEXT, observed REAL, confidence REAL, impact REAL, fingerprint TEXT)'
        )
        self.db.execute('CREATE INDEX IF NOT EXISTS idx_signals_project_time ON signals(project, observed)')
        self.db.execute('CREATE INDEX IF NOT EXISTS idx_signals_family_time ON signals(family, observed)')
        self.db.commit()

    def close(self):
        self.db.close()

    def _normalize(self, event):
        for key in ('source', 'project', 'incident', 'kind'):
            _bounded_text(event.get(key), f'event identity: {key}')
        if event['kind'] not in KNOWN_KINDS:
            raise ValueError('unknown event kind')
        observed = event.get('observed_at')
        if isinstance(observed, bool) or not isinstance(observed, (int, float)):
            raise ValueError('numeric observation timestamp required')
        revision = _bounded_text(event.get('revision', ''), 'revision', allow_empty=True)
        family = _bounded_text(event.get('family', event['kind']), 'signal family')
        confidence = _bounded_number(event.get('confidence'), 'confidence', default=1.0)
        impact = _bounded_number(event.get('impact'), 'impact', default=0.5)
        return {
            'source': event['source'],
            'project': event['project'],
            'incident': event['incident'],
            'kind': event['kind'],
            'observed_at': float(observed),
            'revision': revision,
            'family': family,
            'confidence': confidence,
            'impact': impact,
        }

    def _correlation(self, event, policy, now):
        window = max(1.0, min(86400.0, float(policy.get('correlation_window_seconds', 1800))))
        threshold = max(2, min(20, int(policy.get('correlation_threshold', 3))))
        since = now - window
        same_family = self.db.execute(
            'SELECT COUNT(DISTINCT incident), COUNT(DISTINCT source) FROM signals '
            'WHERE project=? AND family=? AND observed>=?',
            (event['project'], event['family'], since),
        ).fetchone()
        corrections = self.db.execute(
            "SELECT COUNT(*) FROM signals WHERE project=? AND kind='user_correction' AND observed>=?",
            (event['project'], since),
        ).fetchone()[0]
        correlated = (same_family[0] + 1) >= threshold or (same_family[1] + 1) >= threshold
        repeated_corrections = event['kind'] == 'user_correction' and (corrections + 1) >= threshold
        return {
            'window_seconds': window,
            'family_incidents': same_family[0] + 1,
            'family_sources': same_family[1] + 1,
            'repeated_user_corrections': repeated_corrections,
            'clustered': correlated or repeated_corrections,
        }

    def evaluate(self, event, policy, now=None):
        """Policy comes from the owner, never from event text or event authority fields.

        Event metadata is normalized by the source adapter. Raw bodies, instructions,
        credentials and arbitrary extra fields are deliberately not stored.
        """
        now = time.time() if now is None else now
        event = self._normalize(event)
        key = json.dumps([event[k] for k in ('source', 'project', 'incident')])
        fingerprint = hashlib.sha256(
            json.dumps(
                [event['kind'], event['revision'], event['family'], event['confidence'], event['impact'], policy],
                sort_keys=True,
            ).encode()
        ).hexdigest()
        result = dict(
            state='SUPPRESSED', initiative='OBSERVE_ONLY', notify=False,
            execute=False, investigate=False, reason='stale or future event',
            signal_family=event['family'], clustered=False, salience=0.0,
        )
        ttl = min(3600, max(1, float(policy.get('ttl_seconds', 300))))
        if not 0 <= now - event['observed_at'] < ttl:
            return result

        with self.db:
            self.db.execute('DELETE FROM attention WHERE expires<=?', (now,))
            self.db.execute('DELETE FROM investigations WHERE at<=?', (now - 3600,))
            history_ttl = max(ttl, min(86400, float(policy.get('signal_history_seconds', 3600))))
            self.db.execute('DELETE FROM signals WHERE observed<=?', (now - history_ttl,))

            previous = self.db.execute(
                'SELECT fingerprint,decision FROM attention WHERE key=?', (key,)
            ).fetchone()
            correlation = self._correlation(event, policy, now)
            result.update(clustered=correlation['clustered'], correlation=correlation)

            active = event['project'] == policy.get('active_project')
            watched = key in policy.get('watched_incidents', [])
            critical = event['kind'] == 'critical' and event['source'] in policy.get('critical_sources', [])
            quiet = policy.get('mode', 'assistant') == 'quiet'

            base_salience = event['confidence'] * event['impact']
            salience = min(
                1.0,
                base_salience
                + (0.2 if active else 0.0)
                + (0.2 if watched else 0.0)
                + (0.25 if critical else 0.0)
                + (0.2 if correlation['clustered'] else 0.0),
            )
            result['salience'] = round(salience, 3)

            material = (
                (active and event['kind'] in MATERIAL_ACTIVE_KINDS)
                or watched
                or critical
                or correlation['clustered']
            )
            opportunity = active and event['kind'] in OPPORTUNITY_KINDS

            if material:
                result.update(
                    state='NOW', initiative='INTERRUPT_NOW', notify=True,
                    reason='material active or correlated signal',
                )
            elif opportunity:
                result.update(
                    state='NOW', initiative='INVESTIGATE_AUTONOMOUSLY',
                    notify=False, reason='high-leverage opportunity signal',
                )
            elif event['kind'] in WEAK_SIGNAL_KINDS:
                result.update(
                    state='BACKGROUND', initiative='RETAIN_FOR_BRIEFING',
                    reason='weak signal retained for correlation',
                )
            else:
                result.update(
                    state='BACKGROUND', initiative='RETAIN_FOR_BRIEFING',
                    reason='retain for briefing',
                )

            if quiet and not (watched or critical):
                result.update(
                    notify=False,
                    initiative='RETAIN_FOR_BRIEFING' if not opportunity else 'INVESTIGATE_AUTONOMOUSLY',
                    reason='quiet mode',
                )

            if previous:
                old = json.loads(previous[1])
                if previous[0] == fingerprint and old['state'] == result['state']:
                    result.update(
                        notify=False, investigate=False,
                        initiative='OBSERVE_ONLY', reason='duplicate event',
                    )

            count = self.db.execute('SELECT COUNT(*) FROM investigations').fetchone()[0]
            budget = max(0, min(10, int(policy.get('investigations_per_hour', 0))))
            investigation_kind = material or opportunity
            if (
                investigation_kind
                and not previous
                and count < budget
                and event['source'] in policy.get('investigation_sources', [])
            ):
                result['investigate'] = True
                if result['initiative'] == 'RETAIN_FOR_BRIEFING':
                    result['initiative'] = 'INVESTIGATE_AUTONOMOUSLY'
                self.db.execute('INSERT INTO investigations VALUES (?)', (now,))

            self.db.execute(
                'INSERT INTO signals(source,project,incident,kind,family,observed,confidence,impact,fingerprint) '
                'VALUES (?,?,?,?,?,?,?,?,?)',
                (
                    event['source'], event['project'], event['incident'], event['kind'], event['family'],
                    event['observed_at'], event['confidence'], event['impact'], fingerprint,
                ),
            )
            self.db.execute(
                'INSERT OR REPLACE INTO attention VALUES (?,?,?,?,?)',
                (key, now, now + ttl, fingerprint, json.dumps(result)),
            )
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', required=True)
    parser.add_argument('--event', type=Path, required=True)
    parser.add_argument('--policy', type=Path, required=True)
    args = parser.parse_args()
    ledger = Attention(args.db)
    try:
        print(json.dumps(
            ledger.evaluate(json.loads(args.event.read_text()), json.loads(args.policy.read_text())),
            indent=2,
        ))
    finally:
        ledger.close()


if __name__ == '__main__':
    main()
