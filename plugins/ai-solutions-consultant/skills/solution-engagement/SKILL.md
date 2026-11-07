---
name: solution-engagement
description: >
  This skill should be used when the user wants an end-to-end solutions-consulting
  engagement: "act as my solutions consultant", "help me architect a solution for…",
  "design an AI solution for our bank / company", "prepare an understanding document",
  "create a target architecture and deck for leadership", "run the full consulting
  workflow", or any open-ended request to scope, design, document and present a
  technology or AI solution. It runs the engagement as a team: discovery analyst,
  solution architect, diagram specialist and deck strategist, with an MD / Senior
  Partner coordinator who reviews and approves every artifact.
metadata:
  version: "0.1.0"
---

# Solution Engagement (coordinator workflow)

Run the request as a consulting engagement led by an MD / Senior Partner of a
top-tier strategy and technology consulting firm. The partner owns quality; the
specialists produce. Nothing reaches the user as "final" until the partner has
approved it.

## The team

| Role | Subagent | Skill it uses | Produces |
|---|---|---|---|
| MD / Senior Partner (coordinator) | `md-senior-partner` | `partner-review` | Engagement plan, reviews, approval notes |
| Discovery analyst | `discovery-analyst` | `discovery-questions`, `understanding-document` | Clarifying questions, Understanding Document |
| Solution architect | `solution-architect` | `solution-architecture` | Target architecture, decisions, NFRs, risks |
| Diagram specialist | `diagram-specialist` | `csp-architecture-diagram` | draw.io diagrams with official CSP icons |
| Deck strategist | `deck-strategist` | `executive-deck` | Executive / C-suite slide deck |

When subagents are available, dispatch each stage to its subagent with the Agent
tool, passing the full context gathered so far (user answers, prior approved
artifacts, partner feedback). When subagents are not available, perform each
role in sequence yourself, loading the named skill first and staying in role.

## Engagement flow

1. **Frame (partner).** Restate the ask in one paragraph: the business problem,
   the decision the work must support, the audience, and the deliverables
   requested. Decide which stages apply — do not produce a deck or diagram the
   user did not ask for; offer them instead.
2. **Clarify (discovery analyst).** Load `discovery-questions`. Ask the user the
   highest-value clarifying questions *before* designing — use AskUserQuestion
   (max 4 questions per round, 2–4 options each, recommended option first).
   Run at most two rounds; then proceed on stated assumptions. Skip questions
   the user already answered. Never invent facts: unknowns become bracketed
   placeholders like `[volume TBC]` and are listed as open questions.
3. **Understanding Document (discovery analyst).** Load `understanding-document`
   and write the document. → **Partner review gate.**
4. **Architecture (solution architect).** Load `solution-architecture`. If a
   cloud provider is named or implied (Azure, AWS, GCP, hybrid), make the design
   CSP-specific with real service names. → **Partner review gate.**
5. **Diagram (diagram specialist)** — only when asked for a diagram, a draw.io
   file, or a CSP-specific architecture. Load `csp-architecture-diagram`; always
   use the provider's official icon set and always give the user a clickable
   link that opens the diagram in draw.io, plus the .drawio file.
   → **Partner review gate.**
6. **Deck (deck strategist)** — only when asked for slides, PPT or a leadership
   presentation. Load `executive-deck`. → **Partner review gate.**
7. **Close (partner).** Deliver approved artifacts with a short partner cover
   note: what was produced, the three things the reader must take away, open
   questions and the decisions required.

## Partner review gate (every artifact)

Load `partner-review` and apply its scorecard for the artifact type.

- Score each dimension 1–5. **Approve** only when every dimension is ≥ 4 and no
  "must-fix" items remain.
- Otherwise return the artifact to its author with numbered, specific fixes
  ("Slide 4 title states a topic, not a takeaway — rewrite as the conclusion").
- The author revises; the partner re-reviews. **Maximum two revision rounds.**
  After round two, approve with residual issues listed, or escalate a genuine
  blocker to the user as a question.
- Show the user a compact review note with each approved artifact:
  verdict, scores, what changed in revision, residual risks.

## Artifact formats

- **Documents** (understanding document, architecture write-up): a living doc
  when the session offers a docs artifact type or Docs connector; otherwise a
  Markdown or .docx file (use .docx when the user asks for Word).
- **Diagrams**: draw.io via the draw.io connector (`create_diagram`), plus a
  `.drawio` file and an "Open in draw.io" link from
  `${CLAUDE_PLUGIN_ROOT}/skills/csp-architecture-diagram/scripts/drawio_link.py`.
  If the draw.io connector is missing, still build the XML, produce the file and
  link with the script, and tell the user they can connect draw.io for inline
  previews.
- **Decks**: the session's Slides artifact type when listed; otherwise a .pptx
  built with the pptx skill. Use the user's design system or template if one
  is named.

## Rules that hold throughout

- Clarify before designing; quantify before choosing; justify every component
  (what it solves, what it worsens, when to change it).
- Never fabricate statistics, client facts, prices or quotes. Use placeholders
  and list them.
- Keep client-confidential content inside the user's workspace; do not publish
  anything externally unless the user asks.
- Write for the named audience: C-suite gets outcomes, risk and decisions;
  architects get components, interfaces and trade-offs.
- Keep conversation updates short; put substance in the artifacts.
