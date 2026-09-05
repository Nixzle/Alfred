# Pro operational-integrity sweep — 2026-09-04

## Trigger
The user moved the ChatGPT Ultron surface from High to Pro reasoning and requested another broad miss/upgrade sweep.

## Runtime profile
- Surface: ChatGPT
- Identity/bootstrap: Ultron Prime / `SANCTUM-BOOTSTRAP-V1`
- Canonical Sanctum baseline at sweep start: `3e7a0bdc2130af4a09d8a661f7ee7d5c4e22a5a7`
- Reasoning tier: Pro, as selected by the user
- Research: current primary/official sources and current canonical Sanctum
- Council: same-model adversarial review; not counted as independent model confirmation

One Pro run demonstrates a higher-reasoning review, not repeated-run reliability of the Pro runtime profile.

## Method
Cerebro performed a boundary-oriented and subtractive sweep rather than another member/tool inventory. The review tested the complete lifecycle:

`intent -> context -> memory -> delegation -> shared state -> tool dispatch -> external effect -> retry/resume -> monitoring -> incident response -> learning`

It also inspected whether existing doctrine covered the end-to-end behavior or only fragments of it. Council of Reeds challenged every candidate for overlap, speculative complexity, and whether a smaller upgrade to an existing responsibility would suffice.

## Findings promoted

### 1. Effect integrity and resume semantics
**Gap:** Tool contracts, retry discipline, checkpoints, and rollback existed, but the Sanctum did not explicitly treat timeouts as unknown outcomes, require verify-before-retry, track committed effects, or distinguish replay/resume/fork semantics. This leaves duplicate and partial side effects possible after non-atomic failures.

**Evidence:**
- `Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint, Interrupt, and Resume Semantics in Workflow Persistence Layers` (arXiv:2608.03836) reports inconsistent framework resume behavior and duplicate effect execution after crash/recovery.
- `Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures` (arXiv:2608.02645) evaluates postcondition verification, verify-before-retry, and idempotency keys under partial/ambiguous failures.
- `ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore` (arXiv:2603.20625) identifies action replay and authority resurrection when LLM agents re-synthesize effects after restore.

**Promotion:** `governance/OPERATIONAL_INTEGRITY.md`; `TOOL-EFFECT-*` and `RESUME-SEMANTICS-*` regressions; Ikonn/TVA/Watcher roadmap upgrades.

### 2. Shared-state consistency and write ownership
**Gap:** Cognitive independence and isolated worktrees were covered, but concurrency over shared task ledgers, memories, documents, repositories, tool registries, and external state lacked explicit ownership, versions, conflict detection, and effect ordering.

**Evidence:**
- `CoAgent: Concurrency Control for Multi-Agent Systems` (arXiv:2606.15376) treats long-running agent trajectories against shared mutable systems as a concurrency-control problem.
- `Position: Multi-Agent Systems Should Prioritize Concurrency Control` (arXiv:2608.18092) argues stale reads and lost updates become more likely as inference windows grow.
- `Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems` (arXiv:2606.17182) formalizes stale-generation, phantom-tool, causal-cascade, and tool-effect-reordering anomalies.
- `When 20 Agents Fail to Sort` (Findings of ACL 2026) reports failures in shared state, convention alignment, and consistent termination as agent count grows.

**Promotion:** shared-state consistency doctrine; `SHARED-STATE-*` regressions; explicit version/write-owner/conflict requirements in durable-state and Ikonn roadmap items.

### 3. Temporal validity and supersession
**Gap:** Capability freshness and memory integrity existed, but changeable facts could remain simultaneously active without effective dates, supersession, revocation, or `as of` semantics.

**Evidence:**
- `TReMu` (Findings of ACL 2025) demonstrates large gains from time-aware memorization and explicit temporal reasoning in multi-session dialogue.
- `Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents` (Findings of ACL 2026) models semantic occurrence time and durative memory rather than dialogue timestamp alone.
- `Temporal Validity in Retrieval Memory` (arXiv:2606.26511) reports stale-fact errors when similarity retrieval cannot distinguish superseded facts.
- `TEPA: Revoking Stale Memories for Conflict-Robust Language Agents` (arXiv:2608.07429) treats revocation/supersession as a core memory operation while preserving audit history.
- `Governed Shared Memory for Multi-Agent LLM Systems` (arXiv:2606.24535) identifies stale propagation, contradiction persistence, provenance collapse, and scoped retrieval as systems-level concerns.

**Promotion:** temporal-validity doctrine and `TEMPORAL-VALIDITY-*` regressions.

### 4. Delegated authority lineage and attenuation
**Gap:** TVA covered least privilege and action gates, but the Sanctum did not explicitly require principal/delegator/task lineage, authority attenuation through sub-agents, operation-bound grants, replay resistance, or confused-deputy protection.

**Evidence:**
- NIST's 2026 concept paper on software and AI agent identity and authorization calls out identification, authorization, auditing, non-repudiation, and prompt-injection controls.
- `Delegation Without Trust` (arXiv:2609.00267) models confused deputy, token theft/replay, prompt-injection privilege escalation, and compromised sub-agent threats under an untrusted-model assumption.
- `Taming Various Privilege Escalation in LLM-Based Agent Systems` (arXiv:2601.11893) proposes mandatory access control for over-privileged agent-tool interactions and multi-agent privilege escalation.
- `Prompt Injection as Role Confusion` (arXiv:2603.12277) finds models infer authority from linguistic role cues rather than interface provenance.

**Promotion:** TVA/delegation doctrine and `DELEGATION-AUTHORITY-*` regressions.

### 5. Privacy at acquisition and across the data lifecycle
**Gap:** The Archives included Security & Privacy and Watcher supported redaction modes, but the core doctrine focused more on disclosure and secret handling than unnecessary acquisition, purpose limitation, retention, deletion, derived sensitivity, and cross-surface privacy boundaries.

**Evidence:**
- `PrivacyPeek` (arXiv:2606.00152) audits sensitive information agents acquire beyond task scope and shows acquisition-stage leakage is widespread.
- `Privacy in Action` (arXiv:2509.17488) evaluates privacy mitigation in live MCP/A2A-style environments and reports larger practical risks than static benchmarks.
- `CI-Work` (ACL 2026 Industry Track) reports contextual-integrity failures in enterprise retrieval workflows and a utility/privacy tension.
- `MAGPIE` (arXiv:2510.15186) evaluates privacy preservation in collaborative multi-agent tasks where sensitive information is task-relevant.

**Promotion:** data-minimization/lifecycle doctrine and `DATA-MINIMIZATION-*` / `DATA-LIFECYCLE-*` regressions.

### 6. Incident containment
**Gap:** Rollback, recovery, Watcher, and TVA existed, but the operational sequence for a suspected security/privacy/integrity incident was fragmented. There was no explicit stop/quarantine, authority revocation, propagation freeze, blast-radius assessment, evidence preservation, and revalidation sequence.

**Evidence:**
- NIST AI 800-4 (2026) frames post-deployment monitoring as necessary for reliability, unexpected consequences, security, human factors, and compliance.
- NIST's 2026 AI Incident Management workshop and roadmap work distinguish incidents caused by attack, misuse, and malfunction and call for scalable incident-response practices.
- NIST's 2026 AI-agent security RFI analysis reports broad agreement that existing cybersecurity practices need adaptation for agent-specific threats.

**Promotion:** bounded incident-containment doctrine and `INCIDENT-CONTAINMENT-*` regressions. No new member: Watcher detects/records, TVA contains/revokes, Ultron decides, Web verifies.

## Council of Reeds decisions

### Accepted
All six findings close concrete end-to-end gaps that were only partially represented by existing rules. Each was implemented as an invariant or existing-member upgrade rather than a new role.

### Rejected
- **New member:** rejected. TVA, Watcher, Ikonn/Bots, Web, Cerebro, and Ultron already own the necessary responsibilities.
- **New spell:** rejected. These are always-on execution invariants, not episodic orchestration maneuvers.
- **Full-Sanctum rewrite:** rejected. A focused operational-integrity doctrine plus pointers/regressions is lower-complexity and easier to maintain.
- **Pro as permanent maximum-force routing:** rejected. Pro is a runtime profile, not permission to invoke maximum machinery on every ask.
- **Automatic claim of enforcement:** rejected. Runtime support remains mostly `DOCUMENTED/CHECKED`; roadmap implementation is still required.

## Classification
- Doctrine and regression additions: `IMPLEMENT NOW` — completed in this sweep.
- Runtime effect ledger, concurrency controls, delegated capability broker, temporal memory, privacy lifecycle gates, and incident automation: `SCHEDULE` under the implementation roadmap.
- Additional broad speculative research: `REJECT` until implementation or observed failures create a new trigger.

## Confidence and limitations
Confidence is high that these are real missing execution classes. Confidence is lower that the cited 2026 mechanisms are universally best implementations; several are recent preprints. The promoted doctrine therefore specifies required properties and failure tests rather than canonizing one framework or paper's architecture.

The Council and Ultron in this sweep share the same underlying model/runtime and are not counted as independent reasoners. Independence came from competing framings, multiple evidence lines, deterministic/classical systems principles, and explicit overlap/subtractive review.
