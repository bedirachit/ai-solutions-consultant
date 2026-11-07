# Layout conventions and quality checklist

## View types
| View | Audience | Shows |
|---|---|---|
| Context | C-suite, sponsors | Actors, the solution as one box, external systems, key flows |
| Logical | Architects | Layers, components, interfaces (no network detail) |
| Physical / deployment | Infra, security | Regions, VNets/VPCs, subnets, services, private endpoints, on-prem, connectivity |
| Flow (current vs proposed) | Business + architects | Numbered steps across swimlanes or side-by-side panels |
| Security / network | Security, risk | Trust boundaries, ingress/egress, identity, encryption, inspection points |

## Layout
- Flow left → right: users / channels → interaction → AI / orchestration → integration → systems of record. Platform services (identity, monitoring, key vault) in a band at the bottom.
- 40 px grid; icons 48–64 px; label below icon, 12 px; group labels 14 px bold top-left.
- Groups nest strictly (cloud → region → network → subnet); never overlap groups.
- Numbered step badges (circles, 24 px) on edges for flows; matching numbered legend.
- Edge styles: solid = synchronous request, dashed = asynchronous/event, thick = network connectivity, red dashed = trust boundary. Use `edgeStyle=orthogonalEdgeStyle` and `routing: libavoid`.
- Highlight what is new: new components with a colored outline (provider accent) and a "NEW" tag; existing components neutral gray.
- Title block top-left: diagram title, view type, version, date, status ("Draft for review").
- Legend bottom-right.

## Quality checklist (the partner checks these)
- [ ] Official icon set of the stated provider; no mixed generations of icons.
- [ ] Every component labelled with service name and role.
- [ ] Every non-obvious edge labelled (protocol / data).
- [ ] Groups correct and nested; trust boundaries shown.
- [ ] New vs existing clear.
- [ ] Matches the architecture write-up exactly (same names, same components).
- [ ] Readable at slide size: ≤ ~40 shapes, no crossing lines through icons.
- [ ] "Open in draw.io" link and .drawio file delivered.
