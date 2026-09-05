# Anti-Hermes runtime status

Date: 2026-09-05

The anti-Hermes donor tranche is now represented by executable, standard-library runtime contracts plus deterministic regression coverage.

## Implemented

- `spell_registry.py` — on-demand Spellbook indexing, trigger-based selection, content digests, version monotonicity, usage/outcome evidence, duplicate-candidate detection, retirement and manifest integrity.
- `reliability_contracts.py` — delegated-work acceptance/completion receipts, lost-result state, budget guards for tokens/cost/attempts/time, explicit unknown-outcome handling, and failover selection that refuses to skip reconciliation.
- `adapter_contract.py` — portable host adapter manifests with declared reads/writes/effect classes, context mode, health observations, digest integrity, destructive-action confirmation and revocation semantics.
- `self_audit.py` — evidence-driven harness audit that converts repeated corrections/failures into proposals and assigns low/medium/high/forbidden risk. Only low-risk maintenance is eligible for automatic application by contract; consequential changes require review.
- `a2a_contract.py` — dormant A2A-style Agent Card, skill discovery, invocation-grant and artifact contracts. No network listener, remote federation or automatic external agent invocation is enabled.
- `memory_service_contract.py` — dormant host-neutral memory request/authorization/receipt semantics. No MCP/REST server or shared external store is enabled.

## Regression coverage

`runtime/tests/test_anti_hermes.py` checks progressive Spell loading/curation, delivery receipts, budget/failover behavior, adapter health and effect authority, self-audit risk tiers, discovery-vs-invocation separation, and cross-host memory governance.

The canonical validator discovers this test automatically because it runs `runtime/tests/test_*.py`.

## Evidence boundary

These files are IMPLEMENTED and have deterministic regression definitions. They are not yet promoted to integrated-release-validated for the current combined `main` checkout because the authorized development host remained unavailable and there was no hosted workflow evidence at the time of implementation.

A2A and cross-host memory are intentionally dormant contracts. Activating actual network federation, a remote agent registry, MCP/REST memory service, or another persistent trust boundary requires a real consumer, explicit authority, threat review, and runtime validation.
