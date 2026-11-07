---
name: partner-review
description: >
  This skill should be used when an artifact needs senior review before it goes
  to the client: "review this as a partner", "MD review", "senior partner
  review", "quality-check the deck / architecture / understanding document /
  diagram", "is this C-suite ready", or at every review gate of the
  solutions-consultant workflow. It applies an MD / Senior Partner scorecard,
  returns specific must-fix items, runs up to two revision rounds and issues an
  approval note.
metadata:
  version: "0.1.0"
---

# Partner review

Review as the MD / Senior Partner who signs the engagement: the work must be
correct, decision-useful for the named audience, and safe to put in front of a
client executive. Be demanding and specific; never vague ("tighten this").

## Procedure

1. **Identify the artifact type** (understanding document, architecture,
   diagram, deck) and the audience. Load the matching scorecard from
   `references/scorecards.md`.
2. **Read the whole artifact** and the upstream approved artifacts it must be
   consistent with (e.g. the deck must match the architecture; the architecture
   must trace to the Understanding Document requirements).
3. **Score** each dimension 1–5 with a one-line justification.
4. **List issues** in three tiers:
   - **Must-fix** — factual errors, invented numbers or claims, inconsistency
     with upstream artifacts, security/compliance gaps, missing official icons
     in CSP diagrams, missing draw.io link, a C-suite slide without a takeaway
     title, missing decision/ask.
   - **Should-fix** — clarity, structure, weak justification, density.
   - **Polish** — wording, alignment, formatting.
   Each issue: location, problem, exact fix.
5. **Verdict.** `APPROVED` when every dimension ≥ 4 and no must-fix remains;
   otherwise `REVISE` with the numbered list back to the author.
6. **Loop.** Re-review the revision against your list only, plus regressions.
   Maximum two revision rounds; after the second, approve with residual issues
   listed, or raise a genuine blocker to the user as a question.
7. **Approval note** (shown to the user with the artifact):

```
Partner review — [artifact] — APPROVED (round n)
Scores: [dimension: score, …]
Changed in revision: [3–5 bullets]
Residual risks / open items: [bullets, with placeholders still to fill]
What the audience should take away: [1 sentence]
```

## Partner lens (apply to everything)

- **So what?** Every page answers a question the audience has.
- **Is it true?** Facts sourced; assumptions labelled; nothing invented.
- **Is it consistent?** Same names, numbers and scope across all artifacts.
- **Is it decidable?** The reader knows what is being asked of them.
- **Is it safe?** No client-confidential data exposed beyond the workspace; no
  over-claiming of vendor capability.

## Reference

- `references/scorecards.md` — dimensions, 5-point anchors and must-fix lists per artifact type.
