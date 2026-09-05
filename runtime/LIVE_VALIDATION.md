# Local validation to Presence

The concrete event source is this project's actual local release validation process.
Its completion feeds Presence in the same invocation. This is an opt-in synchronous
integration, not an installed watcher or automatic connection to other projects.

```text
python runtime/validate.py --out PRIVATE_NEW_DIRECTORY --attention-db PRIVATE_ATTENTION.db --project sanctum
```

The existing tests, lint, acceptance and diff checks run locally. Their receipt also
records per-check elapsed seconds. The optional hook writes `attention.json` beside
the receipt and stores normalized metadata in the private SQLite ledger. A passing
receipt becomes a result; a failed check becomes a blocker. Owner policy allows local
attention only and zero investigations. `notify=true` recommends surfacing the event
to the caller; it does not send a notification or invoke a model. The hook's failure
raises an error rather than silently claiming a completed integration.

Replay the same receipt in a fresh process to check persisted duplicate suppression:

```text
python -m runtime.release_event --receipt PRIVATE_NEW_DIRECTORY/receipt.json --db PRIVATE_ATTENTION.db --project sanctum
```

Canonical receipt content determines event identity; its original completion time
survives replay. Stale or future receipts are suppressed rather than made fresh. The
deduplication horizon is one hour, matching event expiry. New validation runs have new
completion times and are distinct events. All processes must use the same ledger and
project ID. Compact state expires on subsequent accepted events; this is not a durable
notification outbox, and concurrent exactly-once external delivery is not claimed.

The adapter accepts only complete, unique, consistent check summaries. Inputs are
trusted local owner files; their digest is identity, not signature authentication.
The adapter does not execute receipt content, read referenced file paths, or import
raw logs into Presence. Keep the ledger and live evidence outside the canonical repo.
No network request, hosted Action, paid evaluator or background service is introduced.
