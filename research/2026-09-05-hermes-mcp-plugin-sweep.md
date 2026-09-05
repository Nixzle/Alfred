# Hermes / MCP / Plugin Donor Sweep

Date: 2026-09-05
Mode: Cerebro + Expertise Forge / Mind Stone

## Objective

Scout Hermes Agent and the current plugin/MCP ecosystem for mechanisms that can materially upgrade Sanctum without importing another monolithic agent framework.

## Hermes Agent donor mechanisms

### Curated MCP catalog + per-tool filtering
Hermes can install approved MCP servers from a curated catalog, probe tool surfaces, and enable only selected tools. This is stronger than treating a connected server as an all-or-nothing capability.

Disposition: `ADOPT PATTERN`.

Sanctum translation: maintain a governed integration catalog; discover capabilities first, then separately decide which tools may be exposed on each surface/task.

### Plugin lifecycle hooks
Hermes plugins can attach to pre/post tool calls, pre/post model calls, session lifecycle, subagent completion, and gateway dispatch.

Disposition: `ADOPT PATTERN`.

Sanctum translation: implement high-value deterministic checks/telemetry at stable lifecycle boundaries rather than relying on prompt memory.

### Pluggable memory/context engines/providers
Hermes separates general plugins from memory providers, context-compression engines, and model providers.

Disposition: `ADOPT ARCHITECTURAL PATTERN`.

Sanctum translation: keep knowledge semantics canonical while allowing runtime backends/providers to be replaceable behind explicit contracts.

### Host-owned plugin LLM access
Hermes plugins can make structured LLM calls through host-owned credentials and trust gates rather than receiving raw credentials.

Disposition: `ADOPT PATTERN`.

Sanctum translation: extensions/workers should receive host-governed model/tool capability, not unrestricted secret material.

### Agent exposed as MCP server
Hermes can expose governed conversation/messaging operations to other MCP clients.

Disposition: `PROTOTYPE PATTERN`.

Sanctum translation: a surface may expose narrow Ultron operations to authorized clients without exporting private context or general authority.

### Skills Hub / procedural memory
Hermes treats reusable skills as progressive-disclosure capability documents and can learn/improve skills over time.

Disposition: `ADOPT CONFIRMATION`.

Sanctum already has Spellbooks/Archives and Fast Learn; donor reinforces low-friction candidate capture plus governed promotion rather than core prompt growth.

### Provider routing/fallback
Hermes supports many providers plus cost/quality routing and fallback.

Disposition: `ADOPT PRINCIPLE / PROTOTYPE`.

Sanctum translation: provider/model choice belongs in runtime profile and routing economics; fallback must preserve task/evidence compatibility rather than silently changing claim strength.

## MCP ecosystem donor mechanisms

### Official MCP Registry
Provides a machine-readable distribution/discovery layer for MCP servers with repository/package/version metadata.

Disposition: `ADOPT SOURCE CLASS` for integration scouting. Registry presence is not a trust decision.

### Smithery / large MCP registries
Large catalogs make it cheap to discover existing connectors for web, databases, SaaS, browser automation, research, and developer tools.

Disposition: `ADOPT DISCOVERY SOURCE`, `REJECT popularity-as-trust`.

### MCP policy middleware / server-side enforcement
Current MCP ecosystem work strongly supports a separate policy-enforcement point that decides whether a protected capability should be listed/read/executed for the authenticated actor and current parameters. Middleware implementations demonstrate allow/deny/approval policies and decision receipts.

Disposition: `ADOPT PRINCIPLE`, strengthens TVA/tool-boundary roadmap.

### MCP 2026 authorization/cache changes
Current MCP authorization guidance emphasizes audience/resource binding, short-lived tokens, PKCE and secure authorization flows. New cache metadata for tool/prompt/resource listing also reinforces cache-aware discovery rather than refetching static capability metadata constantly.

Disposition: `ADOPT GROUNDING` for future MCP integration implementations.

## Integration classes to scout instead of rebuild

When a real need appears, Cerebro should search current MCP/plugin ecosystems before greenfield integration work for:

- GitHub/repository operations;
- Slack/Discord/messaging;
- Google/Microsoft productivity;
- browsers/computer use;
- databases/data warehouses;
- vector/search/retrieval systems;
- observability/tracing/evals;
- policy/authorization/approval gateways;
- automation/workflow platforms such as n8n;
- documentation/context retrieval such as Context7;
- web/deep-search providers;
- memory backends;
- Home Assistant / device bridges;
- ticket/project-management systems.

## Adoption rule

For each integration candidate:

`native capability -> known connected plugin -> official/curated MCP -> broader registry -> custom adapter only by exception`

Then apply dependency trust, tool filtering, authority minimization, provenance, and donor-community checks.

## Failure mode to avoid

The existence of MCP makes capability acquisition easy enough to become dangerous. Tool count is not capability quality. A server exposing 100 tools should normally result in a smaller approved surface, not 100 new choices in every prompt.

## Outcome

Promoted general mechanisms to `archives/reliability-and-tool-ecosystem.md`. Mechanical provider installation remains surface/task-specific and is not implied by this research record.
