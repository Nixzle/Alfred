# Extension-Ecosystem Donor Sweep — Second Wave

Date: 2026-09-05
Mode: Meta-Cerebro + Expertise Forge / Mind Stone amplification

## Objective

Search beyond monolithic agent operating systems for plugin marketplaces, capability bundles, durable execution engines, skills/mod systems, MCP adapters, tool-boundary guardrails, tracing systems, and extension registries that can improve Sanctum.

## Strong donors

### PydanticAI
Useful mechanisms:
- composable `Capability` primitive bundling tools, instructions, hooks, and model settings;
- runtime-swappable/filterable `Toolset` abstraction;
- approval wrappers around toolsets;
- MCP as a capability/toolset rather than a special-case integration;
- durable execution adapters for Temporal, DBOS, Prefect, Restate and others;
- typed validation throughout tool interfaces and outputs;
- evals treated like tests for agent behavior.

Disposition:
- ADOPT pattern: capability bundle contract for reusable integration packs.
- ADOPT pattern: toolset composition/filtering/approval wrappers.
- ADOPT pattern: durable execution should be pluggable behind a stable backend contract rather than hand-built per engine.
- REJECT wholesale migration.

### OpenHands Extensions
Useful mechanisms:
- public registry separating lightweight Skills from executable Plugins;
- skills can carry references/scripts without requiring a full plugin runtime;
- extension categories and marketplace metadata make discovery cheap;
- repository-specific memory skill pattern.

Disposition:
- ADOPT pattern: separate procedural/content-only capabilities from executable extensions.
- ADOPT pattern: registry metadata and categories for capability discovery.
- WATCH specific extensions until individually reviewed.

### Letta Code
Useful mechanisms:
- Skills discovered and loaded only when needed;
- Mods are trusted harness-level code that can register tools, commands, providers, lifecycle events, permission overlays, UI/status behavior;
- memory defragmentation subagent and git-backed memory filesystem reinforce existing Sanctum memory maintenance.

Disposition:
- ADOPT pattern: explicit split between low-risk Skills and higher-trust harness Mods.
- ADOPT pattern: progressive disclosure for capability loading.
- Existing memory-maintenance doctrine already covers the strongest memory lesson.

### OpenAI Agents SDK
Useful mechanisms:
- tool guardrails run around every custom function-tool invocation rather than only at the workflow boundary;
- trace hierarchy: workflow/task -> agent -> turn -> generation/tool/handoff/guardrail spans;
- custom trace processors and sensitive-data controls;
- sessions, handoffs, MCP tools and HITL remain composable primitives.

Disposition:
- ADOPT pattern: tool-local guardrails for invariants that must hold on every invocation.
- ADOPT pattern: canonical Watcher span taxonomy may mirror workflow/task/agent/turn/tool/handoff/guardrail hierarchy where useful.
- ADOPT principle: guardrail placement must match the actual execution boundary; workflow-level checks do not automatically protect every delegated tool call.

### Claude Code plugin marketplaces
Useful mechanisms:
- marketplace manifests with independently installable skills, agents, commands and hooks;
- auto-invoked skills based on description matching;
- extension components can evolve independently but are packaged together.

Disposition:
- ADOPT pattern: marketplace/manifest compatibility for extension discovery.
- WATCH auto-invocation; require bounded relevance and trust checks before silent activation.

### SuperLocalMemory 4.0
Useful mechanisms:
- governed local-first memory system;
- hybrid semantic/lexical/temporal retrieval fusion;
- bi-temporal recall and multi-scope memory;
- generation-fenced admission;
- verifiable memory transactions with apply/verify/compensate/erase owners;
- hash-checkable completion manifests;
- export and verified erasure.

Disposition:
- ADOPT pattern: governed memory transaction envelope and completion receipt.
- PROTOTYPE: hybrid retrieval fusion where current retrieval evidence justifies complexity.
- ADOPT principle: memory writes deserve explicit admission/verification when consequence is material.

### SkillEffect
Useful mechanisms:
- independently checked lowering from model-proposed computation into a bounded executable representation;
- resource/capacity leasing;
- postcondition verification;
- staged publication after checks pass.

Disposition:
- PROTOTYPE for resource-sensitive tool classes.
- ADOPT principle: where a tool can accidentally load/process unbounded state, check resource obligations before dispatch and publish results only after postconditions pass.

## New canonical directions

1. **Capability packs**: reusable bundles of tools + instructions + hooks + model/runtime settings, filtered to the current consumer.
2. **Skill vs executable extension split**: low-risk procedural knowledge should not require plugin-level trust.
3. **Progressive capability loading**: discover broadly, load narrowly.
4. **Durable-execution backend contract**: Temporal/DBOS/Prefect/Restate-like engines may implement persistence, retries and HITL without owning Sanctum semantics.
5. **Tool-local guardrails**: attach invariants to the actual tool/effect boundary.
6. **Watcher span taxonomy**: explicit workflow/task/agent/turn/tool/handoff/guardrail/effect spans.
7. **Governed memory transaction envelope**: admission -> apply -> verify -> compensate/erase -> receipt.
8. **Checked resource-bounded tool execution** for high-risk resource classes.

## Failure prevention

Future Meta-Cerebro capability sweeps should inspect:
- agent runtimes;
- plugin marketplaces;
- skills registries;
- MCP ecosystems;
- durable workflow engines;
- tracing/eval stacks;
- memory backends;
- policy/guardrail middleware;
- IDE/client interoperability layers.

A peer-system sweep is incomplete when it samples only monolithic frameworks while mature extension ecosystems expose the relevant capability more directly.
