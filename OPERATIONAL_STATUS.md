# Alfred operational status

Date: 2026-09-05

## Current semantic baseline

Alfred carries a public self-contained Sanctum capability snapshot at `bootstrap/SANCTUM_PORTABLE_CORE.md` and maps it through `SANCTUM_INHERITANCE.md` into Alfred/Batcave responsibilities and theatrics.

Current frozen upstream baseline:

`Nixzle/Sanctum@b997221b889138e40d8797fca13efc89d41afaf0`

The public package validator requires:

- the Sanctum parity contract;
- the public frozen Sanctum snapshot;
- the current validated Sanctum baseline marker in snapshot, inheritance and bootstrap;
- Alfred-native theatrical role mapping;
- release/package identity tooling;
- normal package/link/publication checks.

## Observed CI evidence

GitHub Actions run `33950959662` on commit `db88c1ae1ca55ffc7ab130df1320814d5ba45fb9` completed successfully on the `Validate Alfred` workflow after the initial operational snapshot upgrade and validator correction.

Subsequent operational-hardening changes must receive their own CI result before they inherit that OBSERVED status. A green ancestor is evidence for the tested revision, not a blessing passed genetically to descendants.

## Current operational controls

- automatic validation on push and pull request;
- manual workflow dispatch;
- weekly scheduled validation;
- Linux and Windows validation matrix;
- package/publication/parity validation;
- launcher-isolation tests;
- Python source compilation check;
- diff hygiene check;
- content-addressed package release manifest;
- frozen public upstream operational snapshot;
- explicit repository-admin hardening contract for protected `main`, required checks and signing discipline.

## Operational maturity

| Capability | Maturity |
| --- | --- |
| public self-contained semantic snapshot | CHECKED; OBSERVED only on revisions with green CI |
| Alfred ↔ Sanctum capability mapping | CHECKED; OBSERVED only on revisions with green CI |
| Alfred theatrics mapping | CHECKED; OBSERVED only on revisions with green CI |
| launcher isolation tests | CHECKED / historically OBSERVED CI |
| scheduled package validation | CHECKED configuration; OBSERVED after scheduled runs execute |
| package release content identity | CHECKED |
| live Slack behavior | runtime-specific; not proven by package CI |
| live external integrations | runtime-specific |
| protected main / required checks | DOCUMENTED; not currently enforced by repository branch protection |
| signed canonical commits/releases | DOCUMENTED target; not currently enforced |

## Rule

Package CI proves only the shipped package/revision it actually tested. Runtime capability parity must still be proven on the host that runs Alfred, and repository-admin controls are not ENFORCED until GitHub settings evidence shows they are active.
