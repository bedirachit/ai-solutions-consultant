# Scorecards

Anchors for every dimension: **5** client-ready, no edits; **4** minor polish only; **3** clear gaps a client would notice; **2** significant rework; **1** not fit for purpose.

## Understanding Document
| Dimension | What 5 looks like |
|---|---|
| Completeness | All template sections addressed; scope in/out explicit |
| Accuracy & sourcing | Facts sourced; assumptions `A-n`; unknowns `Q-n` with owners |
| Requirements quality | FR/NFR numbered, testable, prioritized |
| Current vs target clarity | Step-by-step, what changes vs stays is obvious |
| Risk & dependency coverage | Material risks with mitigations and owners |
| Executive readability | Half-page summary a sponsor can confirm in 2 minutes |
Must-fix: invented figures; missing scope boundaries; no open-questions list.

## Architecture
| Dimension | What 5 looks like |
|---|---|
| Traceability | Every component and decision traces to FR/NFR ids |
| Soundness | Patterns fit sync/async, read/write, HITL needs; capacity estimated |
| Trade-offs | Major choices have solves / worsens / when-to-change; ADRs recorded |
| Security & compliance | Least privilege, private connectivity, governed AI access, data protection, audit |
| Resilience & operability | No unhandled SPOF; fallbacks; DR; observability and SLOs |
| CSP fidelity | Real, current service names; landing-zone rules respected; on-prem boundary clear |
| AI governance | Grounding, guardrails, evaluation, human-in-the-loop, model risk |
Must-fix: direct AI access to systems of record bypassing integration layer (unless justified); no fallback path; invented vendor capabilities; CSP named but generic components used.

## Diagram
| Dimension | What 5 looks like |
|---|---|
| Icon fidelity | Official icon set of the stated CSP throughout, one generation |
| Correctness | Matches architecture write-up exactly |
| Structure | Proper nesting (cloud → region → network → subnet), trust boundaries |
| Flow clarity | Labelled, numbered edges; left-to-right reading |
| Readability | ≤ ~40 shapes, no crossings through icons, legible at slide size |
| New vs existing | Clearly distinguished with legend |
| Delivery | "Open in draw.io" link + .drawio file provided |
Must-fix: missing official icons for a named CSP; missing link; components not in the architecture.

## Executive deck
| Dimension | What 5 looks like |
|---|---|
| Storyline | Ghost deck (titles only) tells the full story; answer first |
| Action titles | Every content slide has a takeaway title, consistent grammar |
| Evidence | Each slide's body proves its title; sources on every slide |
| Audience fit | C-suite: outcomes, risk, decisions; detail pushed to appendix |
| Visual quality | Exhibits over bullets; consistent layout; brand/design system applied; nothing overflows |
| The ask | Decisions requested are explicit, owned and dated |
| Consistency | Names, numbers and scope match the architecture and understanding document |
Must-fix: topic-label titles on C-suite slides; invented numbers; missing ask; inconsistency with approved architecture.
