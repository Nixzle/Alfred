# Peer-System Donor Policy

Use when Sanctum itself, another agent operating system, orchestration framework, memory architecture, research system, workflow engine, durable context system, plugin ecosystem, MCP ecosystem, or agent-facing API layer is being improved.

## Rule

Meta-Cerebro must not assume the current taxonomy is sufficient merely because it is internally coherent. Treat credible peer systems **and composable capability ecosystems** as donors and apply Salvage First to the orchestration layer itself.

A bounded peer-system sweep should ask:

- Which peer frameworks solve the same state, memory, orchestration, delegation, recovery, observability, evaluation, context, integration, or authority problem differently?
- Which plugin/MCP/API capabilities already expose the desired integration so we do not build a native adapter unnecessarily?
- Which capabilities do peers make first-class that we currently leave implicit?
- Which mechanisms reduce recovery time, state loss, memory entropy, context pollution, tool misuse, coordination overhead, custom-integration work, or human intervention?
- Which patterns can be absorbed without importing the whole framework?
- What maintainer/community evidence reveals their failure modes, operational scars, or maintenance burden?
- Are we rejecting a useful mechanism merely because the host framework is otherwise overbuilt for us?
- Are we about to write an integration already available through a trusted built-in tool, connected plugin, curated MCP, official API client, or established open-source adapter?
- What is simpler in our current architecture and should remain untouched?

## Source classes

Use current evidence where material from several classes such as:

- peer agent runtimes and orchestration frameworks;
- second-brain / durable-memory systems;
- workflow engines and state machines;
- memory maintenance / retrieval systems;
- evaluation and tracing platforms;
- plugin/extension ecosystems;
- official and curated MCP registries;
- broader MCP marketplaces for discovery, with separate trust review;
- agent-facing APIs and official SDKs;
- policy/authorization/approval middleware;
- maintainer issues, changelogs and postmortems;
- practitioner communities and implementation reports;
- open-source code and examples.

The goal is not a catalogue. Stop when new donors stop changing the capability map or adoption decision.

## Integration salvage order

When the missing capability is an external integration, prefer:

`existing native capability -> already-connected plugin/tool -> trusted official/curated MCP or SDK -> reviewed open-source adapter -> broader registry discovery -> custom integration by exception`

A registry listing is discovery evidence, not permission or trust. Before enabling an external capability, inspect publisher/provenance, license, auth/secret scope, exposed tools, network/data access, maintenance/community evidence, security posture, versioning, and whether a smaller per-tool surface can satisfy the task.

## Decision classes

Classify each mechanism or integration as:

- `ADOPT` — fits existing Sanctum architecture and should become doctrine/implementation;
- `PROTOTYPE` — promising but requires bounded evidence before canonical use;
- `WATCH` — potentially valuable, insufficient present benefit;
- `REJECT` — worse than current Sanctum or too costly/risky/duplicative.

Always separate **mechanism value** from **framework/provider adoption**. It is valid to ADOPT one capability while REJECTING the framework or provider that contains it.

## Current promoted findings

The 2026-09-05 peer-system reviews promoted these mechanisms:

- checkpoint / resume / replay / fork state semantics;
- memory defragmentation and consolidation;
- explicit transient -> durable promotion;
- `ISOLATED`, `PROJECTED`, and `FORKED` worker context modes;
- deterministic-step-first mixed orchestration;
- stronger use of versioned memory/history as an audit surface;
- promotion-aware memory and recall observability;
- replay-case quality loops;
- resource ownership for parallel work;
- deny-by-default effect policy and tamper-evident decision evidence;
- signed erasure/deletion evidence where justified;
- outcome-linked confidence/freshness for volatile memory;
- plugin lifecycle hooks and provider contracts;
- curated MCP/plugin capability catalogs with per-tool filtering;
- host-owned extension credentials/trust gates;
- agent-as-capability patterns with narrow governed surfaces.

See `archives/state-memory-orchestration.md`, `archives/peer-system-adoptions.md`, and `archives/reliability-and-tool-ecosystem.md`.

## Failure condition

A broad Meta-Cerebro run intended to improve an orchestration, memory, or integration system that inspects only papers, generic best practices, or primitive tools while skipping credible peer operating systems **or relevant plugin/MCP/API ecosystems** is incomplete unless a fresh prior sweep already covers the material decision space.

Failure Harvest: `research/2026-09-05-peer-sanctum-donor-blindness-failure-harvest.md`.
Regression: `evals/CEREBRO-PEER-SYSTEM-DONORS-001.md`.
Hermes/MCP sweep: `research/2026-09-05-hermes-mcp-plugin-sweep.md`.
