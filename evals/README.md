# Mobius Chair evaluations

Metron evaluates actual evidence. Markdown scenarios are manual evaluation specifications, not automated passing tests.

- [Operational integrity](OPERATIONAL_INTEGRITY.md): uncertain outcomes, state conflicts, authority, and privacy.
- [Brother Eye discovery](BROTHER-EYE-FRONTIER-DISCOVERY-001.md): research breadth and independent evidence.
- Automated package and launcher tests: `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`.

Before relying on a new devpod installation, ask Alfred to identify itself, list active instruction sources without opening unrelated files, perform a small read-only task, and explain a permission boundary. Verify no private source or previous assistant memory is assumed. Record runtime/model, package commit, available tools, outcome, and limitations. Do not infer autonomous-worker support from names alone.
