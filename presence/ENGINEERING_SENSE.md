# Prime Sense — Engineering and Game Development Signals

Status: canonical Presence extension
Promoted: 2026-09-05

Prime Sense should not only notice project/business events. During active software or game-development work it should notice engineering conditions that predict rework, fragility, wasted effort or incomplete delivery.

## Codebase comprehension signals

Raise attention when:

- substantial edits are proposed without enough repository/symbol/dependency mapping;
- the same file or module repeatedly surprises workers;
- multiple systems duplicate the same concept under different names;
- a change crosses module boundaries without an explicit interface/ownership plan;
- recent git history materially changes assumptions but has not been inspected.

Route: repo map / Scout First / Archives before editing.

## Verification signals

Raise attention when:

- edits repeatedly land without lint/build/test feedback;
- tests cover internals but not the reported failure/user journey;
- CI is green while runtime evidence remains absent;
- a bug has recurred but no regression fixture exists;
- an integration/multiplayer/runtime claim is being upgraded from portable-only evidence.

Route: Evidence Lock -> deterministic gates -> runtime/trajectory inspection -> Failure Harvest.

## Architecture signals

Raise attention when:

- new abstraction has only one consumer and no unavoidable second consumer;
- a small feature requires an unexpectedly large diff;
- dependency count grows faster than user/player capability;
- repeated patches cluster around the same unstable seam;
- state ownership is ambiguous;
- retries/side effects lack idempotency/reconciliation;
- temporary workaround becomes a dependency for new work.

Route: Salvage First / Council / Scope Lock; refactor only when evidence says the seam is the bottleneck.

## Debugging signals

Raise attention when:

- workers make speculative edits without a reproducible failure;
- the same hypothesis is retried without new evidence;
- logs/runtime state are available but unused;
- failures disappear under mocks but persist in integration;
- environment/version differences are not recorded.

Route: reproduce -> minimize -> observe -> falsify -> smallest fix -> regression.

## Performance signals

Raise attention when:

- performance work begins before profiling;
- averages hide spikes/1% lows;
- resource cost drifts gradually;
- one subsystem dominates frame/latency/build time;
- generated content/assets grow without pipeline/budget checks.

Route: profile -> bottleneck -> one optimization -> benchmark -> retain/revert.

## Game-development signals

Raise attention when:

- code changes are not exercised in the actual engine/runtime;
- asset/UI production outruns playable flow;
- a mechanic is technically complete but player goal/feedback/tension is unclear;
- repeated setup makes playtesting expensive but no replay fixture exists;
- content additions require bespoke controller code instead of data/factory expansion;
- multiplayer authority/desync behavior is inferred from solo tests;
- art/audio polish is applied to mechanics that have not survived playtests;
- game feel is being changed without a concrete observed symptom/comparison target.

Route: playable-first runtime loop, replay trail, content factory, telemetry, player feedback.

## Donor escalation

When one of these signals repeats, Prime Sense should ask whether a mature donor discipline already solves it. Examples:

- poor large-repo navigation -> Aider/SWE-agent/LSP/code-intelligence donors;
- repetitive UI/device setup -> Trailblaze/replay automation;
- engine blindness -> Unity/Unreal/Godot editor-control donors;
- slow full builds -> incremental build/cache systems;
- flaky side effects -> distributed-systems/idempotency donors;
- combinatorial rule bugs -> property-based/model-checking donors;
- multiplayer desync -> authoritative networking/prediction/reconciliation donors;
- extension overload -> Hermes/OpenHands/Goose capability filtering/registry patterns.

The user should not need to identify the relevant engineering discipline before Prime Sense considers it.

## Guardrail

Engineering signals create hypotheses and routing pressure. They do not authorize broad refactors or new dependencies by themselves. Preserve the active acceptance contract and choose the smallest intervention that evidence supports.
