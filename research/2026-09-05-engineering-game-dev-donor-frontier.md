# Engineering and Game Development Donor Frontier Sweep

Date: 2026-09-05
Mode: Cerebro + Expertise Forge (Mind Stone amplification)

## Objective

Expand Ultron's engineering capability by scouting coding agents, repository-analysis systems, extension registries, durable workflow engines, engine/editor automation, device replay systems, testing/evaluation frameworks, and conventional software/game-development practices.

## Strong donor mechanisms

### Aider
Adopted mechanisms:
- concise whole-repository map using symbol/dependency importance;
- architect/editor separation for risky or cross-cutting work;
- automatic lint/compile/test feedback after edits;
- explicit ask/context/code modes;
- git/diff awareness and narrow context controls.

Translation: repository map, right-level planning, smallest coherent patch, deterministic post-edit gates.

### SWE-agent
Adopted mechanisms:
- Agent-Computer Interface as a first-class performance variable;
- trajectory/run inspection;
- software issue -> repository exploration -> patch -> execution feedback loop;
- replayable trajectories as evidence.

Translation: treat awkward agent tooling as a systems defect; preserve coding trajectories for debugging and evals.

### OpenHands
Adopted mechanisms:
- public registry of reusable skills, executable plugins, integrations and automations;
- explicit repository boundaries between extension artifacts and execution/runtime core;
- progressive-disclosure skill files.

Translation: separate knowledge skills, executable plugins and provider/runtime code; keep third-party integration burden out of core.

### Goose
Adopted mechanisms:
- MCP extension directory and generic MCP compatibility;
- malware check before extension activation;
- portable declarative recipes with required extensions, parameters and subrecipes;
- subagents isolated from the main conversation;
- ACP interoperability.

Translation: portable recipes, extension trust screening, one-hub/many-capabilities architecture.

### Hermes
Previously promoted; engineering-relevant mechanisms reinforced:
- native MCP discovery and per-server tool filtering;
- plugin lifecycle hooks;
- replaceable memory/context/model providers;
- toolsets and platform-specific capability exposure;
- keep third-party integrations as external plugins to avoid core maintenance burden.

### Trailblaze
Adopted mechanisms:
- device/UI interactions recorded as semantic replayable trails;
- intelligent exploration once, deterministic replay thereafter;
- self-healing when UI drift invalidates a recorded semantic step;
- typed device-control surface and replay reports;
- goal-level interaction while preserving raw evidence on disk.

Translation: game/app smoke journeys should become replayable semantic scenarios, with intelligence reintroduced only on drift.

### Unity MCP ecosystem
Adopted mechanisms:
- direct editor control over scenes, GameObjects/components, assets, scripts, tests, builds and profiling;
- runtime/scene inspection and screenshots;
- explicit project/editor binding and tool exposure control;
- multiplayer and persistent-job support in some implementations.

Translation: do not build custom Unity agent bridges before reviewing mature editor MCPs.

### Unreal MCP ecosystem
Adopted mechanisms:
- Python/C++ editor control across actors, Blueprints, materials, UMG, Niagara, Sequencer, behavior trees and profiling;
- Play-In-Editor automation and screenshots;
- search/introspection + execute-python escape hatches for broad API coverage;
- persistence-safe mutation paths as explicit donor lessons.

Translation: inspect editor-native automation donors before bespoke Unreal integration.

## Untouched or under-raided donor domains

The sweep identified additional donor classes for future just-in-time research:

- compiler/toolchain architecture: incremental compilation, diagnostics, language servers, tree-sitter, static analysis;
- formal methods/property testing/model checking for state machines and invariants;
- database reliability: migrations, transactional outbox, event sourcing, CDC, schema evolution;
- distributed systems: consensus, leases, idempotency, backpressure, circuit breakers, bulkheads;
- SRE/production engineering: SLOs/error budgets, canaries, rollback, chaos testing;
- build systems: Bazel/Nx/Turborepo-style dependency graphs, remote caching, affected-only tests;
- package/supply-chain security: SBOMs, provenance, reproducible builds, signed artifacts;
- code intelligence: LSP, semantic indexes, call graphs, embeddings + symbol graphs;
- mutation testing and differential testing;
- fuzzing and property-based testing;
- game-engine ECS/data-oriented design where scale warrants it;
- game networking: rollback netcode, lag compensation, authoritative simulation, prediction/reconciliation;
- procedural content pipelines and validation;
- automated gameplay/balance simulation;
- accessibility tooling and automated UI readability checks;
- localization pipelines and pseudo-localization;
- shader/material/VFX profiling and automated visual regression;
- audio pipeline validation;
- crash analytics, symbolication and minidump triage;
- telemetry/event-schema governance;
- asset dependency/build caching and content-addressed pipelines;
- mod/plugin architecture and compatibility testing;
- live-ops/configuration/feature-flag systems;
- game-jam and rapid-prototyping methods;
- postmortem databases from shipped/failed games and software incidents.

## Prime Sense implications

Prime Sense should detect when one of these donor classes is obviously relevant before implementation becomes expensive. Examples:

- repeated full builds -> investigate incremental/affected-only build systems;
- flaky distributed side effects -> inspect idempotency/outbox/lease patterns;
- combinatorial state bugs -> inspect property testing/model checking;
- multiplayer desync -> inspect authoritative/prediction/reconciliation donors;
- repeated UI setup -> record/replay semantic trail;
- large unfamiliar codebase -> build semantic repo map;
- agent repeatedly edits wrong seam -> improve ACI/context projection rather than retrying prompts.

## Disposition

ADOPT mechanisms into existing Sanctum Archives/Presence/Spellbooks.
Do not migrate Ultron wholesale onto any donor runtime.
Install/connect external capability only for a real consumer and after trust/authority review.
