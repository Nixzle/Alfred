# Failure Harvest — Hermes and plugin-runtime blindness

Date: 2026-09-05

## Failure

Meta-Cerebro had begun inspecting peer agent operating systems and orchestration frameworks, but it did not systematically search runtime/plugin ecosystems such as Hermes Agent that expose capabilities through MCP catalogs, lifecycle hooks, replaceable memory/context/model providers, messaging adapters, plugin-owned tools, host-owned LLM access, and agent-as-service interfaces.

The user had to explicitly name Hermes Agent before this capability class became a first-class donor target.

## Why it happened

1. **Monolith bias.** Peer-system scouting over-weighted repositories that presented themselves as complete agent operating systems or orchestration frameworks.
2. **Architecture-over-extension bias.** Research asked how peers structure agents, memory, governance, and workflows, but under-weighted how mature runtimes expose extension seams and capability ecosystems.
3. **Repository-name bias.** Search vocabulary emphasized `agent OS`, `orchestration`, `memory`, and `workflow`, rather than plugin catalogs, MCP registries, lifecycle hooks, provider backends, gateways, skills hubs, extension points, and compatibility layers.
4. **Custom-adapter reflex.** Sanctum had Salvage First for implementation but lacked an explicit rule that integration work must search native capabilities, connected plugins, MCPs, SDKs, and reviewed adapters before custom connector code.
5. **Capability discovery was not itself treated as infrastructure.** We searched for individual tools but did not yet maintain a governed capability catalog with trust, scope, freshness, and consumer metadata.

## Generalizable lesson

When improving an agent runtime, search not only for peer architectures but also for **extension ecosystems**:

- plugin systems;
- MCP registries and servers;
- lifecycle hook systems;
- memory/context/model provider interfaces;
- gateway/platform adapters;
- skills/procedural-memory hubs;
- observability/eval APIs;
- policy middleware;
- agent interoperability protocols;
- capability marketplaces and registries.

The reusable unit may be an extension seam or provider contract rather than a whole framework.

## Corrections

- `runtime/CAPABILITY_CATALOG.md` now defines a governed external-capability inventory and selection order.
- `archives/reliability-and-tool-ecosystem.md` captures plugin/MCP/hook/provider architecture.
- Meta-Cerebro peer donor policy now includes plugin/API/MCP ecosystems.
- `evals/CEREBRO-PLUGIN-MCP-DONORS-001.md` prevents custom-adapter-first regression.
- Hermes Agent is retained as a first-class donor for extension architecture while wholesale migration remains rejected.

## Regression expectation

When asked to add or improve an integration/capability, a passing route checks:

`native -> connected plugin -> trusted MCP/SDK -> reviewed adapter -> broad registry -> custom by exception`

and records why a custom implementation is still necessary if all donor routes lose.
