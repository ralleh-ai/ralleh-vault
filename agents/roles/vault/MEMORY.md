# MEMORY.md — Lessons & Patterns

# MEMORY.md — Lessons & Patterns

## Knowledge Quality

- **Link rot is the primary decay vector.** Broken wikilinks spread silently. A renamed note can corrupt dozens of `related` entries before anyone notices. Check links before checking anything else.
- **Empty sources is the most expensive defect.** A note with no `sources` is an unsupported assertion. Every downstream agent that cites it inherits the uncertainty. Never ship a canonical note with `sources: []`.
- **`confidence: high` requires evidence, not optimism.** Assign confidence based on source quality: is the source real, is it the primary record, and does the note body faithfully represent it?
- **Staleness compounds silently.** A decision note marked `stable` two years ago may have been superseded by events. Periodic review prevents accumulated drift from causing retrieval errors.

## Workflow Lessons

- **Always read before writing.** The existing note may have context, links, or approval history that must be preserved. Overwriting without reading first destroys institutional memory.
- **Doctor before commit, not after.** Running the doctor at the end of a large batch surfaces errors that require re-reading already-closed files. Run it incrementally.
- **Approval gates are load-bearing.** Skipping approval metadata on a decision note to "clean up later" creates governance debt that is rarely repaid. Enforce at write time.
- **Escalate early, not after failure.** Attempting to resolve a genuinely ambiguous conflict without escalating wastes time and risks producing a false `high` confidence note that BRAIN will trust incorrectly.

## BRAIN Integration Lessons

- **A `confidence: 0.9` response with `source_path: null` is a logic error.** High confidence without a canonical source is a contradiction. Always verify the source file exists before setting confidence above `0.5`.
- **BRAIN caches VAULT responses.** A wrong answer at L3 can persist in BRAIN's cache until TTL expiry. Accuracy matters more than speed.
- **`resolve_conflict` queries require explicit documentation.** Even when the resolution is obvious, write it in the note. Future sessions cannot re-derive the reasoning from the final output alone.

## Operational Patterns

- **Remediate by code, not by vibes.** Use the failure codes in `DOCTOR.md`. Systematic triage by priority prevents the natural tendency to fix easy issues and defer hard ones.
- **Prefer minimal edits.** The smallest edit that passes doctor and preserves graph integrity is the right edit. Large refactors break links.
- **Index and log hygiene is not optional.** BRAIN and retrieval agents depend on `wiki/index.md` for discovery. An out-of-date index causes missed context even when the canonical note exists.
