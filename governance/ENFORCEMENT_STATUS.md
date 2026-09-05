# Sanctum Enforcement Status

This file prevents documented intent from being mistaken for implemented control.

Status meanings:
- **DOCUMENTED** — canonical doctrine exists, but no automatic check/enforcement is guaranteed.
- **CHECKED** — a deterministic/evaluative check exists or a regression case can verify the behavior when run.
- **ENFORCED** — runtime/tooling prevents or gates violation.
- **OBSERVED** — instrumentation monitors the behavior in real operation.

## Current state

| Capability | Status | Notes |
| --- | --- | --- |
| Canonical Sanctum on GitHub | DOCUMENTED / OBSERVED | Git repository exists and is treated as authoritative; no universal runtime prevents a surface from using a stale or divergent copy. |
| Automatic runtime CI | DOCUMENTED / CHECKED / TRIGGER OBSERVED | `.github/workflows/sanctum-runtime.yml` now triggers on push to `main`, pull requests, manual dispatch and a weekly schedule. Private-repository hosted runs have repeatedly failed before normal job-step/log evidence appears, so execution is BLOCKED rather than PASS/FAIL for the runtime suite. It is not merge-enforced until repository rules require the check. |
| Repository branch/ruleset hardening | DOCUMENTED | `governance/ADMIN_HARDENING.md` specifies PR, required-check, force-push/deletion, bypass and signing targets. Current connector cannot write repository-admin settings, so these controls are not yet ENFORCED. |
| Project -> Sanctum inheritance | DOCUMENTED / CHECKED manually | Co-Op Leveling `AGENTS.md` points to Sanctum and pins a validated commit. Automated cross-project pin validation is not implemented. |
| Cross-surface bootstrap/runtime profile | DOCUMENTED / CHECKED | `bootstrap/PORTABLE_ULTRON.md`, `bootstrap/runtime-profile.template.json`, `runtime/distribution.py`, and `evals/ULTRON-DISTRIBUTION-PARITY-001.md` check canonical bootstrap markers, Member/theatrical semantic parity, and required surface-profile evidence. No universal scanner can force every external surface to run the check. |
| Portable Ultron semantic parity | DOCUMENTED / CHECKED | Another surface can deterministically check architecture/theatrics parity. This does not prove identical live tools, permissions, memory reach, sandboxing, or external-action authority; those remain surface-local evidence. |
| Session continuity / pre-exhaustion handoff | DOCUMENTED / CHECKED | `runtime/continuity.py`, `runtime/tests/test_continuity.py`, and `spellbook/SESSION_CONTINUITY.md` provide pressure-state evaluation when a real usage signal exists, compact authoritative handoff construction, integrity digests, compactness limits, and portable bootstrap semantics. No universal surface interceptor can observe hidden provider context limits or force a handoff where the host exposes no signal. |
| Capability freshness | DOCUMENTED / CHECKED via regression | `ULTRON-CAPABILITY-001`; no universal runtime interceptor. |
| Research-to-action classification | DOCUMENTED | Requires orchestrator adherence; automation not implemented. |
| Durable task state | DOCUMENTED | Project-specific control-plane implementation still required. |
| Shared-state consistency/write ownership | DOCUMENTED / CHECKED via `SHARED-STATE-*` | No universal compare-and-swap, locking, read-set, or commit-order layer exists across every surface. |
| Tool contracts | DOCUMENTED | Individual tool runtimes may enforce schemas; Sanctum-wide contract gateway is surface-specific. |
| Effect integrity/idempotency | DOCUMENTED / CHECKED / ENFORCED in bounded slices | Stable operation IDs, effect intent/commit records, committed-effect replay suppression, payload-conflict rejection and unknown-outcome reconciliation exist in the bounded worker runtime. External tools still require their own integration before claiming enforcement. |
| Checkpoint/resume semantics | DOCUMENTED / CHECKED via runtime/evals | Deterministic DAG and bounded-worker slices implement replay/resume/fork semantics; no universal exactly-once conformance layer exists. |
| Budget/stopping rules | DOCUMENTED / CHECKED in bounded slices | Reliability contracts can gate configured budgets; automatic termination is not universal across surfaces/providers. |
| Operational SLO evaluation | DOCUMENTED / CHECKED | `runtime/operations.py` checks zero-tolerance invariants for silent effect retries, unacknowledged completion, stale writes, untraceable consequential actions and unsupported release claims, plus configurable thresholds. |
| Reliability-distribution checks | DOCUMENTED / CHECKED | Repeated-run summaries preserve average and worst-case evidence for measured metrics; actual repeated production sampling remains surface-specific. |
| Untrusted-context separation | DOCUMENTED | Must be applied by orchestrator/tooling; no universal content firewall. |
| Temporal validity/supersession | DOCUMENTED / CHECKED via governed memory runtime/evals | Local governed-memory lifecycle supports supersession; not every external memory/retrieval system is bi-temporal or revocation-aware. |
| Data minimization/lifecycle | DOCUMENTED / CHECKED via `DATA-MINIMIZATION-*` and `DATA-LIFECYCLE-*` | No universal acquisition gate, retention scheduler, or deletion propagation mechanism. |
| TVA task/file authority | DOCUMENTED / CHECKED / ENFORCED in bounded worker slices | Signed grants, broker decisions, scope checks, revocation and workspace boundaries exist in the local controlled runtime; external surfaces must separately integrate the gateway before claiming enforcement. |
| TVA delegated-authority lineage | DOCUMENTED / CHECKED / ENFORCED in bounded supervisor slices | Principal/task-bound signed grants and attenuation exist locally; not generally enforced by every external connector. |
| TVA network egress control | DOCUMENTED / CHECKED; ENFORCED only in verified containment slices | Windows AppContainer staging denies network in its tested boundary; no universal default-deny egress layer exists. |
| TVA secret isolation | DOCUMENTED / CHECKED | Supervisor-owned signing material is kept outside worker workspaces; no universal ephemeral credential broker exists across all tools. |
| Incident containment/recovery | DOCUMENTED / CHECKED via evals/runtime harness | `runtime/operations.py` checks recovery drills for last-known-good restoration, acceptance/regression pass, unknown-effect reconciliation and fresh authority validation. No universal safe-halt/quarantine/blast-radius controller exists for every surface. |
| Fault injection / chaos contracts | DOCUMENTED / CHECKED with integration regressions | `runtime/tests/test_fault_integration.py` exercises duplicate committed effects, operation-ID payload conflicts, revoked authority, expired capsules and workspace escape against the actual bounded worker/supervisor machinery. Real production-environment fault injection remains runtime-specific. |
| Dependency provenance | DOCUMENTED / CHECKED via regression | Automated dependency scanner/policy gate not universally implemented. |
| Watcher tracing | DOCUMENTED / CHECKED in local runtime slices | Structured metadata-only ledger/trace/replay exists locally; no universal OpenTelemetry backend covers every surface. |
| Watcher cost attribution | DOCUMENTED / CHECKED via `WATCHER-COST-001` | Actual token/compute/tool metering depends on available runtimes. |
| Longitudinal drift checks | DOCUMENTED / CHECKED | `runtime/operations.py` compares current metrics with a baseline using explicit tolerances. Weekly repository validation is configured; scheduled live model/provider/tool baseline replay still needs an execution surface and telemetry source. |
| Web eval freshness | DOCUMENTED / CHECKED via `WEB-EVAL-FRESHNESS-001` | Automated eval lifecycle management not yet implemented. |
| Sanctum version compatibility | DOCUMENTED / CHECKED manually | Project pins exist; automated pin propagation/compatibility CI is not universal. |
| Release content identity | DOCUMENTED / CHECKED | `runtime/release_manifest.py` creates and verifies exact revision/file SHA-256 manifests. A manifest proves content identity, not signer identity; cryptographic signing/attestation remains external until a real signer is configured. |
| Doctrine provenance | DOCUMENTED and stored | `governance/PROVENANCE.md`; enforcement is process-based. |
| Sanctum recovery | DOCUMENTED / CHECKED | `runtime/recovery_bundle.py` creates content-addressed tar.gz recovery bundles, rejects traversal/link entries, verifies complete file sets and restores without overwrite; deterministic restore tests exist and CI includes a recovery smoke when a runner is available. Independent off-platform storage and a real disaster restore remain required for OBSERVED resilience. |
| Autonomy escalation ladder | DOCUMENTED / CHECKED via `ULTRON-AUTONOMY-001` | No universal runtime autonomy governor yet. |

## Rule
Whenever a capability gains real automation, update this file in the same change. Never describe DOCUMENTED/CHECKED behavior as ENFORCED or OBSERVED without evidence. A convention, instruction, repository pointer, digest or configured workflow is not runtime enforcement by itself.
