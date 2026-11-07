# Discovery question bank

Pick from these; never ask them all. Phrase in the client's language.

## 1. Business outcome
- What business problem or opportunity triggers this work? What happens if nothing is done?
- What is the measurable success metric (cost per contact, containment rate, NPS, time-to-decision, revenue)? Baseline and target?
- Who is the executive sponsor and what decision must this work support (approve budget, choose vendor, approve architecture)?
- What is the timeline driver (regulatory date, contract renewal, board meeting)?

## 2. Scope and users
- Which journeys, products, business units and channels are in scope for phase 1? What is explicitly out?
- Who are the users (customers, agents, employees, partners) and how many?
- Which languages and regions?

## 3. Current state
- What systems are involved today (CRM, core banking/ERP, contact center, data warehouse, document stores)?
- How does the process work today, step by step? Where are the pain points?
- What existing vendors or platforms must be reused or retired?

## 4. Cloud, hosting and platform constraints
- Target cloud provider(s): Azure, AWS, GCP, on-prem, hybrid? Is there a landing zone already?
- Must any component stay on-prem (telephony, core systems, data stores)?
- Vendor SaaS allowed, or must vendors deploy into the client's tenancy / private cloud?
- Network constraints: private connectivity only (Private Link / PrivateLink / Private Service Connect, ExpressRoute / Direct Connect / Interconnect), internet egress rules?
- Mandated platforms (API gateway, identity provider, SIEM, observability stack)?

## 5. Data and regulation
- Data classes involved (PII, financial, health, card data)? Data residency requirements?
- Applicable regulation and standards (e.g. RBI / PCI DSS / GDPR / HIPAA / SOC 2 / ISO 27001 / DPDP Act)?
- Retention, audit and right-to-erasure requirements?

## 6. Integration
- For each system: read, write or both? Real-time or batch? Existing APIs, or does an integration layer need building?
- Integration platform (ESB, API gateway, iPaaS, event bus)?
- Authentication model (OAuth2, mTLS, service accounts, SSO)?

## 7. Non-functional requirements
- Volumes: peak concurrent sessions, transactions per second, daily volume, growth.
- Latency targets (e.g. voice turn latency, API p95).
- Availability (SLA, RTO/RPO), DR region needs.
- Cost envelope or pricing model preference (capex/opex, per-use).

## 8. AI-specific
- Which AI capabilities: conversational bot, RAG over knowledge, summarization, classification, agent assist, autonomous actions?
- Which models are allowed (provider, region, open-weight, fine-tuned)? Must all model calls route via an AI gateway?
- Knowledge sources, owners, update frequency and approval (maker–checker)?
- Human-in-the-loop requirements: which actions need approval?
- Evaluation: how will quality, safety, hallucination and bias be measured? Who signs off?
- Responsible-AI and model-risk governance requirements.

## 9. Delivery and operating model
- Who builds and who runs it (client team, vendor, SI)? Skills available?
- Environments and CI/CD expectations; change-management constraints.
- Support model and SLAs with vendors.

## 10. Deliverables and audience
- Which artifacts are wanted: understanding document, architecture, draw.io diagram, deck?
- Audience for each (C-suite, architecture board, security, vendor)? Template or design system to use?
- Diagram style: CSP official icons, level of detail (context, logical, physical/deployment)?
