---
name: executive-deck
description: >
  This skill should be used when the user asks for "a deck", "slides", "a PPT",
  "a PowerPoint", "a presentation for leadership / C-suite / the board / the
  steering committee", "a BCG / McKinsey style deck", "an architecture deck", or
  wants a solution, architecture or recommendation turned into a storyline. It
  builds a top-tier consulting-style deck: answer first, action titles, one
  message per slide, exhibits over bullets, sources on every slide, and a clear
  ask.
metadata:
  version: "0.1.0"
---

# Executive deck (top-tier consulting style)

## Storyline first

1. **Define the governing thought** — the one sentence the audience must
   accept ("A single AI layer automates the contact center without replacing
   core systems").
2. **Choose the structure** — Situation → Complication → Resolution, or
   answer-first pyramid with 3–4 supporting arguments. For approvals, end on
   the decisions requested.
3. **Write the ghost deck** — slide titles only, read in sequence. If the titles
   alone don't tell the story, fix them before building any slide.
4. **Pick an exhibit per slide** from `references/slide-patterns.md`.

## Slide rules

- **Action titles**: a full-sentence takeaway (≤ 2 lines), not a topic label.
  Same grammar across the deck.
- **One message per slide**; the body proves the title, nothing else.
- **Exhibits beat bullets**: layered architecture, flows, before/after,
  tables, 2×2s, timelines, big numbers.
- **Tracker / eyebrow** label above the title showing the section.
- **Source / footnote line** on every content slide; page numbers.
- **Numbers**: never invent. Unknown figures are `[TBC]` placeholders, listed
  in the hand-off message.
- **Executive summary** as slide 2; **decisions requested** and **next steps**
  at the end.
- **Speaker notes** on every slide: what to say, and likely questions.
- For architecture decks: one context-level picture for executives; push
  physical diagrams to the appendix.
- Use the user's design system, brand or template when one is named; otherwise
  a restrained palette (one dark, one light, one accent) and one sans-serif face.

## Build

- When the session lists a **Slides** artifact type, create the deck from it
  and follow that type's instructions.
- Otherwise build a **.pptx** with the pptx skill.
- Embed draw.io diagrams as exported PNG/SVG images; link the editable draw.io
  file in the speaker notes.

## Before the partner gate, self-check

- Read the titles in sequence: does the story stand alone?
- Every slide: title is a takeaway, body supports it, source present.
- No text below the minimum readable size; nothing overflows.
- The ask is explicit and owned.

## Reference

- `references/slide-patterns.md` — slide archetypes with layouts and when to use them.
