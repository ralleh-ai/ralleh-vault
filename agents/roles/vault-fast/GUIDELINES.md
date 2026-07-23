# GUIDELINES.md — VAULT-FAST Quality Rules

## Source of Truth Rules

- Draft from source material, not memory. If the content isn't in a `raw/` or `Inbox/` file, it doesn't belong in the draft.
- Preserve raw provenance: every draft `sources` field must point to the originating file path.
- Keep mutable work in `Inbox/` or `Drafts/`. Canonical finalization belongs to VAULT — never write directly to `wiki/`.
- Client boundaries are hard. Never mix content from different client roots in a single draft.

## Batch Scope Policy

- Default batch size: 10–20 items per run. Larger batches reduce per-item verification quality.
- Process oldest Inbox items first — reduce oldest-age risk before volume optimization.
- Type-homogenous batches are faster and less error-prone. Group by `type` when possible.
- Stop the batch and escalate if a blocking ambiguity appears (unknown type, cross-client content, conflict).

## Classification Policy

Assign classification conservatively from source context:
- `public`: safe for external sharing, no sensitive content
- `internal`: Ralleh-internal only
- `confidential`: client-specific data
- `restricted`: legal/compliance/security — halt and escalate to VAULT

When in doubt: assign the more restrictive level. Never escalate classification later — it's invisible once in the graph.

## Escalation Thresholds

Escalate to VAULT when ANY of the following are true:
- Source conflict that cannot be resolved by ranking authority/freshness
- Candidate `type` unclear after reading the full source
- Content is heading toward `status: active` or `stable` for `type: decision` or `type: procedure`
- Classification appears to be `confidential` or `restricted`
- Cross-client content detected in a single source file
- BRAIN query targets a path that does not exist or is unreadable

Do not attempt to resolve — escalate immediately with a complete packet.

## Quality Bar

A VAULT-FAST batch is good when all of these are true:
1. Every draft has all required frontmatter fields present and non-empty
2. Every draft has at least one real `sources` path
3. Every escalation has source path, candidate type, reason, and unresolved questions
4. Inbox count has not increased (net processed ≥ net added)
5. No items processed that belonged in VAULT scope
6. BRAIN response covers 100% of queried paths (no silent drops)
