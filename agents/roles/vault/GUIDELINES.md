# GUIDELINES.md — VAULT Quality Rules

## Source of Truth Rules

- `raw/` is immutable evidence. Never edit after ingest. Never write canonical output there.
- `wiki/` holds all durable canonical knowledge. No canonical notes outside `wiki/`.
- Every canonical claim requires a non-empty `sources` list with real file paths.
- Relationships must be expressed as `[[wikilinks]]` — not tags, not prose references.
- A note with `status: active` or `status: stable` is authoritative. Treat any change to it as high-impact.

## Frontmatter Rules

Required fields — all must be present and non-empty:
- `created`: ISO-8601 date
- `updated`: ISO-8601 date, must reflect the current edit
- `type`: one of `concept | decision | entity | insight | meeting | procedure | project`
- `status`: one of `draft | active | stable | archived | deprecated`
- `title`: matches filename intent
- `sources`: list of `raw/` paths or external references; must be non-empty
- `related`: list of `[[wikilinks]]`; empty list is acceptable if no links exist yet
- `owner`: agent or human responsible for this note
- `confidence`: one of `high | medium | low`

Optional fields: `tags`, `clients`, `projects`

## Classification Policy

Assign classification from source material context:
- `public`: safe to share externally, no sensitive content
- `internal`: internal Ralleh use only, not for clients
- `confidential`: client-specific data, business-sensitive
- `restricted`: legal/compliance/security-sensitive, requires human approval before sharing

When classification is ambiguous: assign the more restrictive level and flag for review. Never downgrade without explicit authorization.

## Confidence Thresholds

| Confidence | Criteria |
|------------|----------|
| `high` | Complete frontmatter, ≥1 real source, no open conflicts, strict doctor passes |
| `medium` | Minor gaps (weak source, ≤1 missing related link), no approval failures |
| `low` | Draft status, partial sources, or documented open questions |

Return `low` when in doubt. Never inflate confidence.

## Approval Gate Rules

**Mandatory approval metadata** for any note where:
- `type: decision` AND `status: active` or `status: stable`
- `type: procedure` AND `status: active` or `status: stable`

Required approval fields: `approved_by`, `approved_at`, `approval_ref` (or equivalent schema fields per project convention).

Do not finalize, promote, or return to BRAIN without approval metadata present. Flag violations immediately.

## Staleness and Archival

- A `wiki/` note not updated in >90 days with `status: active` should be flagged for review.
- A decision that has been superseded must be set to `status: deprecated` with a `superseded_by` reference.
- `wiki/log.md` must have an entry for every crystallization operation — append-only, never edit past entries.

## Quality Bar

A VAULT output is production-grade only when all of these pass:
1. All required frontmatter fields present and valid enum values
2. `sources` non-empty and paths are real files
3. Uncertainty stated explicitly — not hidden
4. Wikilinks resolved or queued with an explicit follow-up task
5. Approval gates compliant for active/stable decisions and procedures
6. Strict doctor returns zero errors on the affected root
7. `wiki/index.md` and `wiki/log.md` updated where crystallization occurred
