# DOCTOR.md — VAULT Diagnostic Guide

## Purpose
Provide fast, repeatable diagnosis of vault quality regressions and safe remediation paths.

## Fast Triage
1. Run strict doctor on target root.
2. Classify failures: structure, schema, links, staleness, approval gates.
3. Fix highest blast-radius issues first (broken links, missing frontmatter, approval failures).

## Common Failure Modes
- Missing required frontmatter fields.
- Broken wikilinks from moved/renamed notes.
- Empty or weak `sources` in canonical notes.
- Stale inbox indicating processing bottlenecks.
- Active/stable decision/procedure notes missing approval metadata.

## Escalation
Escalate to human/owner when:
- legal/compliance-sensitive classification is unclear
- cross-client boundaries are implicated
- conflicting authoritative sources cannot be reconciled safely

## Doctor Report Format
- Summary metrics (counts, freshness, gate failures)
- Issues by severity
- Warnings with remediation suggestions
- Explicit pass/fail verdict
