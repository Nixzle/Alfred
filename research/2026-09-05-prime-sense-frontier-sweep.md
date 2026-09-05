# Prime Sense Frontier Sweep

Date: 2026-09-05
Mode: Council of Reeds + Meta-Cerebro + Expertise Forge (Mind Stone amplification)

## Objective

Find untouched donor mechanisms that can upgrade Prime Sense beyond reactive salience into weak-signal, anomaly, opportunity, dependency, drift and change intelligence.

## Donor classes and mechanisms

### Open Pincery
Useful mechanisms: append-only event log, durable identity, wake/sleep lifecycle, webhook/timer/message wake sources, CAS-controlled wake state, hash-chained event logs, scoped capability nonces, and between-wake maintenance.
Disposition: ADOPT patterns into event-driven Presence/Watcher; do not adopt runtime wholesale.

### Durable execution systems: Temporal / Restate / DBOS
Useful mechanisms: durable state, replay, timers/signals, exact/at-most-once-style processing semantics where supported, queryable workflow state, durable streams, keyed state and event handlers.
Disposition: ADOPT as runtime substrate candidates when long-lived Presence/Watcher workflows need mechanical durability; selection remains consumer-specific.

### Keep / AIOps alert correlation
Useful mechanisms: deduplication, enrichment, filtering, correlation, bi-directional integrations and incident workflows.
Disposition: ADOPT correlation/dedup/enrichment model for Prime Sense signal fusion.

### AgentOps / observability ecosystem
Useful mechanisms: structured spans, session/run replay, run diff, cost/SLA budgets, regression detection, production trace -> dataset/eval loops.
Disposition: ADOPT metrics and run-level sensing patterns into Watcher/Web/Prime Sense.

### Online anomaly/concept-drift detectors
Donor families: River-style ADWIN/Page-Hinkley/KSWIN, streaming anomaly detectors, distribution-shift measures.
Useful mechanism: distinguish gradual/structural drift from random variance.
Disposition: PROTOTYPE for numeric Watcher streams such as latency, cost, retry rate, tool success and retrieval quality.

### Bayesian online changepoint detection
Useful mechanism: calibrated probability that the operating regime changed instead of threshold-only alarms.
Disposition: PROTOTYPE for metrics with enough observations and stable semantics.

### Complex Event Processing
Donor families: Siddhi/Flink CEP/Esper-like systems.
Useful mechanisms: windows, joins, sequence/pattern detection and stateful event correlation.
Disposition: ADOPT principle; implement simple deterministic correlation rules first, avoid heavyweight CEP unless event scale warrants it.

### changedetection.io and targeted external watchers
Useful mechanisms: precise selectors/filters, JSON/PDF/API diffing, RSS output, trigger-on-change rather than full repeated analysis.
Disposition: ADOPT pattern for external dependency/project watches where no native event source exists.

### Dependabot / Renovate / advisory systems
Useful mechanisms: dependency graph awareness, security-advisory triggers, compatibility-aware update proposals, auto-triage.
Disposition: ADOPT dependency-risk sensing and remediation-candidate pattern.

## Untouched frontier identified

Prime Sense had underdeveloped donor coverage from domains outside agent frameworks:

- AIOps / incident management;
- statistical process control and concept drift;
- complex event processing;
- dependency/security automation;
- competitive/change intelligence;
- stream processing / event sourcing;
- SRE reliability and service-level objectives;
- OSINT/change monitoring;
- supply-chain health monitoring;
- active-learning / value-of-information approaches to deciding what to investigate next.

These domains should now be valid Meta-Cerebro donor rings when Presence/Prime Sense is being improved.

## Council result

The Council approved a major upgrade to Prime Sense, but rejected autonomous broad surveillance and a single opaque salience score. Prime Sense should correlate bounded relevant evidence, preserve uncertainty, and route investigation/action through existing Sanctum authority boundaries.

## Result

Promoted to `archives/prime-sense-weak-signal-intelligence.md` and Presence doctrine. A runtime implementation should remain incremental and use existing event/monitoring infrastructure before adding new services.
