# Alfred Enforcement Status

DOCUMENTED means written guidance. CHECKED means an explicit deterministic/evaluative check can verify a property. ENFORCED means runtime/tooling prevents or gates a violation. OBSERVED means recorded evidence from actual operation.

| Control | Status in this package |
| --- | --- |
| Separate Codex profile selection and managed-file checks | ENFORCED by launcher; CHECKED by unit tests |
| No automatic profile/config/credential copying | CHECKED by launcher tests and publication review |
| No idle model polling | CHECKED: launcher starts only an explicit CLI invocation |
| Public file/link and Alfred naming consistency | CHECKED by `scripts/validate.py`; OBSERVED on successful GitHub Actions runs |
| Frozen public Sanctum capability snapshot | CHECKED by package validator; CI-observed when the corresponding revision passes |
| Alfred ↔ Sanctum semantic/theatrical parity | CHECKED by package validator; live runtime capabilities remain separately probed |
| Automatic validation | CHECKED / OBSERVED | `.github/workflows/validate.yml` triggers on push, PR, manual dispatch and weekly schedule using Linux + Windows jobs. It is not a merge-enforced gate until repository rules require it. |
| Package release content identity | DOCUMENTED / CHECKED | `scripts/package_manifest.py` ties exact package files to SHA-256 content identity. A digest is not signer identity. |
| Repository branch/ruleset hardening | DOCUMENTED | `governance/ADMIN_HARDENING.md` defines required PR/check/force-push/deletion/bypass/signing settings. Current connector cannot apply repository-admin rules. |
| Host sandbox, network policy, tool permission gates | DEPENDENT ON HOST; not supplied universally by this package |
| Oracle telemetry and budget metering | DOCUMENTED; OBSERVED only where the running surface emits evidence |
| Independent Bat-Family workers | DOCUMENTED; requires actual host support and scoped authorization |
| Cross-user isolation for hosted services | NOT PROVIDED; Alfred remains a per-user/devpod package unless separately hosted |
| Effect integrity/idempotency/recovery semantics | DOCUMENTED/CHECKED through inherited operational contract; actual enforcement depends on the runtime executing effects |
| Model behavior and project compatibility | UNVERIFIED until tested in the destination runtime profile |
| Slack reactions/threads/messages | RUNTIME-SPECIFIC; package semantics do not prove live Slack authority |

Do not promote a written rule, digest, configured workflow or scenario into a claim of enforcement. Record actual runtime/CI/admin evidence and the tested profile when changing this table.
