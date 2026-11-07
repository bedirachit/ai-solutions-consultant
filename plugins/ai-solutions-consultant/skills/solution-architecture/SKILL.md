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

The reader is the **client's own team**: their enterprise architects, platform
and infrastructure engineers, security, application owners and delivery leads.
They will build, run and approve this. Write so that each of them can answer:
*what are we building, what does each piece do, how does a request flow through
it, what do I own, and why was it designed this way?*

- **Architecture first.** At least 60% of the document describes the
  architecture itself: components, how they interact, flows, deployment,
  integration, security and operations. Context, research and roadmap stay short.
- **Their language, their systems.** Name their systems, environments and teams
  as they do. Explain every acronym once. No consulting filler, no sales tone.
- **Every component explained.** For each component: role, purpose (the
  requirement it serves), responsibilities, inputs and outputs, interfaces,
  technology/service, who owns and operates it, how it scales and fails, and
  why it was chosen over the alternatives.
- **Flow diagrams in the document.** Embed diagrams directly in the document,
  not only as links:
  1. **Architecture overview diagram** — all components grouped by layer, with
     numbered interactions.
  2. **One flow diagram per key journey** (e.g. inbound call, outbound campaign,
     knowledge publish) — numbered steps; the step table under it names the
     component, the action, the data and the protocol for each step, so the
     reader sees each component's role in motion.
  Draft each as a Mermaid diagram in the document (flowchart or sequence
  diagram). When the diagram specialist produces draw.io versions, insert the
  exported image and keep the Open in draw.io link beneath it.

Follow `assets/architecture-document-template.md` section by section. Keep the
component catalogue and journey flows as the core of the document.

When draw.io diagrams are requested, hand `csp-architecture-diagram` the
component catalogue, groupings (regions, VNets/VPCs, on-prem zone), and the
numbered edges from the journey flows.

## Guardrails

- Never name a tool without its trade-off.
- Least privilege by default: read-only where reads suffice, write-only for
  case creation, no direct database access from AI components.
- Every AI model call goes through one governed path (AI gateway / API
  management) when the client has one.
- Design for failure: every automated path has a human or legacy fallback.
- Do not invent product capabilities, prices or SLAs; flag them `[verify with vendor]`.

## Asset

- `assets/architecture-document-template.md` — the Solution Architecture Document template (component catalogue, journey flow diagrams, deployment, integration, security, operations, ADRs).

## References

- `references/building-blocks.md` — system-design building blocks with when-to-use and stress behavior.
- `references/ai-integration-patterns.md` — enterprise AI patterns (RAG, agentic tool use, MCP, event-driven, gateway, contact-center AI).
- `references/csp-service-map.md` — equivalent services across Azure, AWS, GCP and on-prem.
- `references/tradeoff-framework.md` — trade-off method and ADR template.
- `references/security-compliance.md` — security, privacy, responsible-AI checklist.
