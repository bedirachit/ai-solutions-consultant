# Trade-off framework

## The triple — for every significant choice
- **Solves:** which requirement (FR/NFR id) or risk it addresses.
- **Worsens:** cost, latency, complexity, lock-in, operational load, risk introduced.
- **When to change:** the measurable signal that would make another option better (volume > X, latency > Y, regulation change, vendor exit).

## Common axes
| Axis | Lean left when | Lean right when |
|---|---|---|
| Latency ↔ throughput | Interactive journeys (voice turns, chat) | Batch, analytics |
| Consistency ↔ availability | Money, entitlements, case records | Feeds, counters, recommendations |
| Managed ↔ self-hosted | Small team, speed, compliance-certified services exist | Strict residency, cost at scale, special control needs |
| SaaS vendor ↔ client-tenancy deployment | Speed, vendor operates | Data residency, network isolation, regulator expectation |
| Build ↔ buy | Differentiating capability | Commodity capability |
| Single cloud ↔ multi-cloud | Simplicity, skills | Regulatory concentration risk, specific best-of-breed |
| Synchronous ↔ event-driven | User waits for the answer | Spiky, slow or fan-out work |
| Autonomous ↔ human-in-the-loop | Low-risk, reversible actions | Financial, regulated or irreversible actions |

## Option comparison table
| Criterion (weight) | Option A | Option B | Option C |
|---|---|---|---|
| Meets FR/NFR (30%) | | | |
| Security & compliance (20%) | | | |
| Time to value (15%) | | | |
| Total cost of ownership (15%) | | | |
| Operability / skills (10%) | | | |
| Strategic fit / lock-in (10%) | | | |
| **Weighted score** | | | |

## ADR template
```
ADR-n: [Decision title]
Status: Proposed | Accepted | Superseded
Context: [forces, constraints, linked FR/NFR]
Options considered: [A, B, C with one line each]
Decision: [chosen option]
Rationale: [solves / worsens / when to change]
Consequences: [what this commits us to; follow-up actions]
```
