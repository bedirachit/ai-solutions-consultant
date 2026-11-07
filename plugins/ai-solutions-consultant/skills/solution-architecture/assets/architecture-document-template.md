# [Client] — [Solution]: Solution Architecture Document

| Version | Date | Authors | Partner review | Status |
|---|---|---|---|---|
| 0.1 | [date] | [names] | [verdict] | Draft for [Client] architecture review |

**Who should read what**

| If you are… | Read |
|---|---|
| A sponsor or manager | 1, 2, 5 |
| An enterprise or solution architect | Everything |
| A platform / infrastructure engineer | 2, 7, 8, 9, 10 |
| Security, risk or compliance | 2, 4, 11, 13 |
| An application or integration owner | 2, 7, 8, 10 |

> Writing rule for this document: **every name, option, acronym and system is explained the first time it appears, in that same sentence.** Nothing refers to a section the reader has not reached yet.

---

## 1. The problem and what this solution must achieve
*(Plain words, half a page. A reader who stops here knows why this exists.)*

- **Today:** how the process works now and what is wrong with it, in 3–5 sentences.
- **Goals:** what must be true when this is live (measurable where possible, `[TBC]` where not).
- **Non-goals:** what this solution deliberately does not do in this release.

## 2. The solution at a glance
*(The most important page. A new team member can explain the solution after reading only this section.)*

**2.1 How it works — simple flow**

One sentence telling the reader what the picture shows, then the picture.

[Simple flow diagram — mandatory, rendered as a picture, not as code:
 left to right, 5–8 boxes, plain names ("Customer", "Contact center", "AI voice bot", "Integration layer", "Card system", "CRM"), one numbered arrow per step, new components highlighted, a one-line legend.]

**2.2 The same flow in words** — one numbered line per arrow:
1. The customer calls the service number; the **contact center platform** (the bank's existing telephony system that answers and routes calls) receives the call.
2. …

**2.3 What is new and what stays the same**

| Component | New / changed / unchanged | In one line: what it does |
|---|---|---|

**2.4 The recommended approach in one paragraph** — describe the chosen approach by what it *is* (e.g. "the AI platform runs inside the bank's own Azure subscription, reached only through private network links"), never by a label alone. If options were compared, say which ones in a few words each, and why this one won; details are in Section 5.

## 3. Context and scope (who and what the solution interacts with)
System context diagram (C4 level 1): the solution as one box in the middle; people and external systems around it; each arrow labelled with what passes between them.

| Actor / system | Who or what it is | What it exchanges with the solution |
|---|---|---|

## 4. Constraints we must work within
Facts that are already decided and shape the design (landing zone rules, systems that must stay on-prem, regulation, mandated platforms, budget, dates). One line each, with where it comes from.

## 5. Options considered and the recommendation
*(Only when there was a real choice. Give every option a descriptive name; letters are secondary.)*

For each option:

**Option A — [descriptive name, e.g. "Vendor-hosted SaaS"]**
- **What it is:** 2–3 sentences in plain words, including where it runs and who operates it.
- **Small diagram** of how it differs (optional but recommended).
- **Strengths / weaknesses** for this client.
- **Cost, effort and risk** (indicative; `[TBC]` if unknown).

**Comparison**

| Criterion | Vendor-hosted SaaS (A) | In bank's Azure tenancy (B) | … |
|---|---|---|---|

**Recommendation:** the option by name *and* description, and the 2–3 reasons that decided it.

## 6. Solution strategy — the key design decisions in plain words
5–8 bullets: each decision, what it means in practice, and why. (e.g. "All AI model calls go through the bank's AI gateway — the single controlled entry point to Azure AI services — so usage is logged, metered and filtered.")

## 7. Building blocks
**7.1 Container view** (C4 level 2): the deployable parts of the solution and the existing systems they connect to, grouped by layer, numbered arrows. Rendered as a picture; draw.io with official cloud icons when a CSP applies.

**7.2 Component catalogue** — one block per component:

| | |
|---|---|
| **What it is** | Plain-language description; product/service name explained |
| **Why it is here** | The goal or requirement it serves |
| **What it does / does not do** | 3–6 bullets |
| **Talks to** | Systems, direction, protocol, authentication |
| **Runs on / owned by** | Hosting, environment, team that operates it |
| **When it is busy or fails** | Scaling behaviour, failure impact, fallback |
| **Security** | Identity, network placement, data held |

## 8. How it works at runtime — key journeys
For each of the 2–4 most important journeys:

- One sentence on the journey and when it happens.
- **Flow diagram** (sequence diagram), numbered steps, rendered as a picture.
- **Step table:**

| Step | Who / which component | What happens | Data | How (protocol, auth) |
|---|---|---|---|---|

- **When things go wrong:** what the customer and agent experience if a step fails, and the fallback.

## 9. Deployment
Where everything runs: environments, regions, networks and subnets, private connections, on-prem vs cloud vs vendor. Deployment diagram with official cloud icons. Explain each network zone in one line.

## 10. Integration
| # | From → to | Why | How (pattern, protocol) | Authentication | Data | Volume / latency | Owner |
|---|---|---|---|---|---|---|---|

## 11. Cross-cutting concerns
- **Security and privacy** — identity, network, encryption, secrets, data minimisation, audit.
- **Compliance** — regulation → control → where in this design.
- **Operations** — monitoring, alerting, support model, runbooks.
- **AI governance** (if applicable) — model access path, grounding and knowledge sources, guardrails, evaluation, human oversight.

## 12. Quality requirements as scenarios
| Quality | Scenario ("When…, the system…, within…") | How the design achieves it |
|---|---|---|
| Availability | When the AI platform is unavailable, calls route to the IVR within 5 s | Health-checked routing in the contact center |

## 13. Decisions log
| Decision | Options considered (named and described) | Chosen | Why | Consequences |
|---|---|---|---|---|

## 14. Risks, assumptions and open questions
Tables with ids, owner, date and what happens if unresolved.

## 15. Roadmap
Phases with scope, dependencies and exit criteria.

## 16. Glossary
Every acronym and product name used, in one line each.
