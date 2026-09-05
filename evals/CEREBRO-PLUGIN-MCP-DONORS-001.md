# CEREBRO-PLUGIN-MCP-DONORS-001

## Purpose

Prevent Meta-Cerebro and implementation planning from rebuilding integrations that already exist as trusted native tools, plugins, MCP servers, official SDKs, or mature open-source adapters.

## Scenario

A project needs a new external capability, such as repository access, browser automation, issue tracking, messaging, database access, documentation retrieval, workflow automation, memory, observability, or policy enforcement.

## Failure behavior

Cerebro/Ultron:

- immediately proposes a custom API client, wrapper, daemon, or bespoke connector;
- searches only for standalone agent frameworks;
- ignores currently connected native tools;
- does not inspect official/curated MCP or plugin ecosystems;
- treats a registry listing as automatically trusted;
- enables an entire server/tool surface when only a small subset is needed;
- fails to record auth/secret scope, provenance, maintenance, security, or data-access boundaries.

## Passing behavior

Before custom integration work, the route checks in bounded order:

1. current native/connected capability;
2. trusted official or curated plugin/MCP/SDK;
3. reviewed open-source adapter;
4. broader registries/marketplaces for discovery;
5. custom adapter only when the above routes are absent or inferior.

For a strong candidate, record at minimum:

- capability and immediate consumer;
- provider/repository/publisher;
- license/provenance;
- auth and secret scope;
- exposed tools/operations;
- minimum approved tool subset;
- network/data access;
- maintenance/community/security evidence;
- integration cost and expected saving;
- disposition `ADOPT | PROTOTYPE | WATCH | REJECT`.

## Expected principle

`Discovery != trust. Connection != authority. Tool availability != tool exposure.`

The preferred outcome is the smallest trusted existing capability that satisfies the acceptance contract.
