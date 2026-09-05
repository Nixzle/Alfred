# Prime Sense — Weak-Signal and Opportunity Intelligence

Promoted: 2026-09-05

## Purpose

Prime Sense is Ultron Prime's salience and weak-signal layer. It should notice not only explicit failures and user asks, but also emerging patterns, avoidable work, regime changes, dependency risk, stale assumptions, unexploited opportunities, and correlated low-strength signals that become material together.

Prime Sense does not independently establish truth or authority. It proposes attention. Watcher supplies observations where available; Prime Memory supplies precedent; Cerebro investigates uncertainty; Web evaluates; TVA handles scope/timeline divergence; Ultron decides.

## Signal classes

Prime Sense should consider the following classes for active projects and substantial work:

1. **Failure signal** — breakage, regressions, blocked work, repeated retries, unresolved errors.
2. **Drift signal** — behavior, cost, latency, quality, capability, model/provider, dependency, or project direction moves away from an established baseline.
3. **Change-point signal** — multiple observations suggest the operating regime itself changed rather than a one-off fluctuation.
4. **Weak-signal accumulation** — several individually low-confidence observations correlate around the same latent issue or opportunity.
5. **Opportunity signal** — a donor, plugin, API, MCP, workflow, framework, automation, existing artifact, or market/practitioner pattern could materially remove work or improve outcomes.
6. **Avoidable-reinvention signal** — the project is creating commodity infrastructure despite mature external or local solutions.
7. **Dependency-risk signal** — a library, service, provider, API, model, MCP, plugin, runtime, license, community, or maintainer situation becomes risky or stale.
8. **Stale-assumption signal** — a fact materially influencing execution has exceeded its freshness horizon or conflicts with newer evidence.
9. **Coverage-gap signal** — research repeatedly succeeds inside one source class while adjacent source classes, communities, peer systems, registries, or operator evidence remain unchecked.
10. **Coordination signal** — parallel workers, branches, resources, or effects are converging on conflicting ownership, stale snapshots, or integration bottlenecks.
11. **Cost/efficiency signal** — repeated reasoning, research, tool use, setup, or manual state reconstruction indicates a cache, automation, fixture, reusable kernel, or deterministic procedure is warranted.
12. **Completion-seam signal** — happy-path implementation exists while loading, error, empty, reconnect, cancellation, authority, accessibility, telemetry, or recovery seams remain weak.
13. **User-effort signal** — the user is repeatedly identifying adjacent omissions, asking the same class of follow-up, or manually supplying a source/capability that should have been discovered earlier.
14. **Emergent-practitioner signal** — multiple current practitioners converge on a new tool, workflow, architecture, community, or failure pattern that could change project strategy.
15. **Security/incident signal** — unexpected authority use, effect ambiguity, new vulnerability/advisory, provider compromise, anomalous worker behavior, or suspicious tool/plugin activity.

## Correlation before interruption

Prime Sense should correlate related observations before surfacing them. A weak single event is often noise; repeated or mutually reinforcing events can form a material signal.

Useful dimensions include:

- same subsystem or dependency;
- same failure mode;
- same source/provider;
- same user correction pattern;
- temporal clustering;
- causal adjacency;
- common project milestone;
- repeated donor/community references;
- cost/latency drift;
- cross-surface consistency or conflict.

Do not multiply notifications for correlated symptoms. Prefer one consolidated attention item with evidence and confidence.

## Change-point reasoning

Threshold-only alerting is insufficient for gradual or structural shifts. Where quantitative evidence exists, Watcher/runtime may use deterministic or statistical drift/change-point methods such as moving baselines, ADWIN/Page-Hinkley/KSWIN-style detectors, Bayesian online changepoint detection, or equivalent techniques.

These methods are optional implementation donors, not requirements for every surface. Their role is to distinguish ordinary variance from a probable regime change in metrics such as:

- latency;
- cost;
- tool success rate;
- retry rate;
- retrieval precision/recall proxies;
- build/test failure rate;
- model/provider behavior;
- user correction frequency;
- project lead time;
- dependency/API churn.

A detector raises evidence for attention; it does not independently authorize action.

## Complex-event reasoning

Some important situations are combinations rather than single events. Prime Sense may treat event-correlation / complex-event-processing patterns as a donor mechanism:

`event A + event B within window + shared dependency + unresolved state -> candidate material signal`

Examples:

- package update + maintainer abandonment + new vulnerability -> dependency intervention candidate;
- repeated user correction + source-map omission + competitor tool discovery -> Cerebro coverage failure;
- two worker writes + overlapping files + stale base -> integration conflict risk;
- cost spike + cache miss increase + repeated equivalent tasks -> cache/automation opportunity;
- live failure + same failure in community + donor issue thread -> avoid inheriting donor design.

Prefer deterministic correlation rules when the pattern is known and stable; use model judgment for ambiguous synthesis.

## External change sensing

When a project materially depends on external mutable information, Prime Sense should prefer existing event/change infrastructure before bespoke polling:

- official webhooks/events;
- release feeds/RSS/Atom;
- repository releases/issues/security advisories;
- dependency bots/advisory databases;
- change-detection services;
- MCP/plugin registry updates;
- provider status/incidents;
- community/maintainer announcements;
- scheduled targeted research checks where event surfaces do not exist.

Observe only sources relevant to an active project, explicit watch, or durable dependency. Do not build broad surveillance merely because data is accessible.

## Opportunity intelligence

Prime Sense should proactively consider whether the fastest path is external.

Before substantial work compounds, ask:

- Is there a donor system, open-source project, API, MCP, plugin, SDK, workflow engine, memory backend, eval stack, policy engine, or automation platform that removes this work?
- Does a peer project make this capability first-class while we leave it implicit?
- Are practitioners repeatedly using a capability class we lack?
- Is there a simpler product/process solution than the current technical plan?
- Does a recent community pattern or maintained tool change the best route?

If credible, route through Salvage First / capability catalog / donor ecosystem research rather than silently continuing greenfield work.

## User-correction amplification

A user repeatedly supplying adjacent missing sources, capabilities, or abstractions is a high-value meta-signal.

After one meaningful miss, correct the task.
After repeated misses of the same class, Prime Sense should elevate the pattern itself and trigger Failure Harvest / Meta-Cerebro rather than waiting for another correction.

The user should not need to become the system's anomaly detector.

## Attention scoring

A material implementation may combine dimensions such as:

- relevance to active objective;
- expected consequence;
- time sensitivity;
- confidence/evidence strength;
- reversibility;
- cost of delay;
- user effort saved;
- recurrence/correlation count;
- novelty/regime-change probability;
- available safe next action.

No single numeric score is canonical. The objective is calibrated prioritization, not false precision.

## Escalation

Prime Sense may recommend:

- ignore/suppress;
- retain for briefing;
- surface at next natural turn;
- investigate read-only;
- enter Sanctum;
- use Prime Memory/Archives;
- use Salvage First;
- use Cerebro / Mind Stone;
- convene Council;
- consult Web;
- have TVA prune a divergent branch;
- prepare an action;
- request approval;
- execute only within already-granted authority.

## Donor mechanisms

This doctrine is informed by several external capability classes:

- AIOps/incident tools: alert deduplication, enrichment, correlation and routing;
- streaming anomaly/concept-drift systems: online drift/change detection;
- Bayesian changepoint detectors: regime-change probability rather than threshold-only alerts;
- change-detection/watch services: monitor precise external surfaces and trigger events only on meaningful changes;
- dependency/security bots: event-driven advisories and bounded automated remediation;
- durable/event-driven agent runtimes: append-only events, wake/sleep cycles, replay and keyed state;
- AgentOps stacks: cost/SLA/regression monitoring and production-trace-to-eval loops;
- complex-event-processing engines: pattern/sequence/window correlation.

Sanctum adopts the mechanisms, not whole frameworks by default.

## Status

This Archive is canonical doctrine. Continuous observation, statistical drift detection, external event subscriptions, and automated interruption remain surface/runtime-specific and must be described as DOCUMENTED, CHECKED, ENFORCED, or OBSERVED according to real evidence.
