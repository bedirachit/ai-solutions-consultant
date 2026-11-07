---
name: discovery-questions
description: >
  This skill should be used when a solution, architecture or AI-integration request
  is under-specified and needs clarifying questions before design: "ask me what you
  need to know", "what questions should we ask the client", "scope this", "clarify
  requirements", "discovery for…", or whenever the solutions-consultant workflow
  reaches its clarify step. It selects the few questions whose answers change the
  design and asks them in structured rounds.
metadata:
  version: "0.1.0"
---

# Discovery and clarifying questions

Ask only the questions whose answers would change the architecture, the scope or
the recommendation. A good discovery round feels short to the user and saves a
redesign later.

## Method

1. **Extract what is already known.** List facts from the request, attached
   files, prior conversation and connected knowledge sources (docs, wiki). Do
   not ask for anything already given.
2. **Find the design-changing unknowns.** Walk the dimensions in
   `references/question-bank.md` and mark each unknown as *changes design*,
   *changes estimate only*, or *nice to know*. Ask only the first group; turn
   the rest into stated assumptions.
3. **Prioritize.** Rank by impact × uncertainty. Typical top items: the business
   outcome and success metric; the target cloud / hosting constraint; data
   sensitivity and regulation; integration points with systems of record; volume
   and latency; the audience and deliverables.
4. **Ask in rounds.** Use AskUserQuestion: at most 4 questions per round, each
   with 2–4 concrete options, the recommended option first and marked
   "(Recommended)", and a one-line description of the consequence of each
   option. Allow multi-select where choices are not exclusive (e.g. clouds,
   channels). At most two rounds.
5. **Record.** After answers arrive, write a short "Confirmed / Assumed / Open"
   list. Carry it into the Understanding Document.

## Question quality bar

- Each question names the decision it informs ("so I can pick between managed
  and self-hosted vector search").
- Options are mutually exclusive and specific — never "Other" or "None"
  (the tool adds free text and skip automatically).
- No compound questions; no jargon the audience would not use.
- Stop asking once the remaining unknowns would not change the design.

## When nobody can answer

If the session is unattended or the user skips, proceed with explicit
assumptions, label them in every artifact, and list them as open questions for
the next touchpoint.

## Reference

- `references/question-bank.md` — question bank by dimension, including
  CSP-specific and AI-specific questions.
