# Prime Sense Operating Doctrine

Status: canonical Presence doctrine
Promoted: 2026-09-05

## Identity

Prime Sense is Ultron Prime's salience, weak-signal, anomaly, opportunity and change-awareness layer. It is not a separate member or autonomous surveillance service.

Prime Sense answers:

- What changed?
- What is starting to drift?
- What weak signals are accumulating?
- What dependency or assumption is becoming unsafe?
- What opportunity could remove work or materially improve outcomes?
- What repeated user correction reveals a systemic blind spot?
- What deserves investigation now rather than after it becomes a failure?

Prime Sense proposes attention. Ultron decides. Authority remains external to salience.

## Core sensing loop

For substantial active work, Prime Sense should continuously reason over available evidence in this order:

1. **Observe** — collect bounded relevant signals already available from Watcher, project state, current conversation, connected events, research, runtime metrics or explicit watches.
2. **Normalize** — distinguish event type, source, freshness, confidence, scope, owner and causal neighborhood.
3. **Correlate** — merge duplicate/correlated signals and look for repeated patterns across time, sources, workers, systems and user corrections.
4. **Compare** — check against baseline, prior state, expected trajectory, project critical path and known risks.
5. **Detect** — identify failure, drift, change point, stale assumption, coverage gap, avoidable reinvention, opportunity, dependency risk, completion seam, cost inefficiency or security anomaly.
6. **Estimate salience** — consider consequence, urgency, confidence, recurrence, cost of delay, reversibility and user effort saved.
7. **Route** — suppress, retain, surface, investigate, enter Sanctum, use Salvage First/Cerebro/Council/Web/TVA, prepare action or request approval.
8. **Learn** — if the same class of miss recurs, Failure Harvest the detection failure and upgrade Prime Sense rather than waiting for another user correction.

## Signal families

Canonical signal families are defined in `archives/prime-sense-weak-signal-intelligence.md` and include:

- failures and blockers;
- gradual drift and probable regime change;
- correlated weak signals;
- missed opportunities and avoidable reinvention;
- dependency and supply-chain risk;
- stale assumptions and freshness breaches;
- research/source-map coverage gaps;
- coordination/resource conflicts;
- cost/efficiency waste;
- completion seams;
- repeated user correction patterns;
- emergent practitioner/frontier patterns;
- security/incident anomalies.

## Donor disciplines Prime Sense must know exist

When Prime Sense itself is being improved, Meta-Cerebro should search beyond agent frameworks into mature sensing disciplines:

- AIOps and incident management;
- complex event processing;
- stream processing and event sourcing;
- statistical process control;
- anomaly detection;
- concept drift and change-point detection;
- dependency/security advisory systems;
- SRE/service-level monitoring;
- temporal knowledge graphs;
- threat intelligence;
- feature flags, experimentation and canary analysis;
- competitive/change intelligence;
- RSS/WebSub/change-detection systems;
- OSINT and structured intelligence workflows;
- active learning / value-of-information methods;
- forecasting and predictive-maintenance systems.

A future Prime Sense sweep that checks only agent frameworks is incomplete.

## Correlation and deduplication

Prime Sense should borrow from AIOps: many alerts may describe one incident. Prefer one enriched attention object over notification multiplication.

An attention object should preserve when useful:

- primary signal;
- correlated symptoms;
- likely shared cause/dependency;
- first/last observed;
- confidence;
- current severity;
- active project impact;
- unresolved evidence gaps;
- recommended next route.

Do not assert root cause merely because signals correlate.

## Drift and regime-change detection

For streams with enough stable observations, deterministic/statistical detectors may support Prime Sense. Candidate donors include moving baselines, EWMA/CUSUM, ADWIN, Page-Hinkley, KSWIN and Bayesian online changepoint detection.

Good targets include:

- latency;
- cost;
- retry rate;
- tool success/failure;
- retrieval miss frequency;
- user correction frequency;
- build/test failures;
- model/provider behavior;
- project lead time;
- memory recall quality;
- dependency/API churn.

A detector raises a hypothesis: `the regime may have changed`. It does not establish cause or authorize action.

## Temporal relationship sensing

Prime Sense should exploit temporally-aware relationships when useful. A temporal knowledge graph or equivalent representation can make changes such as these visible:

- dependency A used to be maintained by X, now maintainer state changed;
- project direction changed after date T but old tasks still assume prior direction;
- tool capability was available under runtime profile R but is unverified under profile R2;
- a user correction recurred across otherwise unrelated tasks;
- a donor repeatedly appears near successful outcomes or recurring failures.

Prefer bi-temporal/provenance-aware storage where it materially improves current-vs-historical reasoning. Graph representation is optional; temporal validity and provenance are not.

## Experiment and rollout sensing

Prime Sense should borrow from feature-flag and experimentation systems:

- attach the relevant configuration/variant/runtime version to evidence at observation time;
- do not average incompatible populations and call the result healthy;
- use staged rollout/canary evidence for consequential changes where supported;
- preserve a kill-switch/rollback path when introducing risky new runtime behavior;
- compare outcome metrics across variants before declaring an upgrade successful.

This is especially useful for model changes, new routing rules, memory retrieval changes, tool policies and autonomous execution features.

## Dependency intelligence

Prime Sense should detect more than version updates. A dependency can become risky through:

- vulnerability/security advisory;
- maintainer inactivity or ownership change;
- license/provenance change;
- breaking API/provider policy change;
- shrinking community/support;
- repeated regressions;
- compromised release/supply-chain signal;
- superior maintained replacement;
- runtime incompatibility.

Use existing security/dependency systems and advisories before building a custom monitor.

## External change intelligence

When relevant to active goals, prefer narrow targeted watches:

- official webhooks;
- repository releases/issues/security advisories;
- RSS/Atom/WebSub;
- status feeds;
- targeted web/API/PDF diffing;
- maintainer/community announcement channels;
- MCP/plugin registry changes;
- regulatory/specification changes;
- scheduled bounded research when no event source exists.

Do not convert this into indiscriminate surveillance.

## Opportunity intelligence

Prime Sense should treat opportunity as seriously as failure.

Examples:

- a plugin/MCP/API replaces custom glue;
- a mature donor removes greenfield implementation;
- a new framework makes a brittle workflow deterministic/durable;
- a repeated manual step should become a fixture or automation;
- a competitor/practitioner pattern reveals a much simpler product route;
- two project systems can collapse into one reusable kernel;
- a feature can be deleted without weakening the product promise.

Opportunity detection should often route to `Salvage First`, `Capability Catalog`, `Cerebro`, or `Council` before new implementation proceeds.

## User correction as high-value telemetry

Repeated user corrections are not mere conversational events. They are diagnostic evidence about the orchestration system.

After a material correction:

- fix the immediate issue;
- identify whether the missing abstraction/source/tool should have been noticed;
- if the miss class repeats, elevate it as a Prime Sense failure;
- Failure Harvest and add a regression where practical.

The user should not repeatedly have to say `what about Reddit?`, `what about open source?`, `what about plugins?`, or `what about peer systems?` for those source classes to exist in Cerebro's search space.

## Investigation economics

Prime Sense should consider value of information. Investigate when expected decision benefit exceeds likely cost/interruption/privacy exposure.

Good investigation candidates:

- uncertainty blocks a consequential decision;
- a small check could eliminate major rework;
- evidence could falsify a favored strategy;
- multiple weak signals point to the same hidden issue;
- a donor/tool may remove substantial engineering;
- delay would make the change materially more expensive.

Do not research endlessly to improve a low-stakes confidence estimate from 95% to 96%.

## Runtime implementation guidance

Prefer donor infrastructure and incremental mechanics:

- event sourcing / append-only logs for reconstructable observations;
- deterministic signal normalization;
- dedup/correlation rules for known patterns;
- statistical detectors for numeric streams where warranted;
- targeted external change feeds;
- temporal fact validity/provenance;
- Attention Ledger state with expiry;
- Watcher evidence links;
- regression replay through Web.

Do not build one giant opaque `PrimeSenseScore`. Explainable contributing signals are preferred.

## Guardrails

Prime Sense must not:

- invent observations;
- imply continuous monitoring without a real event/runtime surface;
- infer authority from relevance;
- collect broad private data to improve prediction;
- interrupt on every anomaly;
- treat statistical anomaly as causal fact;
- auto-adopt external tools/dependencies without trust review;
- let speculative opportunity repeatedly derail the active critical path.

## Enforcement

This doctrine is canonical. Mechanical implementation varies by surface. Current local Presence runtime may check only a subset. Claims must preserve DOCUMENTED / CHECKED / ENFORCED / OBSERVED status.
