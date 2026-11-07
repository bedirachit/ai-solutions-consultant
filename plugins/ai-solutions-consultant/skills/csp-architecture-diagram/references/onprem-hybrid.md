# On-prem, hybrid and third-party shapes

Use `search_shapes` with these queries and prefer consistent, flat icon families in one diagram.

| Element | Query | Notes |
|---|---|---|
| Server / VM | `server`, `mxgraph.cisco servers` | Cisco or network2 libraries |
| Database (on-prem) | `database`, `cylinder` | plain cylinder with product name label is fine |
| Firewall | `firewall` (network2 / cisco) | |
| Router / switch | `cisco router`, `switch` | |
| Load balancer | `load balancer` | |
| Data center / zone | rounded rectangle group, gray `#5F6368` border, label "On-premises data center" | |
| DMZ | dashed red border `#C62828` group inside the data center | |
| SBC (session border controller) | `cisco unified border element` or `server` labelled "SBC (SIP/RTP)" | |
| Contact center / PBX | `call center`, `cisco ip phone`, `pbx` | label with product (e.g. "Genesys Engage") |
| PSTN / carrier | `cloud` shape labelled "PSTN / carrier" | |
| Users / customers | `user`, `mobile phone`, `telephone` | |
| Agent desktop | `workstation`, `laptop` | |
| SaaS vendor platform | rounded rectangle with vendor name; vendor logo via icon search only if appropriate | Keep vendor zone visually separate from client tenancy |
| Mainframe | `mainframe` | |
| SharePoint / M365 | `sharepoint` | Microsoft icon from icon service |
| SMS gateway | `sms`, `message` | label with provider |

## Hybrid conventions
- Place on-prem on the left, cloud on the right, connectivity (ExpressRoute / Direct Connect / Interconnect / VPN) as a thick labelled edge between them.
- Put SaaS vendors in their own zone above or right of the client cloud, with the trust boundary drawn.
- Mark trust boundaries with dashed red lines and a label ("Trust boundary — bank network").
- Show which side owns each data store.
