# DOCTOR.md — VAULT-FAST Diagnostic Guide

## Purpose
Diagnose throughput and normalization failures quickly so Inbox flow remains healthy.

## Fast Triage
1. Measure inbox count and oldest age.
2. Sample recent drafts for schema compliance.
3. Check for recurring link or source omissions.
4. Escalate unresolved ambiguity clusters.

## Common Failure Modes
- Missing required frontmatter due rushed drafting.
- Empty `sources` on drafts.
- Incomplete handoff packets.
- Inbox staleness from oversized batch scope.

## Escalation
Escalate to VAULT when:
- contradictory sources block safe classification
- candidate note type is unclear with material impact
- output touches decision/procedure governance

## Doctor Report Format
- Backlog metrics (count + oldest age)
- Draft quality findings
- Escalations created
- Recommended next batch scope
