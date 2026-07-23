# DOCTOR.md — VAULT-FAST Diagnostic Guide

## Purpose

Diagnose throughput and normalization failures quickly so Inbox flow remains healthy and BRAIN seeding quality stays high. Every failure has a code and a concrete recovery path.

## Fast Triage

1. Measure Inbox count and oldest item age.
2. Sample 5 recent drafts for schema compliance.
3. Run doctor:
   ```bash
   python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict
   ```
4. Classify failures by code. Fix in priority order: F1 → F2 → F3 → F4 → F5 → F6.

## Common Failure Modes

**F1 — Empty sources on drafts**
- Symptom: Drafts with `sources: []` or no `sources` key.
- Cause: Draft written from memory or template filled without reading source file.
- Recovery: Open the original source item. Add its path to `sources`. If no source file exists, escalate to VAULT.
- Prevention: Never populate frontmatter before reading the source file.

**F2 — Missing required frontmatter fields**
- Symptom: Doctor reports missing `created`, `updated`, `type`, `status`, `title`, `owner`, or `confidence`.
- Cause: Template partially filled; batch pressure leading to shortcuts.
- Recovery: Open draft, populate all missing fields from source evidence. Do not invent values.

**F3 — Invalid enum values**
- Symptom: Unrecognized `type`, `status`, or `confidence` value.
- Cause: Typo or non-standard value used outside template.
- Recovery: Correct to valid enum from `skills/vault/schemas/frontmatter.md`.

**F4 — Inbox staleness (age > threshold)**
- Symptom: Oldest Inbox item age exceeds 7 days.
- Cause: Processing backlog, missed batch, or item that keeps getting deferred.
- Recovery: Triage oldest items specifically. Classify, draft, or escalate each. Never skip oldest items to process new ones.

**F5 — Incomplete escalation packet**
- Symptom: Escalation draft missing source path, reason, candidate type, or unresolved questions.
- Cause: Escalation created quickly without completing required fields.
- Recovery: Open escalation draft. Fill all required fields. VAULT cannot safely process incomplete packets.

**F6 — BRAIN response coverage gap**
- Symptom: `vault_paths` input has more items than `processed` + `escalations` combined.
- Cause: File read error silently skipped, or item dropped during processing.
- Recovery: Identify which paths are missing. Re-process or create escalation for each. Update response.

## Escalation

Escalate to VAULT when:
- Multiple drafts fail the same schema check across consecutive batches (systemic template issue).
- An escalation packet involves decision/procedure content heading toward `active` or `stable`.
- Cross-client content is detected in any source file.
- Inbox oldest age has been >14 days despite processing (blocking item).

## Doctor Report Format

A VAULT-FAST doctor report includes:

- **Backlog metrics**: Inbox item count, oldest age, trend (improving/stable/worsening)
- **Draft quality findings**: schema compliance rate for sampled drafts, failure codes found
- **Escalations created**: count and list of escalation packet paths
- **Recommended next batch scope**: item count and type filter for next run
- **Verdict**: `green` (zero issues), `yellow` (warnings), `red` (errors)
