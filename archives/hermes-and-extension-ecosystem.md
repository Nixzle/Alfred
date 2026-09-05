# Hermes and Extension-Ecosystem Architecture

Promoted: 2026-09-05

## Purpose

Absorb the strongest extension-system mechanisms from Hermes Agent and adjacent plugin/MCP ecosystems without replacing Sanctum's canonical orchestration, memory, governance, or surface authority model.

## Hermes mechanisms adopted

### 1. Extension seams are first-class
A mature agent runtime should expose stable extension seams rather than requiring core edits for every integration.

Useful extension classes include:

- general tools/plugins;
- lifecycle hooks;
- memory providers;
- context engines/compressors;
- model/provider backends;
- gateway/platform adapters;
- image/video backends;
- procedural skills;
- external MCP servers;
- agent-as-API/MCP surfaces.

Sanctum adopts the **pattern**, not Hermes' exact runtime structure.

### 2. Per-tool capability filtering
Connecting a provider does not mean every tool becomes available to every task. Capability exposure should be filtered by provider, tool, role, task, authority, and current consumer need.

### 3. Lifecycle-hook boundaries
Stable hook points are useful locations for deterministic observation/enforcement:

- pre/post tool;
- pre/post model;
- session start/end/reset/finalize;
- subagent completion;
- gateway dispatch;
- memory retrieval/write/promotion;
- effect commit/reconciliation.

Hooks should remain bounded, inspectable, and fail safely. Core business/orchestration logic should not disappear into opaque hook chains.

### 4. Replaceable provider contracts
Memory, context compression, and model routing should be provider contracts rather than hard-coded singleton implementations when there is a real need for replacement or comparison.

Sanctum semantics remain authoritative. A memory backend may store/retrieve data; it may not redefine promotion, retention, privacy, supersession, or authority rules.

### 5. Host-owned plugin model access
Third-party extensions that need model calls should use host-owned credentials, policy, cost controls, and structured-output validation where possible. Raw unrestricted provider secrets should not be handed to plugins by default.

### 6. Platform adapters without shared-authority illusion
One Ultron core may be surfaced through multiple clients/adapters, but identity does not imply shared permissions, memory scope, data authority, or effect authority. Each adapter re-probes local capability and authority state.

### 7. Agent-as-capability
Ultron may expose a narrow governed API/MCP surface to other authorized clients when useful. Expose explicit operations, not private context or unrestricted orchestration internals.

### 8. Skills and procedural memory
Hermes reinforces the value of reusable procedural capabilities as an extension class. Sanctum already uses Spellbooks; external skill packages may be donor candidates but remain subject to provenance, trust, scope, and local validation.

### 9. Provider routing and fallback
Provider choice may optimize quality, latency, cost, privacy, or availability. Fallback is useful when a primary provider fails, but a fallback route must preserve task requirements, privacy boundaries, and evidence scope. A fallback is a new runtime profile when materially different.

### 10. Prompt/context caching
Reusable, freshness-bounded prompt/context fragments may be cached when authority, version, and freshness are part of the key. Cache use must be visible to Watcher where material and bypassed for changed project/runtime state or explicit live verification.

## Broader donor mechanisms added by this sweep

### Governed memory transactions
Inspired by SuperLocalMemory-style reliability envelopes:

`admit -> apply -> verify -> compensate/erase -> completion receipt`

For consequential durable-memory writes, treat memory mutation as an operation with owners, projections/targets, verification, and failure recovery where the runtime supports it.

### Checked resource-bounded tool execution
Inspired by SkillEffect-style checked lowering:

- bounded resource contract;
- independently checked transformation/plan where practical;
- capacity/resource lease;
- postcondition verification;
- staged publication.

Use only for tool classes where resource exhaustion or unsafe whole-input handling is a material risk. Do not generalize into universal complexity.

## Status

This Archive is canonical doctrine. Actual plugin APIs, hook dispatchers, provider loaders, memory transactions, and resource-bounded execution remain surface/runtime implementation work until verified.
