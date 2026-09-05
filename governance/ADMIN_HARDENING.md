# Alfred Repository Admin Hardening

Status: required external control plane

The Alfred package is publicly downloadable and already runs automatic validation on push/PR. The remaining repository-admin controls cannot be changed through the current connector because branch-protection/ruleset administration is not exposed.

## Required `main` protections

When repository administration access is available:

1. require pull requests before merge for consequential package/runtime changes;
2. require the `Validate Alfred` workflow checks to pass before merge;
3. require both Linux and Windows validation jobs when GitHub exposes them as separate required checks;
4. block force pushes and deletion of `main`;
5. restrict bypasses to explicit maintainers only where operationally necessary;
6. require review-thread resolution when reviews are used;
7. prefer signed release tags/commits where practical;
8. preserve audit evidence for any bypass.

## Release identity

`scripts/package_manifest.py` produces a content-addressed package manifest. A promoted Alfred release should record:

- exact commit SHA;
- package manifest digest;
- CI run/result;
- Alfred package version;
- frozen Sanctum snapshot baseline;
- rollback target;
- cryptographic signature/attestation only when a real signer system has actually produced one.

A SHA-256 digest proves content identity, not author identity.

## Activation evidence

After protections are enabled, record the active ruleset/branch protection, required check names, bypass actors, timestamp, first protected merge, and first signed release/tag if signing is enabled. Only then promote the relevant controls from CHECKED to ENFORCED/OBSERVED.
