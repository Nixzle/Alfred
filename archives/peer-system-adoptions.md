# Peer-System Adoption Doctrine

Promoted 2026-09-05 after Meta-Cerebro + Expertise Forge peer-system scouting and Council of Reeds review.

## Decision

Sanctum adopts the useful mechanisms from the peer-system donor sweep while rejecting wholesale framework adoption. Mechanism value and framework value are separate decisions.

These mechanisms are canonical doctrine immediately. Mechanical enforcement remains DOCUMENTED, CHECKED, ENFORCED, or OBSERVED according to actual runtime evidence.

## Adopted mechanisms

### 1. Promotion-aware memory
Use an explicit knowledge flow:

`transient/raw observation -> candidate -> review/consolidation -> promoted durable truth -> compiled task context`

Transient Mindscape state is not durable truth. Durable writes should preserve provenance, freshness and authority and should be reviewable when consequences are material.

### 2. Recall observability
Watcher should record, where practical and privacy-safe:
- what retrieval source was queried;
- what memories/documents were selected;
- what was omitted as stale, superseded, out-of-scope or low-confidence;
- whether a later miss indicates retrieval failure;
- retrieval latency/cost when measurable.

Retrieval quality itself is an observable system property.

### 3. Trace -> replay -> eval -> improvement loop
A meaningful failure should be reducible to the smallest replayable case practical. Watcher provides the trace; replay reconstructs the relevant state; Web of Destiny evaluates current versus candidate behavior; Failure Harvest decides whether doctrine/runtime changes are warranted.

### 4. Deterministic DAG execution
An LLM may plan or revise a task graph, but once dependencies and deterministic semantics are known, a deterministic scheduler should own execution ordering, retries, ready-state calculation and completion accounting where practical.

Prefer deterministic orchestration steps over model judgment when the property is mechanically decidable.

### 5. Hard-rule migration
Frequently consequential invariants should migrate from prose into the closest reliable enforcement boundary: tool wrapper, scheduler, state machine, CI gate, policy gate, schema, permission system or runtime guard.

Prompt-level doctrine remains useful for judgment; it is not a substitute for enforcement where enforcement is available.

### 6. Branchable durable memory
Material durable-memory changes should support candidate branches/diffs and review before canonical replacement where practical. Preserve immutable history, explicit supersession and merge provenance.

### 7. Memory portability and recovery
Durable Sanctum state should remain exportable/recoverable independently of one provider, model or hosted runtime. Recovery evidence should be periodically tested rather than assumed.

### 8. Confidence/freshness decay
Time-sensitive claims may lose retrieval authority as they age. Decay must be class-aware: stable doctrine should not decay like API availability, prices, model/tool capability, live service status or project runtime state.

Decay never silently converts an old fact into a new fact. It lowers confidence/priority and triggers revalidation when needed.

### 9. Cache-first routing
Before expensive reasoning, research or repeated tool execution, check whether a fresh, authoritative cached result already satisfies the request. Cache keys must include the material runtime/profile/version/scope dimensions needed to avoid stale reuse.

Caching never overrides freshness-sensitive revalidation, user-requested live checks or changed authority/project state.

### 10. Signed/immutable policy artifacts
High-risk execution surfaces should be able to bind policy/configuration to an immutable or cryptographically verifiable artifact where technically justified. Agents must not silently rewrite their own governing authority.

Signing is an implementation option, not a theatrical claim. Until verified, the status remains DOCUMENTED or CHECKED according to evidence.

### 11. Sandboxed temporary tool incubation
A new runtime tool/procedure may be trialed in a bounded sandbox with:
- explicit scope;
- generated schema/contract;
- test/eval cases;
- expiry;
- no automatic permanent authority expansion;
- promotion only after review/evidence.

Self-authored tools do not become canonical merely because they executed successfully once.

### 12. Event-driven Presence
When trustworthy event surfaces exist, prefer event-driven wakeups to polling for Presence/Watcher workflows. Preserve deduplication, bounded fan-out, source authentication, freshness and authority separation.

No event source means no claim of event-driven observation.

### 13. Fast correction-to-candidate path
Small but reusable user corrections should have a low-friction path into a durable candidate without requiring full Failure Harvest ceremony every time:

`correction -> candidate note -> later consolidation/promotion or rejection`

Meaningful failures still use full Failure Harvest.

### 14. Project/domain-local governance overlays
Global Sanctum doctrine remains project-independent. Projects may maintain stricter or domain-specific local rules, state and permissions. Project-specific verified truth outranks generic doctrine for that project while preserving the global authority model.

### 15. Persistent operation slices
Long-running processes should wake, perform bounded work, write explicit state/evidence, then sleep rather than requiring one immortal conversational process. Resume from durable state, not assumed memory.

### 16. Approval queues at effect boundaries
When an operation is otherwise ready but exceeds granted authority, preserve the prepared action and evidence in a reviewable approval state rather than discarding the work or executing optimistically.

### 17. Ledger/accounting as runtime state
For consequential operations, cost, effects, attempts, authority use and state transitions may be first-class runtime facts when they materially affect recovery, auditability or optimization.

## Rejected donor behavior

Do not adopt:
- entire peer frameworks merely to obtain one useful mechanism;
- automatic permanent self-modification;
- universal confidence decay across stable truth;
- opaque cache reuse without freshness/version keys;
- polling when reliable event delivery already exists;
- agent-executed scheduling where deterministic graph execution suffices;
- named subsystem inflation without a distinct responsibility.

## Integration map

- **Prime Memory / Archives:** promotion-aware memory, branch/merge, decay, portability, maintenance.
- **Mindscape / Presence:** transient state, event-driven wakeups, fast candidate capture.
- **Watcher:** recall observability, replay evidence, ledgers.
- **Web of Destiny:** replay-case evaluation and candidate comparison.
- **TVA / governance:** hard-rule migration, signed policy artifacts, approval boundaries.
- **Ultron Prime / orchestration:** cache-first routing, deterministic DAG execution, project-local overlays.
- **Spellbooks:** Checkpoint/Fork, Memory Maintenance, Deterministic First, Fast Learn, Cache First, Tool Incubation.

## Status discipline

Canonical doctrine means the mechanism is an accepted operating principle. It does not mean every runtime or surface mechanically implements it. Each surface must continue to distinguish DOCUMENTED, CHECKED, ENFORCED and OBSERVED behavior.
