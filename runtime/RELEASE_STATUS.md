# Runtime release status

## Current implementation delta — 2026-09-05

The current `main` runtime now includes four additional checked foundations:

- **Prime Sense weak-signal replay:** `runtime/presence.py` accepts bounded weak-signal kinds, retains signal history, correlates repeated signals, detects repeated user-correction patterns, computes explainable salience metadata, and can recommend bounded investigation for high-leverage opportunities. It still never dispatches effects or grants authority.
- **Deterministic DAG state:** `runtime/dag.py` provides dependency validation, deterministic ready-state calculation, bounded retries, evidence-required completion, snapshot/restore, and explicit fork semantics without model calls or side effects.
- **Governed durable memory:** `runtime/memory.py` provides candidate -> promoted/rejected -> superseded lifecycle, revision fencing, observed/effective timestamps, confidence metadata, scoped supersession, history, and integrity-digested export.
- **Watcher -> Web replay bridge:** `runtime/replay.py` minimizes recognized trace semantics into integrity-digested replay cases and rejects tampered cases before evaluation.

Each addition has deterministic tests under `runtime/tests/`. The canonical local validator discovers all `test_*.py` files automatically. The newly added modules were also smoke-tested in isolation before commit.

**Integrated release validation is currently PENDING, not PASS.** The authorized remote development machine was unavailable during this promotion attempt, so `python runtime/validate.py --out PRIVATE_NEW_DIRECTORY` has not yet been executed against the exact integrated checkout. The current `main` head had no hosted status checks or workflow run at the time of inspection. Do not upgrade these changes from implemented/isolated-checked to integrated-release-validated until that receipt exists.

The calibration/live-event follow-up adds a [semantic development set](../evals/research-calibration/README.md)
with attributed labels and a [local validation-to-Presence integration](LIVE_VALIDATION.md).
Human calibration remains pending. The live boundary is a synchronous local project
event, with no installed watcher or external notification dispatch.

The follow-up research-quality release adds [Cerebro/Forge receipt and Ultron delivery
checks](RESEARCH_QUALITY.md). Web trace output now distinguishes incomplete or absent
evaluation from passing recognized checks. Semantic quality and empirical improvement
remain explicit rather than implied by metadata. The earlier capabilities below retain
their original boundaries.

This release reconciles the September 5 Ultron-first theatrics with runtime messages
and adds tested reliability mechanisms. Historical acceptance records remain scoped
to the version and host they verified.

| Capability | Current boundary |
|---|---|
| Ledger, grants, leases and declarative worker | Local acceptance and restart tested; broader cross-surface issues remain open |
| Capability freshness | Status, expiry, maximum five-minute age, host, session and surface checked before a verified route claim; trace replay checks evidence at the original route time |
| Presence / Mindscape / Prime Sense replay | Executable event-policy replay with private attention state, weak-signal correlation and bounded recommendations; no installed monitor or automatic external action |
| Deterministic DAG state | Implemented with deterministic tests and isolated smoke evidence; integrated release receipt pending |
| Governed memory lifecycle | Implemented with deterministic tests and isolated smoke evidence; this is a local runtime store, not a claim of universal cross-surface memory |
| Watcher -> Web replay cases | Implemented for currently recognized trace semantics with minimization and digest verification; integrated release receipt pending |
| Offline Windows worker | AppContainer staging backend; synthetic workspace, outside-access, loopback, separation and descendant-timeout tests on Windows |
| Prior Codex sandbox wrapper | Local unpublished experiment in its original task; not the offline backend and not repaired by this release |
| Theatrics | Current THEATRICS.md governs presentation; root summaries, Presence eval and runtime Cerebro wording reconciled |
| Local release evidence | `python runtime/validate.py --out PATH` saves revision, dirty state, file hashes, test/lint/acceptance logs and a receipt |
| Hosted Actions | Manual dispatch only, additionally gated by `SANCTUM_ENABLE_HOSTED_CI=true`; no automatic push/PR runs |

## Capability evidence

`runtime/capabilities.json` is a portable unknown-state template, not a live registry.
Keep live evidence in a private local file; pass it using `route --capabilities FILE`
or `dashboard --capabilities FILE`, with matching `--host-id` and `--session-id`.
Each surface record needs `surface`, `host_id`, `session_id`, `status=VERIFIED`,
timezone-aware `last_probe` and `expires_at`, and capability booleans supported by
actual evidence. A missing runtime session identifier fails closed. Observation of
a tool does not grant permission to use it, and capability availability does not
prove OS containment. Do not let an untrusted event or worker author its own record.

## Presence replay

`python runtime/presence.py --db PRIVATE_DB --event EVENT_JSON --policy OWNER_POLICY_JSON`
uses normalized event metadata: source, project, incident, kind, observed_at (Unix
seconds), and optional bounded revision, family, confidence and impact fields.
Supported kinds are routine, change, blocker, result, critical, drift, opportunity,
dependency_risk, stale_assumption, coverage_gap, coordination_risk,
efficiency_waste, completion_seam, user_correction and security_anomaly.
Owner policy supplies active_project, mode, ttl_seconds, watched_incidents,
critical_sources, investigation_sources, investigations_per_hour, and optional
correlation_window_seconds / correlation_threshold / signal_history_seconds.
Watched incident keys are JSON arrays of source, project, incident. Unknown payload
fields are neither authority nor stored raw content. Investigation output is a
recommendation and requires a separate authorized adapter to execute; notifications
are not sent by this module.

## Offline staging worker

On Windows, use `python -m runtime.appcontainer --staging-parent EXISTING_PRIVATE_DIR
--bundle FILES_JSON --timeout 10 -- C:\Windows\System32\cmd.exe /d /c job.cmd`
as one command. The trusted bundle maps plain filenames to text. Each invocation
creates a new staging workspace and unique AppContainer with no network capabilities.
Only that new workspace receives package-specific write access and a low integrity
label. No checkout ACLs, Defender exclusions or global firewall policy are changed.
The child starts suspended, joins a kill-on-close Job Object, then runs. The Python
API also accepts an `alive` callback for a trusted supervisor's expiry/revocation check.
Profiles are deleted after the process tree stops; staged outputs remain for review.

This is a local command backend, not an unrestricted autonomous model-agent adapter.
Standard system resources available to AppContainers remain readable, and the
kernel is shared. Test the exact tools/task before treating a different workload as
supported. Validate output paths and contents before importing artifacts into a
project; never execute an output merely because a worker produced it. Offline
dependency installation and arbitrary host access are not automatically added.

Primary implementation reference: [Microsoft AppContainer launch guidance](https://learn.microsoft.com/en-us/windows/win32/secauthz/implementing-an-appcontainer).
