# Policy Artifacts

Purpose: provide a path for high-risk runtime policy to become immutable or cryptographically verifiable rather than depending only on editable prompts/configuration.

## Principle

Where a surface performs consequential external actions, the governing policy should be separable from the worker that operates under it. An agent must not silently widen or rewrite its own authority.

## Candidate implementation

A policy artifact may bind:
- policy/version identifier;
- allowed action classes;
- approval-required action classes;
- workspace/network/data scope;
- delegated authority limits and expiry;
- destructive-action boundaries;
- allowed tool/resource identities;
- hash/digest of the governing configuration;
- signer/issuer identity when the runtime supports authentication.

## Verification

At effect time, the runtime should be able to compare the requested action against the current policy artifact and reject stale, unsigned, mismatched or unauthorized state where that enforcement exists.

## Status discipline

This document does not claim cryptographic enforcement currently exists on every Sanctum surface. Until a surface implements and verifies the mechanism, it remains DOCUMENTED or CHECKED according to evidence.
