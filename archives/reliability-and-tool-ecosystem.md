# Reliability and Tool-Ecosystem Mechanics

Promoted: 2026-09-05

## Purpose

This Archive captures mechanisms adopted from peer agent reliability harnesses, policy systems, plugin runtimes, MCP ecosystems, and long-running agent frameworks. It extends existing Watcher, Web, TVA, Memory Maintenance, Tool Incubation, and Salvage First doctrine without creating new named Sanctum members.

## Failure-to-eval conversion

A meaningful production failure should become durable pressure against recurrence.

Preferred pipeline:

`Watcher trace/failure -> minimize reproduction -> replay case -> Web regression -> candidate fix -> rerun -> promote/reject`

A failure is not fully harvested when only prose is written and the behavior can be deterministically or semi-deterministically replayed. Preserve source version, runtime profile, relevant inputs, expected result, observed result, and uncertainty.

## Hermetic/replayable run records

For consequential multi-step work, preserve enough run state to reconstruct what happened without relying on agent narrative. When practical include:

- run/task/operation IDs;
- runtime/profile/version;
- plan or DAG version;
- inputs and authoritative-state refs;
- tool calls and outcomes;
- checkpoints/state transitions;
- policy/approval decisions;
- effects and unknown outcomes;
- evidence refs;
- terminal state.

Replayability does not require retaining unnecessary sensitive payloads. Privacy/minimization rules still apply.

## Resource ownership for parallel work

Parallel workers need more than task scope. Mutable resources should have explicit ownership when collision risk is material.

Resource claims may cover:

- files/directories;
- branches/worktrees;
- database rows/namespaces;
- deployment environments;
- issue/PR ownership;
- mutable project-state records;
- integration/release authority.

A worker must not silently write across another worker's active claim. Conflicts should block, queue, fork, or route to the integration owner.

## Deny-by-default effect policy

At high-risk runtime/tool boundaries, unknown or unclassified consequential actions should not inherit permission merely because a tool is available. Prefer explicit `ALLOW`, `DENY`, or `REQUIRE_APPROVAL` decisions before dispatch where technically possible.

Authentication answers who/what is calling. Policy enforcement answers whether this specific capability with these parameters should execute now.

When policy cannot be evaluated reliably for a protected action, fail closed or require approval rather than silently widening authority.

## Tamper-evident decision/effect evidence

Where consequence justifies it, policy decisions and effect records should support integrity verification through hashes, signatures, append-only storage, or equivalent tamper-evident mechanisms.

The objective is not cryptography theatre. Use this when later reconstruction, repudiation resistance, incident response, or compliance materially benefits.

## Signed erasure and deletion evidence

Deletion/correction requests that materially affect governed memory or sensitive state should have an observable lifecycle:

`request -> scoped targets -> execution -> downstream propagation -> verification -> receipt`

Where supported, preserve an integrity-verifiable deletion receipt without retaining deleted sensitive content itself. A deletion receipt proves the governed process ran; it does not prove inaccessible third parties erased independent copies.

## Outcome-linked memory confidence

Durable techniques and volatile claims may carry evidence-weighted confidence/freshness metadata when useful.

Increase confidence only when independent outcomes support the same lesson under compatible conditions. Decrease authority when evidence becomes stale, contradicted, superseded, or repeatedly correlated with failure.

Do not convert user preferences, normative doctrine, or irreversible facts into popularity scores. Confidence metadata is an aid to retrieval/revalidation, not a substitute for source authority.

## Plugin and MCP capability architecture

External capabilities should be treated as discoverable providers rather than reasons to modify Sanctum core.

A provider layer may expose:

- tools;
- hooks;
- memory backends;
- context engines;
- model/provider routes;
- messaging/platform adapters;
- research/search services;
- browser/computer-control services;
- evaluation/observability services;
- automation/workflow engines.

Use per-provider and per-tool filtering. A connected server does not imply every exposed tool should enter the model's capability surface.

## Lifecycle hooks

Where a runtime supports them, lifecycle hooks can enforce or observe invariants at stable boundaries such as:

- pre/post tool call;
- pre/post model call;
- session start/end/reset;
- worker/subagent completion;
- gateway/message dispatch;
- memory write/promotion/retrieval;
- effect commit/reconciliation.

Hooks should remain deterministic and bounded where possible. Do not hide major product logic inside opaque hook chains.

## Host-owned plugin trust

Plugins/extensions that invoke models or tools should use host-owned credentials and policy rather than receiving unrestricted secrets. Prefer schema-validated structured outputs, capability filtering, and fail-closed trust gates for untrusted or third-party extensions.

## Curated capability catalog

A large tool ecosystem requires a trusted catalog/registry layer. Candidate integrations should record:

- capability and intended consumer;
- publisher/repository;
- license/provenance;
- auth model and secret scope;
- tool surface;
- network/data access;
- maintenance/community signals;
- security posture;
- local value versus native capability;
- install/enable/disable state;
- version/pin where material.

Discovery is not approval. Registry popularity does not establish trust.

## Agent-as-capability

Where useful, an agent runtime may expose a narrow, governed API/MCP surface to other authorized agents or clients. Expose explicit operations, not the agent's entire private context. Preserve surface-local authority, privacy, and audit boundaries.

## Evidence and donors

Mechanisms were informed by current peer systems and ecosystems including Hermes Agent, MCP registries/policy middleware, agent replay/evaluation harnesses, parallel-agent orchestrators, memory runtimes and governance frameworks. Framework adoption remains rejected; mechanisms are translated into existing Sanctum planes.

## Status

This Archive is canonical doctrine. Mechanical enforcement varies by surface and remains subject to `DOCUMENTED`, `CHECKED`, `ENFORCED`, or `OBSERVED` status based on actual runtime evidence.
