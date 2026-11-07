# Building blocks

For each block: what it answers, main options, behavior under stress, and the signal to use it.

| Block | Answers | Options | Under stress / failure | Use when |
|---|---|---|---|---|
| Requirements scoping | What, for whom, what's out? | FR / NFR / out-of-scope lists | Unclear scope → redesign later | Always first |
| Capacity estimate | How big? | QPS, storage, bandwidth, concurrency | Wrong by 10× → wrong design | Before choosing stores, compute |
| API design | How do parts talk? | REST, gRPC, GraphQL, WebSocket, SIP for voice | Chatty APIs add latency; no idempotency → duplicates on retry | Every interface; add idempotency keys to writes |
| Service decomposition | How many services? | Modular monolith, microservices, BFF, API gateway | Too fine → distributed monolith | Split by team ownership and change rate |
| Load balancing | How is traffic spread? | L4 vs L7, health checks, session affinity | Sticky sessions hurt failover | >1 instance behind one address |
| Data storage | Where do records live? | Relational, document, key-value, wide-column, graph, vector | Hot partitions, replication lag | Pick by access pattern, not fashion |
| Caching | What to keep close? | Cache-aside, read-through, write-through; Redis | Stampede, stale reads, hot keys | Read-heavy, tolerant of staleness |
| Messaging / streaming | What runs async? | Queue (point-to-point), pub/sub, log/stream (Kafka-style) | Backlog growth, poison messages → DLQ | Spiky or slow work, decoupling |
| Workflow / scheduling | Long-running or timed work? | Durable workflow engines, schedulers, sagas | Lost leases, duplicate runs | Multi-step processes, retries, compensation |
| Consistency | What does a reader see? | Strong, eventual, read-your-writes; quorum; sagas | Partitions force CAP choice | Multiple replicas or services own data |
| Resilience | What when it breaks? | Timeouts, retries with backoff + jitter, circuit breaker, bulkhead, rate limit, graceful degradation | Naive retries cause storms | Every remote call |
| Content delivery / edge | Serve static and media close to users | CDN, edge cache, WAF at edge | Origin overload on cache miss | Public web / media |
| DNS / global routing | Which region serves the user? | Geo, latency, weighted, failover routing | TTL delays failover | Multi-region |
| Identity | Who is calling? | OIDC/OAuth2, SAML SSO, managed identities, mTLS | Token expiry, over-broad scopes | Every interface |
| Observability | How do we know it's broken? | Metrics (RED/USE), logs, traces, SLOs, alerting | Alert fatigue; blind spots | Always; define SLOs per journey |
| Search | Find by relevance | Inverted index (BM25), hybrid with vectors | Index lag | Text search over content |
| Vector store | Semantic retrieval | Managed vector DB, search service with vectors, pgvector | Embedding drift, recall loss | RAG, semantic search |
| Blob / object store | Large unstructured files | Object storage with tiers, versioning | Egress cost | Documents, recordings, media |
| Scaling evolution | What breaks next at 10×? | Replicas → cache → shard → multi-region | First bottleneck shifts | Growth planning |

## Typical layers for an enterprise AI solution

1. **Channels** — voice (PSTN/SIP via SBC), chat, web, mobile, messaging, email.
2. **Interaction** — contact center platform, IVR, bot platform, agent desktop.
3. **AI and orchestration** — conversational AI platform, LLM orchestration, agents, prompt and guardrail layer, evaluation.
4. **AI access** — AI gateway / API management in front of all model endpoints; content safety.
5. **Knowledge** — document sources, ingestion, chunking, embeddings, vector + keyword index, approval workflow.
6. **Integration** — API gateway / ESB / iPaaS, event bus; adapters to systems of record.
7. **Systems of record** — CRM, core systems, card platforms, ERP, data warehouse.
8. **Platform** — identity, secrets, network (hub-spoke, private endpoints), SIEM, observability, CI/CD, IaC.
