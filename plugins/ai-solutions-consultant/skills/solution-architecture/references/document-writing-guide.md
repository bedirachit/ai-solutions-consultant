# Writing a client-ready Solution Architecture Document

The final document goes to the client. It must read like the work of a top-tier
strategy and technology firm: confident, specific, easy to navigate, and about
the **proposed solution only**.

## What goes in, and what stays out

| In the client document | Kept out (internal working material) |
|---|---|
| The proposed solution, explained fully | Options considered, comparisons, scoring |
| Decisions taken, with a one-line rationale (Appendix D) | Debate about rejected alternatives |
| Facts, sourced; assumptions and open items labelled | Research notes, review comments, change logs from drafting |
| Figures and tables that carry the argument | Anything not needed to understand, build, run or approve the solution |

If the client asked for an options analysis, deliver it as a **separate
Options Paper**, not inside this document.

## Length and structure

- **15–20 pages** including figures and tables (about 4,500–6,500 words of body
  text). Follow the page budget in the template. If the scope genuinely needs
  more, move detail to appendices rather than growing the body.
- Use the template's section headings exactly, or a client-specific noun phrase
  (e.g. "5.1 Inbound credit card enquiry").
- Always include a **cover**, **document control**, and a real **table of
  contents** (a TOC field in Word; the document tool's index or outline in a
  living doc; a linked section list in Markdown).
- Number sections (1, 1.1, 1.1.1), figures (Figure 1…) and tables (Table 1…),
  each with a caption. Refer to them by number in the text.

## Consulting-grade writing (pyramid principle)

- **Conclusion first.** Every section opens with a 2–3 sentence key message
  stating what the reader needs to know; the rest supports it.
- **Explain in place.** Every system, product, acronym and term is explained the
  first time it appears, in that sentence. No bare labels.
- **Client voice.** "[Client] will…", "The voice bot reads…". Present tense for
  the design; future tense for delivery.
- **Specific over generic.** Name the systems, protocols, regions and teams.
  Replace adjectives with facts ("encrypted with TLS 1.2" not "highly secure").
- **Short paragraphs** (2–4 sentences), active voice, one idea per paragraph.
- **Consistent terminology.** One name per thing across text, figures and
  tables; the glossary uses the same names.

## Headings and phrasing that make a document look AI-written — never use

- Headings that describe the writing task or echo instructions: "Solution in
  one paragraph", "At a glance", "In plain words", "Simple flow", "Key
  takeaways", "Deep dive", "Let's explore".
- Meta-commentary: "This section describes…", "As mentioned above…", "It is
  important to note…", "In conclusion…".
- Rhetorical framings: "It's not X, it's Y", "Here's the thing", questions as
  headings.
- Filler words: leverage, robust, seamless, cutting-edge, best-in-class,
  holistic, synergy, journey (except customer journeys), unlock, empower.
- Bold label followed by a colon at the start of every bullet; walls of bullets
  where a sentence or table would do; emojis; exclamation marks.
- Template brackets, placeholders in headings, or author notes left in the text.

## Diagrams

- Figure 1 is the simple solution overview flow (5–8 boxes, numbered arrows, new
  components highlighted), followed by the numbered steps in 3.1.
- Every diagram renders as a picture in the delivered format (native diagram
  support in docs tools; PNG/SVG images in Word and PDF; Mermaid only where it
  renders). Keep the "Open in draw.io" link beneath draw.io images.
- Every figure is introduced in the text by number before it appears.

## Self-check before review

- [ ] Proposed solution only; no options or comparisons in the body.
- [ ] Cover, document control, table of contents present; sections, figures and tables numbered with captions.
- [ ] 15–20 pages; page budget respected.
- [ ] No heading or sentence from the "never use" list; no template notes left.
- [ ] Each section opens with its key message.
- [ ] Every system, product and acronym explained at first use; glossary complete.
- [ ] Figure 1 overview flow present and rendered; every journey has a figure, step table and exception handling.
- [ ] Names consistent across text, figures, tables and glossary.

## Sources behind this structure
- arc42 architecture documentation template: https://docs.arc42.org/home/
- C4 model for diagram levels: https://icepanel.io/blog/what-is-the-c4-model
- Design Docs at Google: https://www.industrialempathy.com/posts/design-docs-at-google/
- ISO/IEC/IEEE 42010 (stakeholders, concerns, views): https://Www.wikipedia.org/wiki/Software_architecture_description
- Barbara Minto, *The Pyramid Principle* (conclusion-first structure used by McKinsey and other strategy firms)
