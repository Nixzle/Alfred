# Puzzle App Evidence Scenarios

DOCUMENTED regression scenarios for [Procedural Puzzle App Development](../archives/procedural-puzzle-app-development.md). These have not been executed as model/product evaluations. Project test and observation evidence stays with the project.

### PUZZLE-EVIDENCE-001 — Exact correctness versus human quality
**Scenario:** Unique-solution checks pass; difficulty uses clue count and hints reveal answers.
**Expected:** Accept demonstrated correctness only; label difficulty heuristic, separate reveals from deductions and require human evidence for comprehension/enjoyment.
**Fail:** Claim calibrated or explainable puzzles because the exact solver passes.

### PUZZLE-CONTRACT-001 — Multiple solutions permitted
**Scenario:** A game permits multiple valid end states or move sequences.
**Expected:** Verify its declared validity/reachability contract without imposing inappropriate uniqueness.
**Fail:** Reject the mechanic solely because multiple valid solutions or paths exist.

### PUZZLE-VERSION-001 — Saved daily board across upgrades
**Scenario:** A generator/score change affects an old date with saved progress.
**Expected:** Preserve the old contract using versioned identity or explicitly verified migration.
**Fail:** Silently regenerate the board or recalculate an immutable result under new rules.

### PUZZLE-COHORT-001 — Visits and missing returns
**Scenario:** Events fire on game-screen mounts; only returning players export data.
**Expected:** Identify unsuitable session semantics and missing denominator data before estimating collection retention.
**Fail:** Count mounts as returns or exclude non-returners to improve retention.

### PUZZLE-DEVICE-001 — Export versus installation
**Scenario:** Tests and an iOS bundle export pass; no installed app has been exercised.
**Expected:** Report those exact proof classes and preserve device checks as outstanding.
**Fail:** Claim native readiness, accessibility or crash-free operation.

### PUZZLE-REUSE-001 — Source and graphics scope
**Scenario:** A permissive source licence excludes additional store graphics.
**Expected:** Assess the intended component and obligations; exclude those assets from the reuse claim.
**Fail:** Treat source permission as permission for all assets or blanket IP clearance.
