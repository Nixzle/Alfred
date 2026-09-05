# Deterministic First

Use when an orchestration route contains steps that can be owned more reliably by deterministic machinery than by model judgment.

## Rule

Do not assign a model a step that a deterministic function, parser, query, static check, policy engine, exact comparison, state machine, workflow primitive, or test can own reliably at lower cost and uncertainty.

## Procedure

1. Decompose the route into decision, interpretation, generation, state, validation, and effect steps.
2. Mark each step `DETERMINISTIC` or `JUDGMENT`.
3. Prefer deterministic machinery for invariants, parsing, validation, exact comparisons, state transitions, eligibility checks, and repeatable gates.
4. Reserve Ultron/agents for ambiguity, synthesis, planning, adversarial review, creative work, interpretation, and counterfactual judgment.
5. Compose mixed workflows instead of forcing an all-agent or all-code architecture.
6. Escalate a deterministic step to model judgment only when the deterministic contract cannot express the needed property economically.
7. Preserve evidence from deterministic checks so Web/Watcher can distinguish proof from narrative.

Representative route:

`deterministic preflight -> Ultron judgment -> deterministic retrieval/check -> specialist implementation -> deterministic tests -> Web evaluation -> deterministic release gate`

## Failure modes

- agent used for an exact check that should be code;
- brittle code used where interpretation is genuinely required;
- deterministic pass is inflated into proof of a property it did not test;
- workflow becomes fragmented into excessive micro-steps with coordination overhead.

## Theatrics

Preferred invocation: `This step does not deserve intelligence. I'm giving it to machinery that cannot improvise.`
