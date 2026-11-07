# Enterprise AI integration patterns

## Decision points
1. **Sync vs async** — real-time answer (gateway / request-response) or background processing (event-driven)?
2. **Read vs write** — AI reads context (RAG, lookups) or acts in systems (tool use, case creation)?
3. **Single vs multi-system** — one integration or orchestration across several?
4. **Human-in-the-loop vs autonomous** — which actions need approval?

## Patterns

### 1. AI gateway (governed model access)
All model calls pass through one gateway (API management + AI gateway policies): auth, quotas, token metering, content safety, logging, model routing and fallback.
- Solves: governance, cost control, auditability, model swap.
- Worsens: one more hop; gateway must be highly available.
- Use: always in regulated enterprises; mandatory where a landing zone requires it.

### 2. Retrieval-augmented generation (RAG)
Ingest → chunk (with overlap, keep metadata) → embed → index (vector + keyword hybrid) → retrieve → rerank → ground the prompt → cite sources.
- Governance: source owners, maker–checker approval, versioning, tenancy / line-of-business metadata, pull-only ingestion from the system of record, withdrawal propagates.
- Quality: evaluate retrieval recall and answer faithfulness on a golden set before go-live.

### 3. Agentic tool use (actions in systems)
LLM selects tools exposed as narrow, typed functions (or MCP tools). Each tool maps to one API operation with least privilege.
- Controls: allow-list of tools, parameter validation, idempotency keys, approval gates for high-risk actions, full action log.

### 4. MCP server / connector
Expose an enterprise system to AI agents through a Model Context Protocol server: tool definitions, auth (OAuth2 / service account), rate limits, input validation, audit logging.

### 5. Event-driven AI
Business event → queue/stream → AI worker (classify, summarize, enrich) → action dispatcher with approval gates → DLQ for failures.
- Use: post-call summaries, QA scoring, document processing, alerts.

### 6. Integration via existing middleware
AI never calls systems of record directly; it calls the client's API gateway / ESB / iPaaS, which owns transformation, auth and throttling.

### 7. Contact-center AI (voice and chat)
- **Inbound voice bot:** PSTN → carrier → contact-center platform (routing, IVR) → SBC (SIP/RTP) → conversational AI (ASR → NLU/LLM → TTS) → integration layer → systems of record; fallback to IVR or agent with context transfer.
- **Outbound:** dialer places call → bot conversation → disposition written back → follow-ups (SMS/email via messaging gateway) → CRM record.
- **Agent assist:** real-time transcript stream → knowledge retrieval and next-best-action → agent desktop; post-call summary and disposition.
- **Quality monitoring:** recordings/transcripts → automated scoring against a QA rubric → dashboards and coaching; sample human calibration.
- **Controlled rollout:** split traffic (e.g. by DID or percentage) between the incumbent and the new bot; compare containment, CSAT, AHT; reversible by routing change.

### 8. Human-in-the-loop
Draft → human approves → system writes. Use for regulated communications, financial actions, policy exceptions.

## Always include
- Secrets in a vault; managed identities where possible.
- Structured logs, traces, token and cost metrics per use case.
- Evaluation harness: golden datasets, regression tests on prompt/model change, safety tests (prompt injection, jailbreak, PII leakage).
- Phased rollout: one use case, measure, expand.
