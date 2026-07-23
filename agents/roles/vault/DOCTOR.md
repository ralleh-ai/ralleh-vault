# DOCTOR.md — VAULT Diagnostic Guide

## Purpose

Provide fast, repeatable diagnosis of vault quality regressions and safe, minimal remediation steps. Every failure has a code, a priority, and a concrete recovery path.

## Fast Triage

1. Run strict doctor on target root:
   ```bash
   python3 skills/vault/scripts/vault_doctor.py --vault-root vault/ --strict
   ```
2. Classify failures by code (see below). Higher severity first.
3. Fix highest blast-radius issues first: broken links, missing frontmatter, approval failures.
4. Re-run doctor after each fix group. Never mark session complete with errors present.

**Triage priority order:** F1 → F2 → F3 → F4 → F5 → F6 → F7 → F8

## Common Failure Modes

**F1 — Broken wikilinks**
- Symptom: Doctor reports unresolved `[[WikiLink]]` targets.
- Cause: Note moved/renamed without updating references.
- Recovery: Find the new location of the target note. Update all `related` fields referencing the old path. Re-run doctor.
- Blast radius: High — affects every note that references the broken link.

**F2 — Missing required frontmatter**
- Symptom: Doctor reports missing `created`, `updated`, `type`, `status`, `title`, `sources`, `related`, `owner`, or `confidence`.
- Cause: Template shortcut taken, partial draft committed.
- Recovery: Open note, populate all missing fields from source evidence. Do not invent values — use `low` confidence if uncertain.

**F3 — Empty sources**
- Symptom: `sources: []` or `sources` key absent on a canonical note.
- Cause: Note written from memory without citing evidence.
- Recovery: Find the originating `raw/` file. Add its path to `sources`. If no source exists, set `confidence: low` and document why.

**F4 — Approval gate violation**
- Symptom: Note has `type: decision` or `type: procedure` with `status: active` or `stable` but no approval metadata.
- Cause: Status upgraded without completing approval workflow.
- Recovery: Do not edit the note content. Add approval metadata fields: `approved_by`, `approved_at`, `approval_ref`. If approval was not granted, downgrade `status` to `draft`.

**F5 — Invalid enum values**
- Symptom: Doctor reports unrecognized value for `type`, `status`, or `confidence`.
- Cause: Typo or non-standard value used.
- Recovery: Correct the value to an allowed enum. Valid sets in `skills/vault/schemas/frontmatter.md`.

**F6 — Stale inbox**
- Symptom: `Inbox/` contains items older than policy threshold (default: 7 days).
- Cause: Processing lag, oversized batch scope, or missed escalation.
- Recovery: Triage oldest items first. Process or escalate each. If backlog is large, delegate batch to VAULT-FAST.

**F7 — Log staleness**
- Symptom: `wiki/log.md` not updated after recent crystallization operations.
- Cause: Crystallization happened without appending a log entry.
- Recovery: Append a backdated entry for each unlogged crystallization. Include note title, operation type, date.

**F8 — Index drift**
- Symptom: `wiki/index.md` references notes that do not exist, or notes exist that are not indexed.
- Cause: Notes added or removed without updating the index.
- Recovery: Diff actual `wiki/` contents against `wiki/index.md`. Add missing entries. Remove dead ones.

## Escalation

Escalate to human when:
- Legal or compliance classification is unclear and cannot be safely defaulted to `restricted`.
- Cross-client boundaries are implicated (F4 with `clients:` field conflict).
- Conflicting authoritative sources cannot be ranked or reconciled with available evidence.
- A broken link target appears to have been intentionally deleted (data loss risk).

Always produce an escalation packet (see `PATTERNS.md`) before handing off.

## Doctor Report Format

A complete VAULT doctor report includes:

- **Summary metrics**: total note count, broken link count, missing frontmatter count, approval gate violations, inbox count and oldest age
- **Issues by code**: F1 through F8, count of each
- **Remediation list**: per-issue file path and suggested fix
- **Verdict**: `green` (zero issues), `yellow` (warnings only), `red` (one or more errors)

For BRAIN callers: if vault health is `red`, include `vault_health: "red"` in the query response and surface the top issue.
