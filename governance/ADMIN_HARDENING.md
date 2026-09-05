# Repository Admin Hardening

Status: required external control plane

These controls are part of Sanctum's operational target but cannot be enabled through the currently available GitHub connector because repository administration/ruleset writes are not exposed.

## Required settings for `main`

When repository administration access is available, configure `main` with the strongest practical equivalent of:

1. require pull requests before merge for consequential runtime/governance changes;
2. require the `Sanctum Runtime / Runtime control plane` validation check to pass before merge;
3. require branches to be up to date before merge when compatible with the workflow;
4. block force pushes and branch deletion;
5. restrict bypasses to explicit repository owners/administrators only when operationally necessary;
6. require conversation/review resolution where reviews are used;
7. prefer signed commits and/or signed release tags for promoted releases;
8. preserve audit history for any administrative bypass.

## Release identity

`runtime/release_manifest.py` provides content-addressed release identity. A promoted release should include:

- exact Git commit SHA;
- deterministic manifest digest;
- validation receipt/result;
- known runtime profile/evidence scope;
- signature/attestation when the release environment supports one;
- rollback target / last known good revision.

A content digest is integrity evidence, not signer identity. Do not call a manifest `signed` unless a real cryptographic signer/attestation system produced and verified the signature.

## Hosted runner blocker

As of 2026-09-05, private-repository `Sanctum Runtime` workflows trigger on pushes but fail before normal job-step/log evidence is exposed. Until runner availability is repaired:

- hosted CI is `TRIGGER OBSERVED / EXECUTION BLOCKED`;
- do not require a permanently failing hosted check as the sole merge gate;
- use the canonical local validator on an authorized host for release promotion;
- once hosted jobs execute normally, require the hosted validation check for `main`.

## Activation evidence

When these settings are enabled, record:

- ruleset/branch-protection identifier or screenshot/API evidence;
- required check names;
- bypass actors;
- activation timestamp;
- first successful protected merge;
- first verified signed release/tag if signing is enabled.

Then update `governance/ENFORCEMENT_STATUS.md` from CHECKED to ENFORCED/OBSERVED only where the evidence supports it.
