# Research and delivery quality contract

These dependency-free checks make unchecked dimensions visible. They do not turn
self-reported metadata into facts and do not authorize external actions.

## Cerebro / Mind Stone receipt

Run `python runtime/research_quality.py --receipt FILE [--review REVIEW_FILE]`.
The receipt is trusted owner-side data, not a worker's authority grant. Required fields:

- `objective`, timezone-aware `as_of`, `stop_reason`.
- `sources`: unique `id`, `locator`, relevant `section`, `family`, `kind`,
  `access=opened`, timezone-aware `retrieved_at` no later than the receipt date.
- `claims`: unique `id`, `text`, source IDs in `sources`, `basis` (direct, inference,
  proposal), and `limitation`. Inferences need `rationale`; claims marked `current`
  need `freshness_evidence`. `independent_confirmation=true` requires more than one
  declared family, but the checker cannot itself establish independence.
- `coverage`: `scope` and `limits`; landscape runs additionally record actual
  `lateral_route` and `practitioner_route`.
- `rounds`: question, finding and decision_impact for each meaningful round.
- When `forge=true`, `applications`: technique, baseline, change, status (proposed,
  tested, rejected), evidence and limitation. Tested applications also need result.

Keep material claims, not every sentence. Use concise paraphrases and source locations,
not copied articles or hidden reasoning transcripts. Local evidence stays private.

Result `STRUCTURE_PASS` means consistency/completeness only. Claim support stays
`NOT_EVALUATED` without a separately supplied review. A review contains the canonical
JSON receipt SHA-256, reviewer, method (human/agent), independence declaration, and a
complete map of claim IDs to verdict (supported/unsupported/uncertain) and a note.
The digest binds it to this receipt; it does not authenticate the reviewer. `REVIEWED`
records the supplied review, not a mathematically proven conclusion. Uncertainty
remains `NEEDS_REVIEW`; measured improvement is never inferred from a filled form.

The real research outcome remains task-relative. [Research-agent evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
supports separate groundedness, coverage and source-quality checks, with calibrated
judgment. [Search-method guidance](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04)
informs selective use of source lineage and recorded search routes; routine engineering
does not require a full systematic review.

## Web of Destiny trace scope

`research` events accept `{receipt, review?}` in data. A research route with no such
event returns PARTIAL; an empty/unrecognized trace returns NOT_EVALUATED. Existing
routing/action checks remain separately scoped. Multiple failures in one record
cannot make the passed-record count negative. An overall trace PASS does not certify
every semantic dimension; inspect `research_quality` and its claim-support status.
CLI eval returns nonzero for FAIL, PARTIAL or NOT_EVALUATED.

## Ultron delivery and prerequisite checks

`python runtime/delivery.py --contract REQUIRED_JSON --results RESULTS_JSON` compares
owner-defined required IDs and levels with result IDs, completion statuses, levels
and evidence references. Levels should use the exact accepted scope, such as tested,
merged or live. A missing result, changed level or evidence-free claim cannot close
the contract. `all_complete` trace claims must carry acceptance and result records.
Actual evidence still needs verification; this is not a self-issued approval.

`dependency_gate(required_steps, observations)` permits readiness only when every
prerequisite has observed `verified_success`. Failed/missing/unknown outcomes block
dependent action. Use it at the decision point, inspect real tool returns, and verify
state before any retry. It does not execute commands or grant permission.

## Evidence and limits

The [semantic calibration development set](../evals/research-calibration/README.md)
now supplies twelve source/claim examples and an agreement scorer. Labels remain
agent-authored pending human adjudication. The [live validation adapter](LIVE_VALIDATION.md)
connects this project's real release-check completion to local Presence.

`test_research_quality.py` includes development failure cases and additional transfer
cases; `test_delivery.py` checks misleading completion and dependency outcomes. They
are visible deterministic fixtures, not held-out evaluations of a model's general
research ability. Start semantic calibration with manually reviewed task examples;
introduce genuinely held-out questions before making comparative capability claims.
No paid evaluator, background research process or new platform is required.
