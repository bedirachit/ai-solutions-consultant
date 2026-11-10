# Example requests to the AI Solutions Lead

Send every request to **`/ai-solutions-lead`**. Copy one of these and replace the bracketed parts.

---

## 1. Full engagement: bank voice bot on Azure

```
/ai-solutions-lead
A retail bank wants an AI voice bot to handle credit card servicing calls
(balance, due date, card block, statement request). The bank runs an on-prem
contact center and has an Azure AI landing zone where all models must go
through an AI gateway. I need:
1. an understanding document,
2. the Azure target architecture with an Azure diagram using official icons,
3. a 10-slide deck for the CIO and COO asking for approval to build.
```

**What happens**

| Step | Who | You see |
|---|---|---|
| 0 | AI Solutions Lead | "Running as an agent team…" and the stages it will run |
| 1 | AI Solutions Lead | 4 multiple-choice questions (call volume, vendor hosting, systems of record, compliance) |
| 2 | discovery-analyst → md-senior-partner | Research Brief: how banks built card-servicing voice bots, Azure reference architectures, pitfalls, regulator guidance (runs while you answer step 1) |
| 2b | AI Solutions Lead → md-senior-partner | Understanding Document + review note (e.g. approved in round 1) |
| 3 | solution-architect → md-senior-partner | Architecture write-up with ADRs + review note (e.g. round 2 after fixing a missing fallback path) |
| 4 | diagram-specialist → md-senior-partner | Azure diagram in draw.io, **Open in draw.io** link, `.drawio` file + review note |
| 5 | deck-strategist → md-senior-partner | CIO/COO deck + review note |
| 6 | AI Solutions Lead | Partner cover note: three takeaways, open questions, decisions required, placeholders to fill |

---

## 2. Understanding document from workshop notes

```
/ai-solutions-lead
Attached are my notes from two discovery workshops with an insurer about
automating claims intake with AI. Turn them into an understanding document
for the client's CTO to confirm. Word format please.
```
Runs: research + clarify (only real gaps) → AI Solutions Lead writes it → partner gate. Output: `.docx` Understanding Document with numbered FR/NFR, assumptions and open questions.

---

## 3. AWS architecture for a RAG assistant

```
/ai-solutions-lead
Design an AWS architecture for an internal assistant that answers employee
questions from HR and IT policy documents in SharePoint. 8,000 employees,
SSO with Entra ID, data must stay in ap-south-1. Include the AWS diagram.
```
Runs: research + clarify → understanding document → solution-architect → diagram-specialist (aws4 icons) → partner gate on each.

---

## 4. Current vs proposed flow diagram only

```
/ai-solutions-lead
Draw a current vs proposed inbound call flow in draw.io.
Current: IVR verification → legacy voice bot → agent.
Proposed: calls split between legacy bot and new AI bot; AI bot reads the
card system (read-only), writes a case to CRM (write-only) through the API
layer; unresolved calls fall back to IVR or an agent.
```
Runs: light clarify → diagram-specialist → partner gate. Output: two-panel flow diagram, Open in draw.io link, `.drawio` file.

---

## 5. GCP vs SaaS hosting decision

```
/ai-solutions-lead
Our conversational AI vendor offers SaaS or deployment into our GCP project.
Compare the two for a regulated bank and recommend one in an Options Paper,
with an ADR.
```
Runs: research (published comparisons, regulator guidance) + clarify → solution-architect (separate Options Paper + ADR; the architecture document later describes only the chosen option) → partner gate.

---

## 6. Partner review of your own deck

```
/ai-solutions-lead
Review the attached architecture deck like a senior partner before it goes
to the COO on Monday. Be tough.
```
Runs: md-senior-partner only. Output: scorecard, must-fix / should-fix / polish list with exact fixes, verdict.

---

## 7. Hybrid network and security view

```
/ai-solutions-lead
Create the network and security view for the approved architecture: on-prem
data center with DMZ and session border controller, ExpressRoute to Azure
hub-spoke, private endpoints for AI services, trust boundaries marked.
```
Runs: diagram-specialist (Azure + on-prem shapes) → partner gate.

---

## 8. Research only

```
/ai-solutions-lead
How have banks and insurers implemented AI agent assist in their contact
centers? I want implementation patterns, best practices, pitfalls and
published results.
```
Runs: discovery-analyst → partner gate. Output: cited Research Brief with source grades and the top implications first.
