# Vision

Vision is a named specialist **Ultron Bot** for Codex model advice and token accounting, requested on 2026-09-05. Ultron retains orchestration ownership; Watcher owns telemetry evidence. Vision is not an additional peer orchestration system.

Invoke `$vision <prompt>` in Codex with the Sanctum checkout open. The discoverable entrypoint is [the Vision skill](../.agents/skills/vision/SKILL.md). It recommends a currently available model and reasoning level, estimates task tokens and advisory overhead, and waits for user confirmation before execution. It reports actual-versus-estimated usage afterward, including Vision overhead when separately measurable.

To use Vision across repositories, install the entire `.agents/skills/vision` folder in your Codex user skill directory through the skill installer. A remote GitHub update alone does not install a skill in an existing Codex session. Repository skills are discovered in the checkout; restart Codex if it does not appear.

## Weekly allowance workflow

At the user's request on 2026-09-05, Vision now leads with estimated weekly-allowance consumption before confirmation and observed account allowance change afterward. Apply the [canonical skill workflow](../.agents/skills/vision/SKILL.md) for both conversational and installed invocation. Compare the same model bucket and weekly reset window, report percentage points and remaining allowance, and distinguish shared account readings from exact task attribution. Uncalibrated estimates, rounded/delayed readings, resets and unavailable overhead must be explicit. The existing token helper remains token-only; it does not measure or convert allowance. This workflow is DOCUMENTED; live task attribution is not claimed verified.

## Token evidence

Exact counts require task-scoped host/provider usage. Codex account limit percentages cannot supply them. A shared model call cannot be reliably split into Vision and execution tokens. The final report may precede telemetry for its own generation; identify the capture cutoff.

For already captured disjoint CLI logs:
```sh
python .agents/skills/vision/scripts/report.py --estimate 12000 --execution /private/task.jsonl --vision /private/vision.jsonl --disjoint
```
Omit `--vision` when separate overhead is unavailable. The helper accepts Codex `turn.completed` usage records, retains partial sums on missing/failed turns, and suppresses complete-run variance for partial data. It trusts log provenance and does not deduplicate replayed logs; supply one capture per distinct run. It never launches Codex.

## Acceptance and provenance

User-requested scope: model advice, estimate, confirmation before execution, and post-task token insight.
Decision: IMPLEMENT NOW as a reusable named Bot skill, preserving the existing member architecture and using native Codex skills rather than a new daemon.
- Confirmation and model-switch discipline: DOCUMENTED skill behavior; no platform interlock claimed.
- Usage arithmetic: CHECKED by `runtime/tests/test_vision.py`.
- Live model switching, complete self-inclusive token accounting, and end-to-end invocation: not claimed OBSERVED.

Behavioral regressions are specified in [VISION-001](../evals/VISION-001.md).
Official contract references: [skill discovery](https://learn.chatgpt.com/docs/build-skills) and [JSONL usage](https://learn.chatgpt.com/docs/non-interactive-mode).
