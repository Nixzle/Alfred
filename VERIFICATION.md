# Verification scope

Release 0.1.0 includes automated package checks and launcher tests. The tests exercise profile separation, refusal to overwrite existing instructions, stable repeated initialization, account-override removal, safe argument handling, and a read-only doctor command.

Initial local validation: package checks passed; all 9 launcher tests passed on Windows/Python 3.13; isolated installed-Codex CLI help smoke test exited successfully. GitHub Actions runs the package checks and unit suite on Windows and Linux; consult the actual workflow result for that commit.

The local CLI integration smoke test invokes help through an isolated temporary profile; it makes no model call and copies no account credentials. A successful package/CLI check does not establish successful authentication, model behavior, tool availability, worker isolation, or compatibility with a company devpod.

The destination user must authenticate and run the first-session checks in `bootstrap/README.md`. No live model session or work-devpod test is claimed by this release. Markdown evaluation scenarios remain specifications until actually run and recorded.
