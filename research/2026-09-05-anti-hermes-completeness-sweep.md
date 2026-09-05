# Anti-Hermes Completeness Sweep

Date: 2026-09-05
Mode: Prime Sense -> Sanctum -> Cerebro + Mind Stone (Expertise Forge)

## Question
Are current Sanctum donor sweeps complete enough to stop broad raiding, or are there still donor ecosystems that could hide material capability classes the current taxonomy misses?

## Verdict
Not complete. Coverage is now broad, but the remaining gap is no longer primarily isolated frameworks. It is **ecosystem-level capability evolution**: families of interoperating agent runtimes, portable skill/context layers, agent-to-agent protocols, self-evolving harnesses, and cross-project reliability evidence.

## Material donor classes surfaced

### 1. OpenClaw / Claw-family ecosystem
Current ecosystem comparisons show OpenClaw, Hermes, ZeroClaw, NanoClaw/NanoBot, IronClaw, CoPaw, PicoClaw, NullClaw, Moltis and related runtimes converging on common production concerns: session-state integrity, message-delivery semantics, plugin/skill extensibility, MCP reliability, sandboxing, provider fallback, token/cost observability, channel/gateway reliability and security hardening.

Donor value:
- treat *cross-project recurring pain* as stronger evidence than any one framework feature;
- message-delivery and subagent-completion integrity as first-class reliability contracts;
- session contamination/state corruption detection;
- workspace isolation and tool confinement;
- provider fallback and silent-failure detection;
- per-turn token/cost loop guards;
- plugin/skill security scanning with usable allowlists;
- channel/gateway reliability as a distinct operational problem.

Disposition: ADOPT the cross-project reliability lessons; inspect individual implementations only when a concrete consumer appears.

### 2. Hermes ecosystem maps, skill factories and skill evolution
Hermes ecosystem maps now contain not only plugins/MCPs but skill registries, skill factories, multi-agent bridges, cost-control plugins, operational playbooks, and automatic skill curation/evolution.

Donor value:
- curated ecosystem maps as living donor inventories;
- workflow-to-skill factories;
- skill dedupe/consolidation/evolution from session evidence;
- operator playbooks as reusable procedural knowledge;
- periodic curator jobs for skill-library hygiene.

Disposition: ADOPT mechanisms into Archives/Spellbooks/Memory Maintenance rather than adding new entities.

### 3. Agent2Agent (A2A) protocol
A2A is now a Linux Foundation open protocol for agent-to-agent discovery and collaboration. It complements MCP: MCP exposes tools/resources; A2A lets opaque agents discover one another, advertise skills/capabilities, negotiate interaction modalities, exchange artifacts, and manage long-running tasks without exposing private internal memory/tools.

Donor value:
- explicit Agent Cards/capability descriptors;
- agent discovery separate from tool discovery;
- long-running delegated task lifecycle;
- artifact exchange;
- authorization-aware agent discovery/calling;
- interoperability without sharing private internal state.

Disposition: PROTOTYPE as a future Ultron Bots/Ikonn interoperability donor. Do not add remote-agent federation without a real consumer and trust boundary.

### 4. A2A gateways/registries
Emerging gateways combine agent registration, discovery, access control and optional reverse-proxy execution.

Donor value:
- registry-only discovery versus proxy-mediated execution as separate modes;
- capability visibility controlled by policy;
- agent invocation grants independent of mere discovery;
- machine-readable capability metadata.

Disposition: ADOPT architecture principles into capability catalog and worker/delegation doctrine.

### 5. Portable context operating systems
Projects such as agent-context-os and filesystem-first agent OSs treat identity/project/state/session files, receipts, handoffs and skills as portable Git-backed artifacts with host-specific adapters.

Donor value:
- one portable semantic core with thin surface adapters;
- integrations declare reads/writes/destructive effects, confirmation gates, health checks and uninstall behavior;
- add at most one new trust boundary at a time;
- progressive disclosure of project/context state;
- one worktree per concurrent agent session;
- proposal/apply/receipt semantics for context mutation.

Disposition: ADOPT principles into Sanctum surface adapters, capability catalog and Compact & Handoff.

### 6. On-demand skill registries
Portable skill registries store a large skill library centrally and load only a tiny gateway/index at startup, fetching the selected skill on demand.

Donor value:
- avoid startup-context bloat from loading every spell/skill;
- fetch procedures only when triggered;
- version skills like code;
- one canonical source with multiple host adapters.

Disposition: ADOPT as Spellbook retrieval architecture. The full Spellbook need not be injected into every task context.

### 7. Self-evolving harness skills
Some projects implement explicit self-audit loops over config + logs, with risk tiers for what may be changed automatically versus reviewed or forbidden.

Donor value:
- periodic harness self-audit using actual run evidence;
- risk-tiered improvement authority;
- cross-discipline lookup lattice for unknown-unknown discovery;
- proposed changes separate from automatic promotion.

Disposition: ADOPT as Failure Harvest / Memory Maintenance / Web candidate flow; never grant blanket self-modification authority.

### 8. Cross-agent persistent memory services
New memory layers expose one shared memory service across Claude Code, Codex, Hermes, Cursor, OpenCode, Goose, Aider and other clients using hooks + MCP/REST.

Donor value:
- memory semantics can remain independent of the agent host;
- host hooks can capture/retrieve at reliable lifecycle boundaries;
- shared memory does not require shared private execution state;
- memory quality should be benchmarked and audited rather than assumed.

Disposition: WATCH/PROTOTYPE for future surfaces. Sanctum semantics remain authoritative over any storage backend.

## Completeness interpretation

The donor map is approaching **architectural saturation**, not internet completeness.

Most newly found agent systems now repeat capabilities Sanctum already covers:
- tools/MCP;
- skills/plugins;
- memory;
- hooks;
- subagents;
- durable sessions;
- provider routing;
- observability;
- sandboxing;
- scheduling.

The remaining high-value novelty is increasingly found in:
1. cross-project operational scars rather than headline features;
2. interoperability standards such as A2A;
3. retrieval/skill-distribution mechanics;
4. security/reliability details;
5. new adjacent disciplines outside the agent ecosystem.

Therefore broad random framework discovery should no longer be continuous. Use periodic Meta-Cerebro landscape sweeps or Prime Sense triggers when a new ecosystem, protocol, capability class or recurring user correction suggests the map changed materially.

## New anti-Hermes question

Before declaring a capability landscape complete, ask:

> What systems solve this problem without calling themselves what I am searching for, and what ecosystems/standards/marketplaces are evolving the capability faster than individual projects?

This applies recursively to Sanctum, software engineering, game development and project-specific donor research.
