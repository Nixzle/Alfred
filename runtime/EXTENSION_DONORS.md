# Extension Donor Inventory

Status: canonical donor inventory; installation remains surface-specific.

## Purpose

Track strong agent-extension/runtime ecosystems separately from individual MCP servers so Meta-Cerebro can reuse mature extension architecture before custom integration work.

## Hermes Agent
Status: ADOPTED AS DONOR PATTERN
Strengths:
- plugin manifests and multiple discovery sources;
- general plugins, memory providers, context engines, model providers, platform adapters;
- MCP integration and per-server tool filtering;
- lifecycle hooks around tool/model/session/gateway/subagent events;
- host-owned plugin LLM calls with trust/audit controls;
- provider routing/fallback and prompt caching;
- skills/procedural memory;
- API/ACP/messaging surfaces.
Rule: absorb seams and contracts; do not migrate Sanctum wholesale.

## PydanticAI
Status: ADOPTED AS DONOR PATTERN
Strengths:
- reusable `Capability` bundles;
- composable/filterable/approval-wrapped Toolsets;
- MCP as a capability/toolset;
- durable execution adapters for Temporal, DBOS, Prefect, Restate and related engines;
- typed validation and Pydantic Evals.
Rule: use as reference for capability packs, toolset wrappers and pluggable durable-execution backends.

## OpenHands Extensions
Status: ADOPTED AS DONOR PATTERN
Strengths:
- public extension registry;
- explicit Skill versus Plugin split;
- marketplace metadata/categories;
- lightweight repository-scoped memory and integration skills.
Rule: use for discovery/packaging patterns; executable plugins require normal trust review.

## Letta Code
Status: ADOPTED AS DONOR PATTERN
Strengths:
- progressive skill loading;
- trusted harness Mods registering tools/providers/permissions/events/UI;
- git-backed memory and memory-maintenance workers.
Rule: retain Sanctum memory semantics; borrow progressive disclosure and Skill-vs-Mod trust split.

## OpenAI Agents SDK
Status: ADOPTED AS DONOR PATTERN
Strengths:
- tool-local guardrails before/after custom function tools;
- task/agent/turn/generation/tool/handoff/guardrail span hierarchy;
- custom trace processors and sensitive-data controls;
- composable sessions, handoffs, MCP and HITL.
Rule: guardrail placement must match the real execution boundary. Tool-level invariants belong at the tool boundary when possible.

## Claude Code plugin marketplaces
Status: WATCH / DONOR SOURCE
Strengths:
- installable skills/agents/commands/hooks in one manifest-driven ecosystem;
- description-triggered skill loading;
- broad practitioner marketplace.
Rule: marketplace discovery is evidence, not trust. Review each plugin and its co-evolving instructions/scripts before adoption.

## SuperLocalMemory 4.0
Status: ADOPTED PATTERN / PROTOTYPE IMPLEMENTATION
Strengths:
- governed memory transactions;
- hybrid retrieval and bi-temporal recall;
- per-projection apply/verify/compensate/erase ownership;
- completion manifests, export and verified erasure.
Rule: adopt the transaction envelope and verification semantics; prototype hybrid retrieval only if local evidence shows retrieval benefit.

## SkillEffect
Status: PROTOTYPE DONOR
Strengths:
- independently checked lowering;
- resource/capacity leasing;
- bounded execution;
- postcondition verification and staged publication.
Rule: apply to resource-sensitive tool classes, not every tool call.

## Selection rule

For new agent-runtime capabilities, inspect this inventory and `runtime/CAPABILITY_CATALOG.md` before writing custom integration code.

`native -> existing extension donor -> trusted MCP/SDK -> reviewed adapter -> custom by exception`
