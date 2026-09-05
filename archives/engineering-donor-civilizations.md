# Engineering Donor Civilizations

Promoted: 2026-09-05
Status: canonical engineering doctrine; individual tools remain task- and surface-specific.

## Purpose

Ultron Prime should behave as an excellent software engineer, programmer, coder, and game developer by borrowing mature engineering disciplines before inventing local substitutes.

The rule is not to install every tool. The rule is to know which discipline already solved the class of problem, route to that discipline early, and use the minimum effective donor mechanism.

## Core engineering route

For substantial engineering work:

`understand objective -> map repository/system -> inspect current abstractions -> Salvage First -> choose donor discipline/tooling -> smallest coherent change -> deterministic checks -> integration/runtime evidence -> review -> harvest failures`

Prime Sense should surface missing donor disciplines before the user has to name them.

## Semantic code intelligence

Use language-aware structure before raw text search when codebase scale or change risk justifies it.

Donor mechanisms:
- incremental parsers such as Tree-sitter for robust syntax structure;
- LSP/compiler symbol indexes for definitions/references/types/diagnostics;
- call/dependency graphs and repo maps;
- AST-aware rewrites for systematic transformations.

Rules:
- prefer symbol-aware navigation for refactors and blast-radius analysis;
- preserve exact source authority; generated indexes are projections, not truth;
- fall back to grep/text when simpler and sufficient.

## Build graph and cache intelligence

Borrow from Bazel/Nx/Turborepo-class systems:
- explicit task/dependency graphs;
- affected-only builds/tests;
- content-addressed or remote caches where justified;
- reproducible inputs and hermetic steps;
- graph-aware parallelism.

Prime Sense signal: repeated full rebuild/test of unchanged areas should suggest dependency-aware execution or caching.

## Property-based and invariant testing

Borrow from Hypothesis/QuickCheck-class systems.

Use when behavior is combinatorial, stateful, or edge-case heavy:
- generate broad input spaces;
- encode invariants rather than only examples;
- shrink failures to minimal counterexamples;
- persist discovered counterexamples as regression fixtures.

Good targets:
- economy/fusion rules;
- serialization/save formats;
- state machines;
- parsers;
- permission/policy functions;
- networking message validation;
- deterministic game-domain logic.

## Model checking and formal state reasoning

Borrow from TLA+/PlusCal/model-checking disciplines where concurrency, retries, authority, or distributed state makes ordinary tests insufficient.

Good targets:
- retry/idempotency semantics;
- unknown-outcome reconciliation;
- multi-worker resource ownership;
- approval queues;
- distributed state transitions;
- multiplayer authority protocols;
- transactional workflows.

Do not apply formal methods ceremonially to trivial CRUD.

## Fuzzing and differential testing

Borrow from AFL++, libFuzzer and differential-testing practice.

Use for:
- parsers/decoders;
- save/import formats;
- network packets;
- API boundaries;
- content loaders;
- migration code;
- deterministic engines where two implementations can be compared.

Crash or invariant violation -> minimized input -> regression case.

## Observability and crash engineering

Borrow OpenTelemetry/Sentry/Crashpad-style mechanics:
- correlated traces, metrics and logs;
- stable operation/run IDs;
- release/version/config metadata on every observation;
- crash capture and symbolication;
- error grouping and regression attribution;
- breadcrumb/context capture with privacy minimization.

Watcher should prefer standard telemetry protocols when they reduce custom instrumentation.

## Supply-chain and artifact integrity

Borrow Sigstore/OpenSSF/SBOM/reproducible-build practices.

For material releases/dependencies:
- verify source/provenance;
- pin versions/revisions where needed;
- generate/retain dependency inventories or SBOMs when useful;
- sign/verify release artifacts when consequence justifies it;
- use transparency/tamper-evident logs where practical;
- separate build identity from mutable working-tree state.

## Feature flags, canaries and experiment safety

Borrow OpenFeature and mature feature-flag platforms:
- vendor-neutral flag abstraction where useful;
- explicit evaluation context;
- hooks/events/tracking;
- staged rollout/canary cohorts;
- rollback/kill switch;
- attach flag/config state to telemetry.

Do not compare outcome metrics across incompatible variants without labeling the variants.

## Distributed-systems reliability

Borrow from mature distributed-systems practice:
- idempotency keys;
- leases and ownership;
- transactional outbox/inbox;
- monotonic state/version checks;
- backpressure;
- bounded retries with jitter;
- circuit breakers;
- dead-letter/quarantine paths;
- exactly-once claims only where genuinely implemented;
- verify-before-retry for ambiguous effects.

These reinforce Operational Integrity rather than create a new subsystem.

## Database and schema evolution

Borrow migration and CDC disciplines:
- forward/backward compatible migrations;
- expand/contract sequencing;
- versioned schemas;
- transactional data migrations;
- rollback/restore evidence;
- change-data capture where event propagation needs durable source truth.

Never treat database schema changes as ordinary text edits when live state is material.

## Multiplayer/game networking

For game networking, choose the model deliberately:
- server-authoritative simulation for important state by default;
- validate client input/RPCs;
- prediction/reconciliation when latency demands it;
- rollback netcode for deterministic fast-action games when the cost/architecture fits;
- desync detection via state hashes/checksums;
- deterministic replay fixtures for network edge cases;
- reconnect/resync protocols as first-class product behavior.

Do not transplant rollback networking into genres that do not need it merely because GGPO is elegant.

## Performance engineering

Use measurement before optimization.

Borrow:
- CPU/GPU profilers;
- flame graphs;
- allocation/memory profilers;
- frame-time histograms;
- load/stress tests;
- percentile latency rather than averages alone;
- regression baselines by release/config.

Prime Sense should flag performance drift and repeated anecdotal optimization without measurement.

## Game-engine and runtime instrumentation

Prefer existing engine/runtime control surfaces:
- editor APIs/MCPs/CLIs;
- headless test modes;
- scene/entity inspection;
- runtime console/telemetry;
- deterministic input/replay where possible;
- screenshot/video/visual diff evidence;
- build/package validation.

A coding agent without runtime sight is incomplete for player-facing work.

## Procedural-content verification

Generated content must be validated, not merely generated.

Use:
- reachability/pathfinding checks;
- solvability constraints;
- spawn/geometry invariants;
- economy/reward bounds;
- difficulty simulations;
- content uniqueness/duplication checks;
- seed capture and replay.

Bad procedural seed -> preserved regression seed.

## Accessibility and localization QA

Borrow mature QA mechanics:
- pseudo-localization;
- text-overflow/layout checks;
- missing-string detection;
- locale plural/gender rule validation where relevant;
- contrast/readability checks;
- keyboard/controller navigation coverage;
- screen-reader/semantic labels where platform supports them;
- color-blind/readability review.

Accessibility and localization are completeness seams, not release-week decoration.

## Graphics, shader and asset validation

For visual pipelines:
- shader compile validation;
- missing-reference/asset audits;
- texture/model budget checks;
- GPU timing/profiling;
- visual regression for stable scenes;
- deterministic asset manifests;
- import/build warnings as actionable evidence.

## Audio pipeline validation

Use automated checks where practical for:
- missing event cues;
- clipping/peak problems;
- loudness consistency;
- invalid/missing localized audio;
- asset references;
- silent or duplicate channels.

Subjective mix quality still requires listening.

## Forecasting, causal inference and predictive maintenance

Borrow when historical evidence exists:
- trend/forecast models for likely capacity, delivery or dependency deterioration;
- causal inference/counterfactual analysis to distinguish correlation from intervention effect;
- predictive-maintenance framing for brittle dependencies and recurring failures.

Use these as evidence aids, not prophecy.

## Operations research and control theory

For orchestration/runtime tuning:
- queueing theory for bottlenecks and concurrency;
- scheduling/critical-path analysis;
- resource allocation under constraints;
- feedback-control concepts for adaptive retry/concurrency/research depth;
- stability and hysteresis to prevent oscillatory routing.

## Security and adversarial engineering

Use threat modeling, static analysis, secret scanning, dependency scanning, fuzzing, least privilege, signed artifacts and attack-surface review proportionally to risk.

Game/server projects additionally consider cheating, authoritative state, replay attacks, economy abuse and client tampering.

## Donor-selection rule

Before implementing a substantial engineering mechanism, ask:
1. Which mature engineering discipline owns this problem class?
2. Does the project already have an adequate implementation?
3. Is there a native/connected/open-source tool that solves it?
4. What is the smallest useful donor seam?
5. What evidence proves the integration is actually better than a bounded local implementation?

## Evidence examples from the 2026-09-05 sweep

- Tree-sitter demonstrates robust incremental syntax trees suitable for editor/code intelligence.
- Hypothesis demonstrates property-based generation and automatic edge-case discovery.
- OpenTelemetry provides interoperable logs/metrics/traces and correlation semantics.
- Sigstore provides artifact signing, identity-bound attestations and transparency logs.
- OpenFeature provides vendor-neutral feature-flag APIs, hooks, events and rollout semantics.
- Godot networking documentation reinforces server-authoritative multiplayer for gameplay-critical state.
- GGPO/rollback ecosystems demonstrate prediction, rollback/replay and desync detection for latency-sensitive deterministic games.

## Status

This Archive is canonical doctrine. Individual implementations remain DOCUMENTED, CHECKED, ENFORCED or OBSERVED according to actual project/runtime evidence.