# Engineering Principles (Carmack-leaning)

This repository favors a pragmatic, reliability-first style inspired by John Carmack’s engineering habits.

## Principles applied

1. **Simple data model first**
   - Markdown files on disk are source of truth.
   - Frontmatter schema is explicit and constrained.

2. **Deterministic checks over opinions**
   - `vault_doctor.py` encodes concrete invariants.
   - CI runs strict checks and fixture-driven tests.

3. **Measure and expose state**
   - Doctor outputs counts and health indicators (inbox, links, approvals, log freshness).
   - Health output is script-friendly and compact.

4. **Fast feedback loops**
   - Unit fixtures model real failure modes.
   - `make` targets support one-command local validation.

5. **Avoid accidental complexity**
   - No runtime DB dependency for canonical knowledge.
   - No heavy framework for doctor/test tooling.

6. **Safety boundaries are code, not just docs**
   - Approval gates for active/stable decisions/procedures.
   - Immutable raw source policy enforced by workflow conventions.
