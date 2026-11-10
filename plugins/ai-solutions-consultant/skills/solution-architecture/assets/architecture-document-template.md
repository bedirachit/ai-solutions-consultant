<!--
TEMPLATE NOTES (instructions for the author; never copy these notes or any
bracketed guidance into the delivered document).

- This is the CLIENT-READY Solution Architecture Document. It describes the
  proposed solution only. Do not include options that were rejected, option
  comparisons or scoring. Record only the decisions taken, in Appendix D.
- Length: 15-20 pages including figures and tables (about 4,500-6,500 words of
  body text). Use the page budget below.
- Headings: use the headings below exactly, or a client-specific noun phrase.
  Never a heading that describes the writing task ("in one paragraph",
  "at a glance", "in plain words", "simple flow").
- Every section opens with a 2-3 sentence key message (the conclusion first),
  then the supporting detail.
- Number every figure and table, give each a caption and, where relevant, a
  source line.

PAGE BUDGET
| Section | Pages |
|---|---|
| Cover, document control, contents | 2 |
| 1 Executive summary | 1 |
| 2 Context and objectives | 1 |
| 3 Solution overview | 2 |
| 4 Solution architecture | 4 |
| 5 Key journeys | 3 |
| 6 Integration | 1 |
| 7 Deployment and infrastructure | 1.5 |
| 8 Security, compliance and AI governance | 1.5 |
| 9 Non-functional requirements | 1 |
| 10 Operations and support | 0.5 |
| 11 Implementation roadmap | 1 |
| 12 Risks, assumptions and dependencies | 1 |
| Appendices | 1-2 |
-->

# [Client name]
# [Solution name]
## Solution Architecture Document

[Version] · [Date] · [Classification, e.g. Confidential — for [Client] internal use]

---

### Document control

| Version | Date | Author | Reviewer | Changes |
|---|---|---|---|---|
| 1.0 | | | | Issued for client review |

| Approver | Role | Signature / date |
|---|---|---|
| | | |

### Contents

[Generate a real table of contents: a TOC field in Word, the document tool's
index or outline in a living doc, a linked list of sections in Markdown.]

---

## 1. Executive summary

[Key message: what [Client] will build, the outcome it delivers, and the one or
two design choices that matter most. Then 4-6 short paragraphs or bullets:
business need, proposed solution, what changes and what stays, key benefits,
key risks and how they are managed, decisions or approvals required.]

## 2. Context and objectives

### 2.1 Background
### 2.2 Objectives and success measures
| Objective | Measure | Target |
|---|---|---|
### 2.3 Scope
| In scope | Out of scope |
|---|---|

## 3. Solution overview

[Key message.]

**Figure 1 — Solution overview**
[Simple flow diagram: 5-8 boxes, left to right, the client's names for systems,
numbered arrows, new components highlighted, legend. Rendered as a picture.]

### 3.1 How the solution works
[Numbered steps matching the numbers in Figure 1, one sentence each.]

### 3.2 What changes for [Client]
**Table 1 — New, changed and unchanged components**
| Component | Status | Role |
|---|---|---|

## 4. Solution architecture

### 4.1 Architecture principles
**Table 2 — Architecture principles**
| Principle | What it means for this solution |
|---|---|

### 4.2 Logical architecture
**Figure 2 — Logical architecture**
[Layers and components; rendered picture; draw.io with official cloud icons
where a cloud provider applies; "Open in draw.io" link under the image.]

[One paragraph per layer.]

### 4.3 Component descriptions
[One sub-section per component, 4.3.1, 4.3.2 … each with a short paragraph and
this table.]

| Attribute | Description |
|---|---|
| Purpose | |
| Responsibilities | |
| Interfaces | |
| Technology | |
| Hosting and ownership | |
| Scaling and resilience | |
| Security | |

## 5. Key journeys

[Key message. One sub-section per journey, 5.1, 5.2 …]

### 5.1 [Journey name, e.g. Inbound credit card enquiry]
**Figure 3 — [Journey name] flow**
[Sequence or flow diagram, rendered picture.]

**Table 3 — [Journey name] steps**
| Step | Component | Action | Data | Protocol / authentication |
|---|---|---|---|---|

**Exception handling.** [What happens when a step fails and the fallback.]

## 6. Integration

**Table 4 — Integration catalogue**
| ID | Source | Target | Purpose | Pattern / protocol | Authentication | Data | Volume / latency | Owner |
|---|---|---|---|---|---|---|---|---|

## 7. Deployment and infrastructure

**Figure 4 — Deployment view**
[Environments, regions, network zones, private connectivity, on-premises vs
cloud vs vendor-hosted; official cloud icons.]

### 7.1 Environments
### 7.2 Network and connectivity
### 7.3 Hosting and capacity

## 8. Security, compliance and AI governance

### 8.1 Identity and access
### 8.2 Network security
### 8.3 Data protection
### 8.4 Regulatory compliance
**Table 5 — Compliance mapping**
| Requirement | Control | Where implemented |
|---|---|---|
### 8.5 AI governance
[Model access path, knowledge governance, guardrails, evaluation, human
oversight. Omit 8.5 if the solution has no AI component.]

## 9. Non-functional requirements

**Table 6 — Non-functional requirements**
| Category | Requirement | Target | How the design meets it |
|---|---|---|---|

## 10. Operations and support

[Monitoring and alerting, support model and responsibilities, runbooks,
release and change management.]

## 11. Implementation roadmap

**Figure 5 — Implementation roadmap**
| Phase | Scope | Dependencies | Exit criteria | Indicative timing |
|---|---|---|---|---|

## 12. Risks, assumptions and dependencies

**Table 7 — Risks**
| ID | Risk | Impact | Mitigation | Owner |
|---|---|---|---|---|
**Table 8 — Assumptions and dependencies**
| ID | Assumption or dependency | Owner | Status |
|---|---|---|---|

## Appendices

### Appendix A — Glossary
### Appendix B — Requirements traceability
| Requirement ID | Requirement | Section |
|---|---|---|
### Appendix C — References
### Appendix D — Design decisions
| ID | Decision | Rationale |
|---|---|---|
[Decisions taken only. No rejected options or comparisons.]
