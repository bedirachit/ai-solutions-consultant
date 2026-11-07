---
name: solution-architecture
description: >
  This skill should be used when the user asks to "design the architecture",
  "create a target architecture", "high-level / logical / physical architecture",
  "how should we integrate AI with our systems", "design a RAG / agent / chatbot /
  voice bot solution", "Azure / AWS / GCP architecture for…", "system design for…",
  "architecture decision", "NFRs", or "trade-offs between options". It covers
  system-design building blocks, enterprise AI-integration patterns, CSP-specific
  service mapping, security and compliance, and produces a justified, stress-tested
  architecture write-up.
metadata:
  version: "0.1.0"
---

# Solution Architecture

Design by reasoning, not by recalling a reference diagram. Every architecture is
a hypothesis that holds until a constraint changes; make the constraints explicit.

## The reasoning loop

1. **Anchor on the Understanding Document.** Cite FR/NFR ids. If there is none,
   run `discovery-questions` first or state assumptions.
2. **Estimate.** Convert "high volume" into numbers: peak QPS / concurrent
   sessions, data size, growth, latency budget. Show the arithmetic briefly.
3. **Choose the integration pattern(s).** Use `references/ai-integration-patterns.md`:
   sync vs async, read vs write, single vs multi-system, human-in-the-loop vs
   autonomous.
4. **Lay out the layers.** Channels → experience / interaction → orchestration
   and AI → integration → systems of record and data → platform (identity,
   security, observability, DevOps). Use `references/building-blocks.md`
   to pick components.
5. **Map to the cloud.** When a CSP is named or implied, use real service names
   from `references/csp-service-map.md`, respect landing-zone rules (hub-spoke,
   private endpoints, gateway-only AI access), and mark what stays on-prem.
6. **Justify each major choice** with the trade-off triple in
   `references/tradeoff-framework.md`: solves / worsens / when to change.
   Record significant choices as ADRs (decision, options considered, rationale,
   consequences).
7. **Stress-test.** Single points of failure, degradation and fallback paths,
   DR (RTO/RPO), security threats (`references/security-compliance.md`),
   AI risks (hallucination, prompt injection, data leakage), cost at 10× volume.
8. **Iterate** on the weakest part, then write the Solution Architecture Document below.

## Write the Solution Architecture Document for the client's team

The reader is the **client's own team**: architects, platform and infrastructure
engineers, security, application owners and delivery leads. Follow
`assets/architecture-document-template.md` and the seven rules in
`references/document-writing-guide.md` (based on arc42, the C4 model, Google
design docs and ISO/IEC/IEEE 42010). The non-negotiables:

1. **Explain in place.** Every option, system, product, acronym and team is
   explained in the sentence where it first appears. Never write "Option B"
   without saying what Option B is; give options descriptive names.
2. **Sections 1–2 stand alone.** The problem, then "the solution at a glance":
   a **simple flow diagram** (5–8 boxes, left to right, plain names, numbered
   arrows, new parts highlighted) followed by the same steps in numbered
   sentences, a new-vs-unchanged table, and the recommended approach described
   by what it is.
3. **Diagrams render as pictures** in the delivered format — check before
   delivery (native diagram support in docs tools; PNG/SVG images in Word and
   PDF; Mermaid only where it renders, e.g. GitHub). Never deliver diagram code
   that shows as text.
4. **Architecture is the core**: context diagram, container view, component
   catalogue, runtime journeys (diagram + step table + failure path),
   deployment, integration, cross-cutting concerns, quality scenarios.
5. Run the self-check in the writing guide before sending for review.

When draw.io diagrams are requested, hand `csp-architecture-diagram` the
simple flow, the context view, the container view and each journey, with the
component list, groupings and numbered edges.

## Guardrails

- Never name a tool without its trade-off.
- Least privilege by default: read-only where reads suffice, write-only for
  case creation, no direct database access from AI components.
- Every AI model call goes through one governed path (AI gateway / API
  management) when the client has one.
- Design for failure: every automated path has a human or legacy fallback.
- Do not invent product capabilities, prices or SLAs; flag them `[verify with vendor]`.

## Asset

- `assets/architecture-document-template.md` — the Solution Architecture Document template.

## References

- `references/document-writing-guide.md` — the seven writing rules, the research behind the structure, and the pre-review self-check.

- `references/building-blocks.md` — system-design building blocks with when-to-use and stress behavior.
- `references/ai-integration-patterns.md` — enterprise AI patterns (RAG, agentic tool use, MCP, event-driven, gateway, contact-center AI).
- `references/csp-service-map.md` — equivalent services across Azure, AWS, GCP and on-prem.
- `references/tradeoff-framework.md` — trade-off method and ADR template.
- `references/security-compliance.md` — security, privacy, responsible-AI checklist.
