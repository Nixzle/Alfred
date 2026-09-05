# Runtime foundations: local pilot

This document records the initial pilot. For current implemented capabilities and
the separate offline Windows backend, consult [release status](RELEASE_STATUS.md).

This implements the first local, dependency-free slice of roadmap issues 1–4.
It is not a claim that every Codex, ChatGPT or Discord action is contained.

## Durable task truth

`ledger.py` maintains a SQLite task database outside worker workspaces. Tasks have
objectives, owners, integration owners, worker IDs, dependencies, acceptance
criteria, evidence, blockers, next actions and attempt histories. Each change
requires the current revision and owner. Transactions reject stale updates.
Historical revisions remain available in the history table; terminal records
cannot be revived. Create a successor rather than replaying a completed task.
The owner is a trusted local supervisor identity, not an authenticated remote user.

```sh
python runtime/ledger.py --db .sanctum/control.sqlite create --id example --objective "Write a report" --owner prime --acceptance "Owner reviews report"
python runtime/ledger.py --db .sanctum/control.sqlite snapshot
python runtime/ledger.py --db .sanctum/control.sqlite trace --id example
```

Updates use `update --id example --revision 1 --actor prime --changes changes.json`.
The JSON object can change status, worker, evidence, blocker, next_action, attempts
or supersedes. Completing a task requires evidence and finished dependencies.
Evidence presence is checked; truth of acceptance remains the integration owner's
responsibility. Task bodies are private project data; telemetry minimization does
not imply automatic redaction of intentionally stored task truth.

## Declarative worker and TVA boundary

The supervisor creates an empty, separate workspace and a trusted capsule:

```json
{
  "task_id": "example",
  "owner": "prime",
  "worker_id": "image-example",
  "expires_at": "2000-01-01T00:00:00+00:00",
  "allowed_actions": ["read", "create"],
  "allowed_targets": ["report.txt"],
  "approval_required_actions": []
}
```

The deliberately expired example must be replaced by the supervisor with a short
future expiry before use. A plan is a list of operations:

```json
[{"id":"report-v1","action":"create","target":"report.txt","text":"Report content"}]
```

```sh
python runtime/bounded_worker.py --db .sanctum/control.sqlite --capsule capsule.json --workspace worker-example --plan plan.json
```

Supported operations are bounded file reads (digest evidence only) and exclusive
file creation, each limited to one MiB. No arbitrary code, subprocess, network,
dependency installation, overwrite or deletion operation is exposed. Unsupported
actions are denied even if a capsule or plan requests them. Required approvals
stop dispatch; a plan's `approved` field is not authority. An approval service is
not implemented. A supervisor must create a new approved successor capsule/task.

Workspace resolution rejects traversal, absolute paths, Windows alternate streams,
symbolic links, detected junctions, hard links and protected metadata paths.
Authority and expiry are checked before dispatch. Worker/workspace/capsule bindings
cannot change on resume; registered workspaces cannot overlap. The database must
be outside the worker workspace. These controls are **ENFORCED for the built-in
broker operations** and **CHECKED by the tests**.

The supervisor is trusted. Same-account processes can still tamper with the
database, code or filesystem between checks. This is not an OS sandbox and must
not be used to execute hostile Python, shell scripts or unrestricted model tools.
Network is absent from the adapter, not blocked system-wide. No production surface
is automatically wired into this boundary by importing Sanctum doctrine.

## Restart, evidence and stopping

Each operation has a stable ID and payload fingerprint. Durable intent is written
before dispatch. A committed operation returns its previous evidence without
writing again. After interruption, an exact expected create postcondition can be
reconciled; missing, partial or conflicting output stops for owner review. It does
not blindly repeat an uncertain operation. A plan change requires a successor.

Plans have at most 50 unique operations and three attempts. Any unresolved error
stops at the first gap; there is no automatic retry loop. Ctrl+C records a stopped
worker when Python can handle it; hard termination leaves durable intent for the
next session. No child processes or background workers are launched. File I/O on
stalled network filesystems has no hard timeout, so use local workspaces. One
active supervisor per workspace is required; this is not a distributed scheduler.

Structured handbacks include task/worker IDs, revision, results, blocker and next
action. Successful execution waits for acceptance review instead of granting the
worker authority to mark its own task complete.

Watcher stores ordered intent/guard/commit/reconcile/failure/delegation events in
SQLite, linked by task, worker and operation IDs. Payloads, file contents and raw
exception messages are excluded. Cost is recorded only when supplied by a trusted
adapter; missing cost is unknown, not zero. Legacy `sanctum.py trace` remains a raw
manual diagnostic tool and should not receive secrets or worker payloads.

## Evidence and remaining issue scope

- Issue 1: local durable task state and stale-writer detection implemented.
- Issue 2: declarative isolated execution, checkpoints, conservative recovery and
  handbacks implemented. General model-worker launch, OS containment, leases and
  hard timeout/process-tree termination remain outstanding.
- Issue 3: broker execution telemetry implemented. External-tool/model usage and
  production adapter instrumentation remain outstanding.
- Issue 4: broker effects have mandatory checks. Authenticated cross-surface grants,
  OS-level filesystem/network containment and production tool mediation remain
  outstanding. Keep the broad issue open until those boundaries are demonstrated.

Run `python -m unittest discover -s runtime/tests -p 'test_*.py'` and
`python runtime/sanctum.py lint` locally. Regression cases cover fresh-session
recovery, stale writes, dependency gates, denied dispatch, expiry, approval spoofing,
unknown outcomes, repeat suppression, changed plans, cross-worker separation,
workspace rebinding, hard links and telemetry minimization.

Rollback: stop invoking these two new entrypoints. Existing routing commands and
production integrations are unchanged. Preserve the database as private evidence;
copy/backup it only with SQLite's backup API or after closing all connections.

Provenance: implements the existing four foundation issues against main commit
22312b01ecda90345aebe710ed22b08f9ec85385. No new member or voice project is introduced.

## Supervisor hardening follow-up

`supervisor.py` adds HMAC-signed, task/worker-bound, expiring grants, exact-subset
attenuation, parent revocation, durable single-host leases and fencing generations.
`Supervisor.run_plan` acquires a lease and enforces the signed grant at each broker
dispatch. Its CLI accepts supervisor-owned key/grant/capsule files. Grant issuance
is an explicit trusted Python API (`Supervisor.issue`), not an unauthenticated
remote endpoint. Signing keys are not passed to workers. Expired leases require
supervisor reconciliation; no automatic takeover or background scheduler exists.

`process_control.py` provides bounded lifecycle control for trusted adapters. On
Windows it assigns the gated launcher to a kill-on-close Job Object before work
starts. Closing the job cleans up descendants on timeout or revocation. The local
regression starts a real child process and verifies its delayed write never occurs
after timeout. This is lifecycle control, not filesystem or network containment.

A real Codex sandbox probe on this host allowed workspace writes and denied an
outside write. HTTPS failed. However, an outside synthetic control file remained
readable with both a minimal profile and an explicit deny-read rule. Consequently
unrestricted agent dispatch is NOT activated. `require_containment` rejects missing,
failed or stale trusted probe evidence. It must not consume worker-supplied claims.
Docker is unavailable and WSL is not installed. No admin policy changes, package
installations, real secret reads or paid model tests were performed.

These additions supersede the earlier missing local grant, lease and process-tree
cleanup entries above. Cross-host authentication, distributed scheduling and
production model-agent containment are still unverified; the installed sandbox's
failed read-boundary probe is the concrete blocker. Do not close the broad TVA or
Ikonn issue on the strength of successful lifecycle tests.

## Release acceptance

`python runtime/acceptance.py --out .sanctum/health-acceptance` runs a complete
health-report task: fresh doctrine lint, signed grant, leased worker dispatch,
exclusive artifact creation, content verification, owner acceptance, grant
revocation and recovery from a new ledger session. Use a new output directory for
each run; existing evidence is never overwritten. This validates issue 1's local
fresh-session task-truth acceptance. It does not validate unrestricted model agents.

The release was checked locally with 35 tests, doctrine lint, route/guard smoke
checks and the complete task above. Hosted CI is explicitly skipped to respect the
account's Actions budget; local evidence is not represented as a hosted CI run.
Issues 2–4 retain their broader integration/containment scope.
