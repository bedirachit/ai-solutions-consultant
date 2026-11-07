# Writing the Solution Architecture Document

The structure in `assets/architecture-document-template.md` combines four established practices:

| Practice | What we take from it |
|---|---|
| **arc42** (Starke & Hruschka) — 12-section architecture template | Goals, constraints, context and scope, solution strategy, building-block view, runtime view, deployment view, cross-cutting concepts, decisions, quality scenarios, risks, glossary |
| **C4 model** (Simon Brown) — zoom levels for diagrams | Level 1 system context diagram; level 2 container diagram; components only where needed |
| **Design docs at Google** | Context and scope; goals and **non-goals**; the design itself; **alternatives considered** with why they lost; cross-cutting concerns |
| **ISO/IEC/IEEE 42010** | Name the stakeholders and their concerns; give each a view that answers them ("Who should read what") |

## The seven rules

1. **Explain in place.** The first time an option, system, product, acronym or team appears, say what it is in that same sentence. "Option B" alone is never acceptable; write "Option B — the AI platform runs in the bank's own Azure subscription". Prefer descriptive option names and use letters only as a short label after the name.
2. **No forward references in the opening sections.** Sections 1–2 must make sense with nothing else read. Do not cite "see Section 5" as a substitute for an explanation; give the one-line explanation, then point to detail.
3. **Picture first, then words.** Section 2 opens with a simple flow diagram (5–8 boxes, left to right, plain names, numbered arrows, new parts highlighted) followed by the same steps in numbered sentences. Every later diagram is introduced by one sentence saying what to look at and followed by a numbered walkthrough or step table.
4. **Diagrams must render as pictures in the delivered format.** Before delivery, check each diagram shows as an image, not as code:
   - Living doc / docs tool: use its native diagram support, or insert a PNG exported from draw.io.
   - Word (.docx) and PDF: insert PNG/SVG images (export from draw.io; or render Mermaid to PNG with a Mermaid CLI such as `mmdc` when available).
   - Markdown viewed on GitHub or similar: Mermaid code blocks render; elsewhere, use images.
   Keep the Open in draw.io link under each draw.io image.
5. **Architecture is the core.** Sections 7–11 (building blocks, runtime, deployment, integration, cross-cutting) carry most of the length. Background stays short.
6. **Write for the client's engineers.** Use their system names, short sentences, active voice, concrete nouns. No sales language, no consulting filler ("leverage", "synergies", "best-in-class").
7. **Quality as scenarios.** State non-functional requirements as testable scenarios: "When X happens, the system does Y within Z".

## Self-check before review
- [ ] Could a new client engineer explain the solution after reading only Sections 1–2?
- [ ] Is every option, acronym and system explained where it first appears?
- [ ] Is there a simple flow diagram near the top, visible as a picture in this format?
- [ ] Does every component in the diagrams appear in the catalogue, and vice versa?
- [ ] Does every journey have a diagram, a step table and a failure path?
- [ ] Is the recommendation described by what it is, not only by its label?

## Sources
- arc42 template and docs: https://docs.arc42.org/home/ · https://examples.arc42.org/sections/
- C4 model overview: https://icepanel.io/blog/what-is-the-c4-model
- Design Docs at Google (Malte Ubl): https://www.industrialempathy.com/posts/design-docs-at-google/
- ISO/IEC/IEEE 42010 overview: https://Www.wikipedia.org/wiki/Software_architecture_description
