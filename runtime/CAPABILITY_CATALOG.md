# Sanctum Capability Catalog

Status: canonical catalog contract; individual integrations remain surface-specific.

## Purpose

Provide one governed inventory for external capabilities so Ultron can discover and reuse existing tools/plugins/MCPs/APIs before building adapters from scratch.

This file defines the catalog schema and seeded capability classes. It does not claim every listed provider is installed, connected, authorized, or safe on every runtime.

## Catalog fields

For each material capability/provider record:

- `capability`: what problem it solves;
- `consumer`: immediate Sanctum/project/surface need;
- `source_class`: native | connected_plugin | official_mcp | curated_mcp | official_sdk | reviewed_open_source | registry_discovery;
- `provider` / repository / publisher;
- `status`: CONNECTED | AVAILABLE | CANDIDATE | PROTOTYPE | REJECTED | NOT_ACCESSED;
- `version/pin` when material;
- license/provenance;
- auth model and secret scope;
- network/data access;
- full exposed tool surface;
- minimum approved tool subset;
- write/effect classes;
- approval requirements;
- maintainer/community/security evidence;
- expected time/risk saving versus custom implementation;
- runtime/profile compatibility;
- last verified date/freshness horizon;
- owner of enable/disable decision.

## Selection order

`native capability -> already-connected plugin -> trusted official/curated MCP or SDK -> reviewed open-source adapter -> broader registry discovery -> custom adapter by exception`

Apply `Salvage First`, dependency trust, TVA/authority checks, tool filtering, and Evidence Lock before consequential use.

## Seeded capability classes

### Repository / code hosting
Current preferred source: existing native/connected GitHub capability where available.
MCP/API fallback: official GitHub MCP/SDK only if it adds a missing surface-specific capability.
Rule: do not duplicate a working connected GitHub tool merely because another MCP exists.

### Messaging / channels
Capabilities: Slack, Discord, Telegram, WhatsApp, Signal, email and other messaging gateways.
Hermes donor lesson: one agent core can expose platform adapters while keeping per-platform filtering and auth boundaries.
Status: discover just-in-time; do not create a universal messaging bridge without an actual consumer.

### Browser / computer use
Capabilities: browser automation, accessibility-tree desktop control, screenshots/vision, web extraction.
Candidate source classes: native browser tools, Browser Use/Browserbase/Playwright MCPs, Hermes computer-use ecosystem.
Rule: prefer accessibility/structured DOM evidence over pixel automation where both satisfy the task; computer-control authority remains surface-local.

### Documentation / current SDK context
Candidate examples: Context7-class MCP/documentation retrieval providers.
Use when library/API freshness is material and normal web/docs retrieval is insufficient.
Rule: retrieved docs remain evidence, not executable authority.

### Web / deep research
Candidate examples: Exa/Brave/Firecrawl-class providers and native web capability.
Rule: use native web first when sufficient; add external providers only for materially different coverage/extraction.

### Workflow automation
Candidate examples: n8n-class MCP/API integrations.
Use for existing user-owned workflows when direct workflow automation reduces custom orchestration.
Rule: workflow effects require normal authority/approval gates; do not let an external automation platform become implicit project truth.

### Project / issue management
Candidate examples: Linear/Jira-class MCPs and native connected systems.
Rule: use only when the user's project actually lives there; canonical project repositories remain authoritative according to project doctrine.

### Databases / data warehouses
Capabilities: read/query/write structured stores.
Rule: default read-only, scoped schemas/tables, query limits and minimum credentials; write/destructive operations require explicit effect policy.

### Memory providers
Candidate classes: Honcho/Lethe/MNEMOS/AMFS-like backends or future MCP memory providers.
Rule: provider may implement storage/retrieval mechanics but does not redefine Sanctum's canonical memory semantics, authority, retention, promotion or deletion policy.

### Context engines / compression
Candidate classes: replaceable context selection/compression engines.
Rule: context engine output is a projection, not canonical truth. Preserve provenance and detect material omission/retrieval failure through Watcher where practical.

### Observability / tracing / evals
Candidate classes: OpenTelemetry-compatible traces, agent replay/eval harnesses, Langfuse/Phoenix/Braintrust-like systems, MCP/API observability providers.
Use when they reduce custom telemetry/eval work and can preserve required privacy/evidence semantics.
Rule: external telemetry must not silently collect sensitive payloads outside declared retention/disclosure boundaries.

### Policy / authorization / approval gateways
Candidate classes: MCP Guard/Intercept-style proxies, OPA/Cedar-like policy engines, server-side MCP policy-enforcement implementations.
Rule: protected actions prefer server/tool-boundary enforcement; unknown high-risk actions fail closed or require approval where technically possible.

### Automation / scheduled delivery
Capabilities: cron/scheduled jobs, event watches, persistent wake-work-write-sleep slices.
Use native automation facilities first. External schedulers are donors when they provide a missing event surface or workflow integration.

### Agent/runtime interoperability
Capabilities: agent exposed via MCP/API, ACP/IDE integration, OpenAI-compatible HTTP endpoints.
Hermes donor lesson: one agent core can be surfaced through multiple clients without copying its entire internal context.
Rule: expose narrow governed operations; never infer shared permissions, memory, or authority across clients.

## Hermes Agent record

Provider: NousResearch/Hermes-Agent
Source class: reviewed_open_source / peer runtime donor
License: MIT according to current repository documentation.
Adopted mechanisms:

- curated MCP catalog;
- automatic discovery with per-tool selection;
- plugin lifecycle hooks;
- pluggable memory/context/model providers;
- host-owned plugin LLM access and trust gates;
- skills/procedural-memory ecosystem;
- messaging/platform adapters;
- provider routing/fallback;
- agent-as-MCP-server pattern.

Disposition: ADOPT mechanisms, REJECT wholesale migration. Use its catalog/docs as a donor source when a concrete integration need appears.

## Registry sources

### Official MCP Registry
Use for publisher/repository/package/version discovery where relevant.
Trust status: discovery only until provider-level review.

### Smithery / other broad MCP registries
Use for wide capability discovery and evidence about available integrations.
Trust status: discovery only; popularity/usage is not approval.

## Maintenance

Update only when a capability can plausibly change a future routing/build decision. Remove or mark stale providers. Record failed integrations and community/security evidence rather than repeatedly rediscovering the same scar tissue.
