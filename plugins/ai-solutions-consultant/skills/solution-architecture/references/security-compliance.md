# Security, privacy and responsible-AI checklist

## Identity and access
- [ ] SSO for users; managed identities / workload identities for services; no shared accounts.
- [ ] Least privilege per integration (read-only vs write-only scopes); periodic access review.
- [ ] Privileged access via PIM / just-in-time; break-glass procedure.

## Network
- [ ] Private connectivity to managed services (private endpoints / PrivateLink / PSC); no public endpoints for data services.
- [ ] Hub-spoke with central firewall and egress control; WAF on any public ingress.
- [ ] On-prem connectivity via dedicated circuits or VPN with redundancy.
- [ ] Voice: SIP/TLS and SRTP where supported; SBC in DMZ; topology hiding.

## Data
- [ ] Data classification and residency mapped per data store and per model endpoint.
- [ ] Encryption in transit (TLS 1.2+) and at rest (customer-managed keys where required).
- [ ] PII minimization and masking in prompts, logs, transcripts and recordings.
- [ ] Retention and deletion schedules; legal hold.
- [ ] Card data (PCI DSS): pause/resume recording, DTMF masking, keep PAN out of AI context.

## Application and API
- [ ] All APIs behind the API gateway with authN/authZ, throttling, schema validation.
- [ ] Idempotency on writes; replay protection.
- [ ] Secrets in a vault; rotation; no secrets in code or prompts.

## AI-specific
- [ ] All model calls via the governed AI gateway; approved models and regions only.
- [ ] Content safety and prompt-injection defenses on inputs and retrieved content.
- [ ] Grounding with citations; refusal when knowledge is missing; no free-form answers on regulated topics without approved content.
- [ ] Tool allow-list; high-risk actions require human approval.
- [ ] Evaluation before go-live and on every change: accuracy, faithfulness, safety, bias, latency, cost.
- [ ] Model risk management: inventory, owner, intended use, limitations, monitoring, periodic review.
- [ ] Customer disclosure that they are speaking with an automated assistant, where required.

## Operations
- [ ] Centralized logging to SIEM; AI action audit trail.
- [ ] SLOs and alerts per journey; runbooks; on-call.
- [ ] DR: RTO/RPO defined and tested; fallback to human/legacy path.
- [ ] Vendor risk: SOC 2 / ISO 27001 evidence, data processing terms, sub-processors, exit plan.

## Regulatory prompts (confirm applicability with the client's compliance team)
Banking regulator outsourcing and IT guidelines, data protection law (e.g. GDPR, India DPDP Act), PCI DSS, SOC 2, ISO 27001/27701, sector AI guidance.
