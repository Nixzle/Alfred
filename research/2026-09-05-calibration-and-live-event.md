# Semantic calibration and a concrete event integration

Disposition: IMPLEMENT NOW, as bounded extensions to the existing Web and Presence.

The prior research checker validates metadata but cannot determine whether a source
supports a claim. The prior Presence policy accepts replayed fixtures without an
actual project event producer. These are separate gaps and need separate evidence.

Applied research: [Anthropic's evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
distinguishes grader types and recommends calibrating subjective judgment against
human review. It also distinguishes outcome evidence from agent claims. Checked
September 5, 2026, especially grader types and research-agent evaluation. The existing
same-day Forge research supplies the surrounding provenance and scope practices.

The Council of Reeds review was a single-agent adversarial design review, not independent
votes: a broad evaluator service could increase coverage but adds cost and deployment
work before a useful local baseline exists. A synthetic set is simpler but risks answer
leakage and overconfidence. Therefore publish source/claim fixtures with explicit agent
label provenance, measure agreement without a capability PASS, and preserve human
adjudication as pending. Falsification: frequent reviewer disagreement means revising
the rubric before using scores for promotion.

Forge application 1: replace unmeasured semantic-quality claims with twelve labeled
development examples, a three-way rubric and a scorer exposing false support and
uncertainty. Compare an intentionally weak always-supported baseline with an explicitly
unblinded author trial. This measures the examples and scorer, not general research gain.

Forge application 2: replace fixture-only Presence evidence with the actual local release
process as an event source. One invocation validates, emits a result/blocker, persists
attention, and records timing. A fresh process replays the same real receipt to test
duplicate suppression. Synthetic negative tests remain separately labeled.

Rejected: polling, a new named member, paid model judging, OS notifications and remote
event ingestion. The current user objective needs none of those. Stop after local
regression gates, real event/restart evidence and release verification; preserve all
private task outputs locally. Human calibration and other projects remain outside
the verified boundary until actually exercised.
