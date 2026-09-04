# Enforcement status

DOCUMENTED means written guidance. CHECKED means an explicit check can verify a property. ENFORCED means runtime code prevents a violation. OBSERVED means recorded evidence from actual operation.

| Control | Status in this package |
| --- | --- |
| Separate Codex profile selection and managed-file checks | ENFORCED by the launcher; CHECKED by unit tests |
| No automatic profile/config/credential copying | CHECKED by launcher tests and publication review |
| No idle model polling | CHECKED: launcher starts only an explicit CLI invocation |
| Public file/link and naming consistency | CHECKED by package validation |
| Host sandbox, network policy, tool permission gates | DEPENDENT ON HOST; not implemented by these documents |
| Oracle telemetry and budget metering | DOCUMENTED; only available when the runtime supplies evidence |
| Independent Bat-Family workers | DOCUMENTED; requires actual host support and scoped authorization |
| Cross-user isolation for hosted services | NOT PROVIDED; this is a per-user devpod package |
| Idempotency, incident recovery, authority attenuation | DOCUMENTED; scenarios available for host evaluation |
| Model behavior and project compatibility | UNVERIFIED until tested in the destination runtime |

Do not promote a written rule or scenario into a claim of runtime enforcement. Record new evidence and the tested runtime when changing this table.
