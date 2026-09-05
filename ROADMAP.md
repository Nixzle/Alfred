# Sanctum Implementation Roadmap

This file tracks known implementation work. The purpose is to prevent validated gaps from dissolving into prose.

## Status model
- `IMPLEMENT NOW` — foundational, low-risk, high-value work that should be executed before further speculative expansion.
- `NEXT` — important work that depends on or benefits from the IMPLEMENT NOW layer.
- `LATER` — useful but not currently on the critical path.
- `BLOCKED` — cannot proceed until a named external dependency/permission/runtime is available.

A task is not complete because doctrine exists. Completion requires the declared acceptance evidence.

## Accepted foundation

### 1. Durable task/control plane
**Objective:** Give long-running and multi-agent work an external source of task truth.

**Minimum state:**
- objective
- owner/worker
- dependencies
- status
- acceptance criteria
- evidence
- blocker
- next action
- attempt/retry history where relevant
- authoritative version/revision
- read snapshot/causal version where shared state is mutable
- write owner and merge/integration owner
- observation/effective timestamps and supersession for changeable facts

**Acceptance:** A fresh worker/session can determine what is active, blocked, complete, current, superseded, and next without replaying chat history. Concurrent writers cannot silently erase one another or commit work derived from materially stale state without a detected conflict/revalidation step.

**Why now:** Ultron cannot reliably orchestrate persistent work if conversation history remains the de facto task database or if shared state silently accepts lost updates.

**Status:** Accepted for the local signed declarative worker in PR #7; issue #1 closed. `runtime/validate.py` replays acceptance and fresh-session recovery. This does not claim production coverage on every surface.

## IMPLEMENT NOW

### 2. Images of Ikonn runtime foundation
**Objective:** Turn Images of Ikonn from doctrine into real autonomous execution infrastructure.

**Minimum capability:**
- isolated/projected/forked worker context modes;
- isolated worktree/runtime where needed;
- checkpoint/resume/replay/fork semantics;
- retry/recovery;
- stable task and operation IDs;
- effect ledger for state-changing/external actions;
- idempotency keys or at-most-once gates where supported;
- verify-before-retry and unknown-outcome reconciliation;
- partial-effect compensation/recovery where possible;
- structured Task Capsule input;
- structured handback;
- gap-based stuck detection;
- state version/read-set validation before commit;
- write conflict detection and deterministic integration/ordering;
- clean termination.

**Acceptance:** An Image can execute a bounded task, fail/restart safely, and hand back evidence without contaminating another Image's state, duplicating committed effects, resurrecting consumed authority, or silently committing against a stale/conflicting snapshot.

### 3. Watcher telemetry and recall-observability foundation
**Objective:** Capture real orchestration/execution evidence, including retrieval quality.

**Minimum capability:**
- routing/delegation trace;
- principal/task/delegation lineage where available;
- tool/action trace;
- stable operation IDs;
- effect intent / dispatch / observed / committed / compensated / unknown state;
- state versions, conflicts, and commit ordering;
- retries/failures;
- evidence links;
- task/member/worker identifiers;
- temporal supersession/currentness events;
- retrieval source queried, selected results, superseded/omitted results where practical;
- cache hit/miss/revalidation events where useful;
- sensitive-data acquisition and disclosure-boundary metadata without copying unnecessary payloads;
- incident/quarantine/recovery events;
- cost/latency where measurable;
- privacy/redaction mode.

**Acceptance:** A meaningful failure or incident can be reconstructed from trace evidence without relying on the worker's narrative, and a material retrieval miss can be diagnosed as source, search, ranking, freshness or scope failure where evidence permits.

### 4. TVA enforcement boundary and hard-rule migration
**Objective:** Move critical authority rules from `DOCUMENTED` toward `ENFORCED` and systematically migrate frequently consequential prose invariants to runtime/tool boundaries.

**Minimum capability:**
- allow / deny / require-approval decision point;
- authenticated principal and delegation lineage;
- task/operation-bound authority with expiry;
- authority attenuation across child workers;
- replay/confused-deputy protection;
- task-scope checks;
- filesystem/workspace boundary checks;
- destructive-action gate;
- secret/credential minimization;
- network egress policy where technically available;
- dependency-install authority checks;
- data-acquisition/disclosure minimization at tool boundaries;
- emergency revocation, safe halt, and quarantine path;
- inventory of high-value prose invariants and their closest enforceable runtime boundary.

**Acceptance:** A worker cannot silently expand or re-delegate its authority, replay an expired/consumed grant, over-acquire sensitive data, or perform a disallowed consequential action merely by asking a tool to do it. Material hard rules have an explicit DOCUMENTED/CHECKED/ENFORCED status and migration target.

### 5. Promotion-aware governed memory pipeline
**Objective:** Turn durable memory into an explicit lifecycle rather than an accumulation surface.

**Minimum capability:**
- transient/raw -> candidate -> reviewed/promoted -> compiled-context states;
- source/authority/provenance metadata;
- observation/effective-time fields;
- current/historical/disputed/unknown validity state;
- branch/diff/merge semantics for material candidate changes;
- deterministic supersession/revocation without destroying audit history;
- scoped retrieval by user/project/surface/task;
- per-class retention/expiry rules;
- correction/deletion propagation where supported;
- confidence/freshness decay for volatile facts only;
- acquisition-stage privacy audit;
- derived-data sensitivity handling;
- export/import and recovery representation.

**Acceptance:** Transient context is not silently promoted; durable changes are reviewable where material; superseded facts stop contaminating current retrieval; historical `as of` queries remain possible; volatile facts lose authority or trigger revalidation appropriately; durable state can be exported and restored with provenance.

### 6. Deterministic DAG execution layer
**Objective:** Let models plan or revise work while deterministic runtime logic owns mechanically decidable graph execution.

**Minimum capability:**
- dependency graph representation;
- deterministic ready-state calculation;
- explicit task status transitions;
- bounded retries governed by observed outcomes;
- stable run IDs;
- replayable run records;
- deterministic branch/join semantics where possible;
- clean escalation when a graph node requires judgment or new information.

**Acceptance:** Known workflow semantics do not depend on an LLM remembering what step comes next, and an interrupted run can be reconstructed/replayed from explicit graph/run state.

### 7. Replay-case quality loop
**Objective:** Connect Watcher evidence to durable improvement pressure.

**Minimum capability:**
- convert meaningful failures/traces into minimal replay cases;
- bind replay case to source evidence/version;
- run current-versus-candidate behavior in Web of Destiny;
- preserve pass/fail/uncertain results;
- route confirmed generalizable failures into Failure Harvest or runtime fixes.

**Acceptance:** At least representative routing, retrieval, authority, recovery, donor-discovery and stale-state failures can be reproduced without waiting for a user to rediscover them in production.

### 8. Memory recovery/export foundation
**Objective:** Avoid treating one hosted system, retrieval backend or provider as immortal durable truth.

**Minimum capability:**
- documented export format;
- provenance/version preservation;
- import/restore path;
- independent clone/mirror path where practical;
- periodic restore verification.

**Acceptance:** Sanctum's durable knowledge can be reconstructed from an independent export/clone with materially equivalent active doctrine, provenance and supersession state.

## NEXT

### 9. Web of Destiny automated regression harness
**Objective:** Execute Sanctum regression cases automatically rather than only reasoning about them manually.

**Minimum capability:**
- machine-readable eval cases;
- deterministic checks where possible;
- candidate-vs-current comparison;
- pass/fail evidence;
- regression blocking for material doctrine changes;
- fault injection for timeout-after-commit, partial effects, crash/resume, stale snapshots, concurrent writes, expired delegation, superseded facts, privacy over-acquisition, donor-ecosystem misses and incident recovery.

**Acceptance:** Seed routing, capability freshness, verification-strength, Bot scope, Watcher trace, Ikonn recovery, TVA authority, peer-system donor and operational-integrity cases can be run repeatably.

### 10. Longitudinal drift checks
**Objective:** Detect behavior changes when models, providers, tools, or runtimes drift even if Sanctum doctrine does not change.

**Minimum capability:** stable baseline eval set, periodic replay, quality/tool-use/cost/latency comparison, thresholded drift flag, and eval-set freshness review.

**Acceptance:** A material behavior regression can be detected without waiting for a user to notice it in production.

### 11. Sanctum version compatibility automation
**Objective:** Prevent projects from silently inheriting incompatible Sanctum changes.

**Minimum capability:** project pin to Sanctum commit/version, current-vs-pinned comparison, compatibility/eval gate before promotion, explicit update record.

**Acceptance:** A project can prove which Sanctum revision it was validated against and whether moving to a newer revision is safe.

### 12. Sanctum distribution / inheritance checks
**Objective:** Ensure projects that claim Sanctum inheritance can actually discover the canonical repo and relevant doctrine.

**Minimum capability:** inheritance pointer, accessibility check, stale/missing pointer detection, project-specific precedence rule.

**Acceptance:** A compatible fresh agent entering a project can locate the Sanctum, load relevant doctrine, and preserve project-local authority without manual chat archaeology.

### 13. Cache-first routing prototype
**Objective:** Reduce repeat reasoning/research/tool cost without reusing stale evidence.

**Minimum capability:**
- material cache key including task/scope/source/version/runtime/freshness dimensions;
- explicit freshness horizon;
- authoritative-source preference;
- hit/miss/revalidation telemetry;
- bypass for user-requested live checks and changed authority/project state.

**Acceptance:** Repeated equivalent tasks can reuse valid evidence measurably while freshness-sensitive tasks continue to revalidate.

### 14. Signed/immutable policy artifact prototype
**Objective:** Make high-risk runtime policy independently verifiable and non-self-modifiable where technically justified.

**Minimum capability:** policy/version ID, digest/signature where supported, issuer identity, action classes, authority/expiry, tool/workspace/network/data scope, effect-time validation.

**Acceptance:** A supported runtime can reject stale/mismatched/unauthorized policy state, with verification evidence distinct from prompt-level doctrine.

### 15. Event-driven Presence prototype
**Objective:** Prefer reliable source events to polling where an event surface exists.

**Minimum capability:** source identity, stable event IDs/deduplication, timestamps, scope, bounded fan-out, replay protection, untrusted-payload handling, authority separation.

**Acceptance:** A supported surface responds to real events without duplicate wakeups or converting event content into authority.

### 16. Sandboxed tool incubation prototype
**Objective:** Trial new tools/helpers safely before permanent installation or authority.

**Minimum capability:** narrow schema/contract, isolated scope, minimum permissions, explicit expiry, representative tests, evidence handoff, promotion/rejection state.

**Acceptance:** A temporary tool can be tested and discarded without silently gaining durable authority or becoming canonical.

### 17. Fast correction-to-candidate pipeline
**Objective:** Capture small reusable corrections cheaply while preserving governed promotion.

**Minimum capability:** correction capture, scope classification, candidate record, source/provenance, project-vs-general classification, later promote/reject decision.

**Acceptance:** Small corrections stop disappearing without forcing every minor improvement through full Failure Harvest ceremony.

## LATER

### 18. Doctrine provenance automation
**Objective:** Make `why does this rule exist?` answerable mechanically.

**Target:** Link doctrine changes to triggering failure, evidence, evals, decision status, peer donor where relevant, and superseded rule.

### 19. Cost-efficiency feedback loop
**Objective:** Let Watcher evidence teach Ultron whether a member/spell/delegation/routing pattern is worth its coordination cost.

**Target:** Compare reliability/quality gains against latency, token, compute, cache benefit, tool cost and retry cost.

### 20. Dependency trust automation
**Objective:** Automate checks for newly proposed packages, repositories, MCPs or external tools.

**Target:** Publisher/maintainer signals, license, vulnerabilities, suspicious install behavior, necessity, provenance and community/maintainer failure evidence before consequential adoption.

### 21. Persistent-operation slices
**Objective:** Support bounded wake-work-write-sleep processes rather than requiring immortal conversations.

**Target:** Durable wake condition, task/run state, bounded execution, explicit checkpoint, next wake condition and no dependence on hidden conversational continuity.

### 22. Approval queue runtime
**Objective:** Preserve prepared consequential actions that are waiting on authority rather than discarding state or executing optimistically.

**Target:** approval-required state, actor/authority target, prepared effect digest, expiry, evidence, approve/reject/revise transition.

### 23. Runtime accounting/ledger refinement
**Objective:** Treat cost/effect/attempt/authority-use accounting as first-class runtime evidence when materially useful.

**Target:** operation cost, attempt count, effect state, authority grant use, reconciliation state, causal links and retention policy.

## BLOCKED

Items belong here only when a concrete external dependency prevents work. Each blocked item must state blocker, owner of unblock, what can continue meanwhile, and re-probe condition.

**Current state:** No foundational roadmap item is classified BLOCKED merely because its implementation is non-trivial.

## Execution order
1. Durable task/control plane
2. Ikonn runtime foundation
3. Watcher + recall observability
4. TVA enforcement + hard-rule migration
5. Promotion-aware governed memory
6. Deterministic DAG execution
7. Replay-case quality loop
8. Memory recovery/export
9. Web automated evals
10. Cache/policy/event/tool-incubation prototypes
11. Drift/version/distribution checks

The exact engineering order may be adjusted when implementation reveals dependencies, but changes require evidence rather than convenience.

## Research policy
Do not run additional broad discovery sweeps while IMPLEMENT NOW items remain unaddressed unless implementation hits a concrete uncertainty, Watcher detects unexplained friction, a major platform/tool change creates a new capability or risk class, a peer-system donor materially changes the capability map, or the Web identifies a regression current doctrine cannot explain.

Research is just-in-time by default. Meta-Cerebro must still apply the peer-system donor policy when Sanctum itself is the object of improvement.
