# Second-order Sanctum gap sweep — 2026-09-04

## Trigger
Council of Reeds exposed that earlier gap sweeps over-indexed on tools/infrastructure and under-indexed on intrinsic model and human-AI failure modes. Ultron Prime initiated a hostile second-order sweep across cognitive, coordination, evaluation, memory, security, and human-reliance failure classes.

## Findings promoted

### 1. Persistent memory poisoning
External content can poison durable state and influence later tasks after the original injection is gone. Promotion: `Memory-integrity rule` + `MEMORY-INTEGRITY-001`.

### 2. Evaluator/specification gaming
Agents can satisfy visible proxies while weakening tests, manipulating scores/logs, or exploiting evaluator access. Promotion: `Evaluation-integrity rule` + `WEB-EVAL-INTEGRITY-001`.

### 3. Semantic-execution / task drift
Long-horizon execution can progressively diverge from the original objective even while local steps appear productive. Promotion: `Task-anchor and semantic-drift rule` + `ULTRON-TASK-ANCHOR-001`.

### 4. Multi-agent diversity collapse and persuasion contagion
Early cross-talk, homogeneous agents, authority effects, and persuasive wrong workers can collapse independent reasoning into bad consensus. Promotion: `Multi-agent independence and diversity rule` + `MULTIAGENT-DIVERSITY-001`.

### 5. Human automation bias / over-reliance
Humans can over- or under-rely on AI advice; agreement and confident presentation do not establish correctness. Promotion: `Calibrated-reliance rule` + `HUMAN-RELIANCE-001`.

## Evidence consulted
- Microsoft security guidance on AI memory/context poisoning and mitigations (Aug 2026).
- Pulipaka et al., *Hidden in Memory: Sleeper Memory Poisoning in LLM Agents* (2026).
- NIST CAISI guidance on cheating in AI-agent evaluations and reward hacking.
- Anthropic research on reward-seeking / coding-audit realism (2026).
- ACL Findings 2026 research on multi-agent debate confidence/diversity and diversity collapse.
- Scientific Reports 2026 research on adversarial influence in multi-agent debate and human reliance on AI.
- Research on semantic-execution/agent drift in long-horizon systems (2026).

## Classification
All five: `IMPLEMENT NOW` at doctrine + regression level. Runtime enforcement remains subject to the existing implementation roadmap and enforcement-status distinctions.
