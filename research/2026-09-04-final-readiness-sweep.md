# Final readiness sweep — 2026-09-04

## Trigger
User requested one final upgrade sweep with Council of Reeds adversarial review before freezing speculative Sanctum expansion.

## Method
Cerebro searched current 2026 work on agent reliability, long-horizon planning, context engineering, tool-use failures, multi-agent failure propagation, and evaluation validity. Council of Reeds then challenged whether each finding represented a real gap, duplicated existing doctrine, or merely added complexity.

## Findings promoted

### 1. Context preflight
**Gap:** Sanctum evaluated behavior after execution but did not explicitly score/inspect the quality of the operating context before consequential runs.
**Promotion:** `Context-preflight rule` + `CONTEXT-PREFLIGHT-001`.
**Evidence:** 2026 research on context engineering identifies role clarity, instruction consistency, grounding, tool schemas, guardrails, injection hardening, and token efficiency as leading indicators of agent reliability.

### 2. Global constraint ledger and infeasibility detection
**Gap:** Task anchoring protected the objective, but long-horizon plans could still satisfy local steps while violating global budgets/dependencies/constraints or forcing an infeasible plan.
**Promotion:** `Constraint-ledger and feasibility rule` + `GLOBAL-CONSTRAINTS-001`.
**Evidence:** ACL 2026 DeepPlanning and Agent Planning Benchmark report persistent failures in global constrained optimization, tool-noise robustness, and calibrated infeasibility detection.

### 3. Tool necessity and result grounding
**Gap:** Tool contracts governed how tools should be called but did not explicitly cover unnecessary tool use, required-tool skipping, ignoring returned results, or misapplying tool outputs.
**Promotion:** `Tool-necessity and result-grounding rule` + `TOOL-GROUNDING-001`.
**Evidence:** Tool-use diagnostic benchmarks distinguish tool-skip, always-call, result-ignore, and output-application failures.

### 4. Reliability distributions, not one successful run
**Gap:** Watcher tracked cost/drift and Web tracked regressions, but doctrine did not explicitly distinguish capability from consistency across repeated runs.
**Promotion:** `Reliability-distribution rule` + `RELIABILITY-DISTRIBUTION-001`.
**Evidence:** Princeton HAL/ICML 2026 reliability work reports substantial gaps between task capability and repeated-run reliability, plus high resource variance.

## Council of Reeds verdict
The Council rejected additional speculative members, spells, and broad architectural layers. The four promotions above close concrete diagnostic gaps without expanding the named roster. The Council also reaffirmed the subtractive rule: implementation and measurement now dominate further speculative discovery.

## Classification
All four: `IMPLEMENT NOW` at doctrine/regression level. Runtime automation remains governed by `ROADMAP.md` and `governance/ENFORCEMENT_STATUS.md`.

## Freeze decision
After this sweep, broad speculative Sanctum expansion is frozen by default. New research is just-in-time unless real work, Watcher evidence, a major platform change, or Web regression exposes a concrete gap.
