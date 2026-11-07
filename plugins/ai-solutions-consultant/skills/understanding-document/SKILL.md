---
name: understanding-document
description: >
  This skill should be used when the user asks for an "understanding document",
  "requirements understanding", "our understanding of the requirement", "discovery
  summary", "scope document", "as-is / to-be write-up", or when the
  solutions-consultant workflow needs a detailed written record of what was
  understood before architecture begins. It produces a structured, client-ready
  document that confirms scope, current state, target state, requirements,
  assumptions, risks and open questions.
metadata:
  version: "0.1.0"
---

# Understanding Document

The Understanding Document is the contract of understanding between consultant
and client. It must let a reader who missed every meeting confirm, correct or
sign off the scope. Write it before the architecture; the architecture cites it.

## Build it

1. Gather inputs: the request, discovery answers ("Confirmed / Assumed / Open"),
   attached materials, prior artifacts.
2. Follow `assets/understanding-document-template.md` section by section. Keep
   every heading; write "Not applicable — [reason]" rather than deleting one.
3. Write facts as facts with their source ("per discussion on [date]", "per
   attached process map"). Write assumptions as assumptions with an `A-n` id.
   Write unknowns as open questions with a `Q-n` id, an owner and a needed-by
   date placeholder.
4. Number requirements (`FR-n`, `NFR-n`) so the architecture and deck can trace
   to them.
5. Describe the current and target processes as numbered steps, and where it
   helps, as a simple flow (a Mermaid flowchart or a draw.io diagram via
   `csp-architecture-diagram`).
6. Open with a half-page executive summary in plain language: problem,
   proposed direction, scope of phase 1, top risks, decisions needed.

## Style

- Plain, specific, client-facing. No marketing language.
- Tables for inventories (systems, integrations, requirements, risks).
- Never invent volumes, costs, dates or names — use `[TBC]` placeholders and
  list them as open questions.
- Mark anything confidential as such in the header.

## Format

Produce it as a living doc when a docs artifact type or Docs connector is
available; otherwise as Markdown, or .docx when Word is requested. Send it to
the partner review gate before presenting it as final.

## Asset

- `assets/understanding-document-template.md` — the section template.
