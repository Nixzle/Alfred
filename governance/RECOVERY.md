# Sanctum Recovery and Continuity

GitHub is canonical for the Sanctum, but the doctrine must remain recoverable without GitHub.

## Recovery requirements
- Keep doctrine as ordinary text/Markdown files that can be read from any clone or export.
- Avoid making critical doctrine depend on proprietary server-side metadata that is absent from a clone.
- Maintain at least one recoverable copy outside the live GitHub repository when practical, such as a local clone, periodic archive/export, or secondary mirror.
- Record the last known good canonical commit in recovery metadata or project pins.
- Do not place secrets or private chat transcripts in recovery artifacts.

## Outage behavior
If GitHub is temporarily unavailable:
1. Do not declare the Sanctum lost.
2. Use the latest trusted local clone/export if available.
3. Continue read-only or local work that does not require GitHub writes.
4. Queue doctrine/project updates locally with clear provenance rather than inventing remote success.
5. Re-probe GitHub availability later and reconcile against the canonical branch before pushing.

## Restoration
If the canonical repository is lost or corrupted:
1. Select the latest trusted full clone/export and verify its commit history/content integrity as far as practical.
2. Restore to a new private repository or mirror.
3. Re-establish project inheritance pointers and access controls.
4. Run the core Web of Destiny regression suite before declaring the restored Sanctum canonical.
5. Record the recovery event in `governance/PROVENANCE.md`.

## Current limitation
This repository defines the recovery contract, but an independent mirror/export is an infrastructure action outside the repository itself. Until one exists, disaster recovery is DOCUMENTED rather than fully ENFORCED.
