# Scorecards

Anchors for every dimension: **5** client-ready, no edits; **4** minor polish only; **3** clear gaps a client would notice; **2** significant rework; **1** not fit for purpose.

## Research Brief
| Dimension | What 5 looks like |
|---|---|
| Relevance | Research questions match the engagement; implications lead |
| Evidence quality | Mostly grade A/B sources; vendor claims labelled; dates given |
| Coverage | Similar implementations, reference architectures, best practices, pitfalls, regulation as applicable |
| Citation integrity | Every fact and number linked to a source that says it |
| Confidentiality | No client names or confidential details in the brief's search trail |
| Decision usefulness | Clear, specific implications for the design; gaps and confidence stated |
Must-fix: any uncited or unverifiable claim; invented case study or statistic; client-confidential detail in queries.

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
| Self-contained explanations | Every option, system, product and acronym explained where it first appears; no bare labels ("Option B") or forward references in Sections 1–2 |
| Client-team readability | Written for the client's architects, engineers and security team: their systems and terms, no filler |
| Architecture depth | Architecture is the bulk of the document; every component has role, purpose, responsibilities, interfaces, technology, owner, scaling/failure, security, rationale |
| Simple flow diagram | Section 2 opens with a simple flow (5–8 boxes, plain names, numbered arrows) **visible as a picture**, followed by the steps in words |
| Journey flows | One rendered flow diagram per key journey, numbered steps matching a step table; failure paths described |
| Traceability | Every component and decision traces to FR/NFR ids |
| Soundness | Patterns fit sync/async, read/write, HITL needs; capacity estimated |
| Trade-offs | Major choices have solves / worsens / when-to-change; ADRs recorded |
| Security & compliance | Least privilege, private connectivity, governed AI access, data protection, audit |
| Resilience & operability | No unhandled SPOF; fallbacks; DR; observability and SLOs |
| CSP fidelity | Real, current service names; landing-zone rules respected; on-prem boundary clear |
| AI governance | Grounding, guardrails, evaluation, human-in-the-loop, model risk |
Must-fix: no simple flow diagram near the top, or any diagram showing as code instead of a picture; an option, system or acronym used before it is explained; no flow diagram for a key journey; a component without its role and purpose explained; document mostly context rather than architecture; direct AI access to systems of record bypassing integration layer (unless justified); no fallback path; invented vendor capabilities; CSP named but generic components used.

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
