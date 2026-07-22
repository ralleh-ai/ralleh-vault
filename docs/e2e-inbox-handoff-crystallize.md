# End-to-End Scenario: Inbox → Handoff → Crystallize

This scenario demonstrates the canonical operating loop.

## Input

- `vault/raw/transcripts/client-alpha-kickoff.txt`
- `vault/Inbox/2026-07-22-alpha-kickoff-batch.md`

## Stage A — Process (VAULT-FAST)

1. Read batch note and source transcript.
2. Produce draft project note:
   - `vault/wiki/Projects/Client Alpha - Onboarding.md`
3. Produce escalation handoff note for unresolved decision:
   - `vault/wiki/Resources/Handoff - Pricing Strategy Open Question.md`

### Example handoff payload

- Item: `vault/raw/transcripts/client-alpha-kickoff.txt`
- Candidate type: `decision`
- Why escalate: conflicting signals on pricing model
- Open questions:
  - annual vs monthly contract default?
  - discount guardrails?
- Source refs:
  - `raw/transcripts/client-alpha-kickoff.txt`

## Stage B — Crystallize (VAULT)

1. Resolve conflict with source citations.
2. Create canonical decision note:
   - `vault/wiki/Decisions/Client Alpha Pricing Model.md`
3. Update links in project note.
4. Update `wiki/index.md` and append `wiki/log.md`.

## Stage C — Validation

Run doctor:

```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root vault --strict
```

Expected outcome:
- no broken links
- no missing frontmatter
- approval gate satisfied for active/stable decision
- inbox trend remains controlled

## Operational metric targets

- Inbox oldest item age < 72h
- 0 approval-gate violations
- 0 broken wikilinks
- 100% canonical notes with non-empty `sources`
