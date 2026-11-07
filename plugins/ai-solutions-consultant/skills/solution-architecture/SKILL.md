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
8. **Iterate** on the weakest part, then write it up.

## Write-up structure

1. Context and drivers (link to Understanding Document).
2. Architecture principles (5–7, specific to this client).
3. Logical architecture: layers and components, one line on each component's
   job.
4. Key flows: numbered steps for the 2–4 most important journeys
   (e.g. inbound call, outbound campaign, knowledge update).
5. Physical / deployment view (CSP-specific): regions, networks, subnets,
   private connectivity, managed services, on-prem components.
6. Integration view: system, direction, protocol, auth, data, owner.
7. Security, privacy and compliance controls mapped to NFRs.
8. Non-functional design: scalability, availability, DR, performance, observability.
9. AI design: models and access path, grounding / knowledge, guardrails,
   evaluation, human-in-the-loop, model risk governance.
10. Architecture decisions (ADRs) and alternatives rejected.
11. Risks, assumptions, open questions.
12. Roadmap: phases with exit criteria.

When a diagram is requested, hand the logical and physical views to
`csp-architecture-diagram` with a component list, groupings (regions, VNets/VPCs,
on-prem zone), and the edges with labels.

## Guardrails

- Never name a tool without its trade-off.
- Least privilege by default: read-only where reads suffice, write-only for
  case creation, no direct database access from AI components.
- Every AI model call goes through one governed path (AI gateway / API
  management) when the client has one.
- Design for failure: every automated path has a human or legacy fallback.
- Do not invent product capabilities, prices or SLAs; flag them `[verify with vendor]`.

## References

- `references/building-blocks.md` — system-design building blocks with when-to-use and stress behavior.
- `references/ai-integration-patterns.md` — enterprise AI patterns (RAG, agentic tool use, MCP, event-driven, gateway, contact-center AI).
- `references/csp-service-map.md` — equivalent services across Azure, AWS, GCP and on-prem.
- `references/tradeoff-framework.md` — trade-off method and ADR template.
- `references/security-compliance.md` — security, privacy, responsible-AI checklist.
