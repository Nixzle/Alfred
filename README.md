# Alfred · The Batcave

“Your briefing is ready. Shall we make ourselves useful?”

A public Batman/DC-themed assistant operating framework for Codex in a development pod. Alfred brings planning, research, coding, verification, and restrained theatrics to your own workspace.

## Start in your devpod

Requires Python 3.10+, Git, and an installed [Codex CLI](https://learn.chatgpt.com/docs/cli). Use your work environment's approved Codex installation and account. This package has no Python dependencies and installs no services.

```sh
git clone https://github.com/Nixzle/Alfred.git
cd Alfred
python3 scripts/alfred.py doctor
python3 scripts/alfred.py login
python3 scripts/alfred.py run --workspace /path/to/your/project
```

On Windows use `python` instead of `python3`. For a headless pod, use `python3 scripts/alfred.py login --device-auth`. If the pod already supplies an approved model runner other than Codex, give that runner this repository's `AGENTS.md` and preserve its own project and permission rules.

Alfred's profile lives at `~/.local/share/alfred/codex`. Its instructions point to this checkout, so retain the checkout. Login, configuration, and sessions use that separate profile; the launcher never copies your normal Codex profile. It does not modify the target project's files. There is no account or paid API access bundled with the package.

## The roster

| Name | Responsibility |
| --- | --- |
| **Alfred** | Intent, orchestration, decisions, and verified delivery |
| **Batcave** | The operating framework |
| **Brother Eye** | Research, discovery, and capability gaps |
| **Bat-Drones** | Bounded specialist roles |
| **Bat-Family** | Isolated autonomous workers when available |
| **Oracle** | Evidence, activity, cost, and anomaly tracking |
| **Mobius Chair / Metron** | Evaluation, alternatives, and regressions |
| **Justice League** | Adversarial review of difficult decisions |
| **Contingency Plans** | Permission and action-boundary rules |
| **Batcomputer** | The collection of reusable **Protocols** |
| **Archives** | Reusable knowledge and records |
| **Mission Briefs** | Worker scope and acceptance criteria |
| **Bat-Signal** | Actionable alerts |
| **Batcave Console** | The interface label; currently the Codex terminal |

## Use Alfred

Try: “Review this repository and give me a mission brief.” Or: “Brother Eye, investigate the blocker, then implement and verify the smallest useful fix.”

Alfred loads only the relevant guidance for the task. Named roles never imply imaginary tool calls, workers, tests, monitoring, or permissions. The package starts no background polling and makes no model calls while idle by itself. Actual Codex work uses your account's normal usage.

## What is included

- [Identity and routing](AGENTS.md), [role definitions](members/README.md), and [theatrics](THEATRICS.md).
- [Batcomputer Protocols](batcomputer/README.md), [Brother Eye research](research/README.md), and an [Archives starter](archives/README.md).
- [Contingency Plans](governance/OPERATIONAL_INTEGRITY.md), [actual enforcement status](governance/ENFORCEMENT_STATUS.md), and [evaluation scenarios](evals/README.md).
- A standalone launcher, [devpod setup notes](bootstrap/README.md), and a [Mission Brief template](templates/MISSION_BRIEF.md).

## Boundaries

New named roles require a distinct responsibility that existing roles cannot reasonably cover, plus evidence that the added complexity improves results. Prefer strengthening or simplifying existing roles. Naming a role never creates runtime capability.

Public package does not mean public access to your devpod. Each installation uses its own account and project. No private conversations, personal connector configuration, project history, or source repository history are included. This release is not a hosted chat service, multi-user platform, model, or security sandbox. Profile separation prevents automatic profile reuse; operating-system access and the host's sandbox still determine what a process can access. Configure workplace integrations separately.

## Check the package

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The automated tests check the launcher and package structure, not model quality or your company's environment. See [verification status](VERIFICATION.md). This is an unofficial fan-themed software project.
