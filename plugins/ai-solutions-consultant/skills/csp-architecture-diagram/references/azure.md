# Azure — official icons in draw.io

Library: **azure2** (Microsoft Azure architecture icons). Image path pattern:
`https://app.diagrams.net/img/lib/azure2/<category>/<Icon_Name>.svg`

Base style (example, Azure OpenAI):
```
image;aspect=fixed;html=1;align=center;fontSize=12;image=https://app.diagrams.net/img/lib/azure2/ai_machine_learning/Azure_OpenAI.svg;
```
Always confirm the exact path with `search_shapes` ("azure <service>").

## Common services → search query
| Service | Query | Typical category folder |
|---|---|---|
| Azure OpenAI / AI Foundry | `azure openai`, `azure ai studio` | ai_machine_learning |
| Azure AI Search | `azure cognitive search` / `azure search` | ai_machine_learning / web |
| Azure AI Speech | `azure speech services` | ai_machine_learning |
| Content Safety | `azure content safety` | ai_machine_learning |
| API Management | `azure api management` | integration / app_services |
| App Service / Functions | `azure app services`, `azure function apps` | app_services / compute |
| AKS / Container Apps | `azure kubernetes services`, `azure container apps` | containers |
| Service Bus / Event Grid / Event Hubs | `azure service bus`, `azure event grid`, `azure event hubs` | integration / analytics |
| Logic Apps | `azure logic apps` | integration |
| Cosmos DB / SQL / PostgreSQL | `azure cosmos db`, `azure sql`, `azure database postgresql` | databases |
| Storage / Blob | `azure storage accounts`, `azure blob` | storage |
| Key Vault | `azure key vaults` | security |
| Entra ID | `azure entra id` / `azure active directory` | identity |
| Virtual Network / Firewall / Private Link | `azure virtual networks`, `azure firewall`, `azure private link` | networking |
| ExpressRoute / VPN Gateway | `azure expressroute circuits`, `azure virtual network gateways` | networking |
| Front Door / Application Gateway | `azure front doors`, `azure application gateways` | networking |
| Monitor / App Insights / Log Analytics | `azure monitor`, `azure application insights`, `azure log analytics` | monitor / devops |
| Sentinel | `azure sentinel` | security |
| SharePoint / Microsoft 365 | `sharepoint`, `office 365` | other / icon service |

## Grouping (Microsoft reference-architecture convention)
- Subscription / landing zone: rounded rectangle, light gray fill `#F2F2F2`, label top-left.
- Region: dashed border `#0078D4`, no fill.
- Virtual network: border `#0078D4` solid 1.5 px, fill `#E8F2FB`, VNet icon at top-left.
- Subnet: dashed border `#7FBA00` or `#0078D4`, fill white.
- Hub-spoke: hub VNet (firewall, gateway, bastion) center-left, spokes right.
- Private endpoint: small private-link icon on the edge of the service, inside the subnet.
- Accent color for Azure edges and highlights: `#0078D4`.
