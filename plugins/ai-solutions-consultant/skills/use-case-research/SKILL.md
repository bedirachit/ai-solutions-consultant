---
name: use-case-research
description: >
  This skill should be used when a solution needs outside evidence before or during
  design: "research similar use cases", "how have others implemented this", "best
  practices for…", "reference architecture for…", "case studies", "what are the
  pitfalls", "industry benchmarks", "vendor landscape", or whenever the AI Solutions
  Lead dispatches the discovery analyst. It runs structured web research and
  produces a cited Research Brief.
metadata:
  version: "0.4.0"
---

# Use-case research

Find out how comparable organizations solved the same problem, what the cloud
providers and vendors recommend, what went wrong for others, and what
regulators expect — then say what it means for this design.

## Procedure

1. **Frame research questions** from the brief (4–8). Cover the lenses below
   that apply; skip the rest.
2. **Search** with WebSearch, several queries per question, varied wording
   (problem + industry, problem + cloud provider, "reference architecture",
   "case study", "lessons learned", "best practices", "pitfalls"). Read the
   most relevant pages in full before citing them.
3. **Protect the client.** Queries contain only the generic problem, industry,
   region and technology — never the client's name, internal system names,
   people, volumes or other confidential details.
4. **Grade sources** (see `references/research-brief-template.md`): A primary /
   independent, B vendor or provider documentation, C vendor marketing or press,
   D blogs and forums. Prefer A and B; use C and D only with a label.
5. **Synthesize** into the Research Brief template. Lead with implications for
   the design; keep evidence and inference separate.
6. **Cite everything**: every fact, number and example links to its source with
   publication date. Flag anything older than 3 years for fast-moving topics (AI
   models, cloud services).

## Research lenses

| Lens | Look for |
|---|---|
| Similar implementations | Named organizations in the same or adjacent industry, what they built, scope, results |
| Reference architectures | Cloud-provider architecture centers (Azure Architecture Center, AWS Architecture Center / Solutions Library, Google Cloud Architecture Center), vendor reference designs |
| Best practices | Provider well-architected guidance, vendor implementation guides, standards bodies |
| Pitfalls and failures | Post-mortems, lessons learned, regulator findings, analyst warnings |
| Regulation and risk | Regulator circulars and guidance for the sector and region, AI governance frameworks (e.g. NIST AI RMF, ISO/IEC 42001) |
| Outcomes and benchmarks | Published containment, CSAT, AHT, cost-to-serve, accuracy figures — with context and source |
| Vendor and technology landscape | Options in the market, how they are typically deployed, notable differences |

## Rules

- Never fabricate case studies, customers, statistics or quotes. "No published evidence found" is a valid finding.
- Vendor-claimed results are labelled "vendor-reported".
- Numbers carry their unit, context, date and source; never combine figures from different sources into a new number without saying so.
- Keep it decision-useful: 2–4 pages, implications first.

## Reference

- `references/research-brief-template.md` — brief structure and source-grading rubric.
