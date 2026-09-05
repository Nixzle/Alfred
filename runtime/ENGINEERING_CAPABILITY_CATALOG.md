# Engineering Capability Catalog

Status: canonical catalog contract; individual tools remain surface/project-specific.

## Purpose

Provide Ultron a governed donor inventory for software engineering, coding and game development so capabilities are discovered before custom engineering begins.

## Selection order

`project-native -> language/framework-native -> existing connected tool -> trusted SDK/plugin/MCP -> reviewed open source -> proven pattern -> custom implementation by exception`

## Codebase intelligence

Capability classes:
- semantic repository maps;
- symbol/call/dependency graphs;
- LSP/indexing;
- tree-sitter parsing;
- recent-change/diff context;
- ownership/module maps.

Donor examples/classes: Aider repo map, LSP/tree-sitter/code-intelligence systems, repository search/indexing providers.

## Coding-agent interface

Capability classes:
- bounded file/symbol navigation;
- structured patching;
- terminal execution;
- trajectory inspection;
- replay;
- architect/editor separation;
- ask/context/code modes.

Donor examples/classes: SWE-agent ACI, Aider modes, OpenHands software-agent interfaces.

## Deterministic verification

Capability classes:
- formatter/lint/typecheck;
- focused tests;
- build/compile;
- affected-only tests;
- integration/e2e;
- mutation/property/fuzz/model-based tests;
- coverage/quality gates.

Prefer language/framework-native tools and project CI before new infrastructure.

## Build systems

Candidate donor classes:
- incremental/affected dependency graphs;
- remote/local caching;
- hermetic/reproducible builds;
- content-addressed artifacts;
- distributed test execution.

Use when build/test latency is a measured bottleneck.

## Runtime/dev environment

Capability classes:
- sandboxed terminals/containers;
- local/remote dev environments;
- deterministic fixtures;
- replayable run records;
- crash/log inspection.

## Game editor/runtime control

### Dota / Source 2
Use existing project Workshop/VConsole/Dota2 Workshop MCP tooling before custom bridges.

### Unity
Candidate donors: mature Unity MCP/editor bridges capable of scene/assets/scripts/tests/build/profiling/runtime inspection. Review current license, editor-version compatibility, tool exposure, execute-code safety and project binding before adoption.

### Unreal
Candidate donors: Unreal MCP/editor Python bridges with actor/asset/Blueprint/material/UI/VFX/PIE/screenshot/test capability. Prefer minimal typed tools plus introspection/execute-python escape hatch when safe.

### Godot
Candidate donors: Godot editor/runtime MCPs, CLI/headless tests, scene-tree/property inspection, screenshot/runtime automation. Review maturity before relying on a specific project.

## Device/UI replay

Candidate donor: Trailblaze-style semantic trails.
Use for repeated Android/iOS/web/game UI journeys: explore once, record semantic steps, deterministic replay, self-heal/re-author on drift.

## Game simulation/balance

Capability classes:
- deterministic combat/economy simulation;
- Monte Carlo/probability models;
- bot playthroughs;
- telemetry analysis;
- encounter generation validation;
- progression/economy curve checks.

## Multiplayer/networking

Donor classes:
- authoritative server/host simulation;
- prediction/reconciliation;
- rollback netcode;
- lag compensation;
- deterministic lockstep where appropriate;
- reconnect/state snapshot protocols;
- idempotent transaction/effect semantics.

## Performance/profiling

Capability classes:
- CPU/GPU profiling;
- frame-time/1% lows;
- memory/allocation/GC;
- network profiling;
- build-time profiling;
- asset/content loading;
- trace comparison/regression budgets.

## Reliability/distributed systems

Donor classes:
- idempotency keys;
- transactional outbox;
- leases/locks;
- queues/backpressure;
- circuit breakers/bulkheads;
- checkpoint/replay;
- schema/version migration;
- compensation/reconciliation.

## Security/supply chain

Capability classes:
- dependency vulnerability/license/provenance review;
- SBOMs;
- signed/reproducible artifacts;
- secret scanning;
- static analysis;
- least-privilege execution;
- extension/MCP trust filters.

## Software/game extension ecosystems

Donor examples/classes:
- OpenHands Extensions;
- Hermes plugins/skills/providers/MCP catalog;
- Goose extensions/recipes;
- Letta skills/mods;
- PydanticAI toolsets/durable execution;
- Claude/Codex-compatible skill/plugin registries;
- MCP registries and official SDKs.

Rule: catalog/discovery is not trust approval.

## Maintenance

Prime Sense should update/navigate this catalog when an active engineering bottleneck maps to a donor class. A capability record should exist only when it can plausibly change an implementation decision.
