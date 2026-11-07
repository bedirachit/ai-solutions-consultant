# AI Solutions Consultant

A consulting team in a plugin for Claude Cowork. Give it a business or technology problem and it runs a full engagement: it asks the clarifying questions that matter, writes a detailed Understanding Document, designs a CSP-specific target architecture, draws it in draw.io with the cloud provider's official icons, and builds an executive deck. An **MD / Senior Partner** coordinator reviews and approves every artifact before you see the final version.

## The team

| Agent | Role |
|---|---|
| `md-senior-partner` | Coordinator and final reviewer. Frames the work, dispatches specialists, scores every artifact, sends it back for fixes (max 2 rounds) and approves. |
| `discovery-analyst` | Clarifying questions and the Understanding Document. |
| `solution-architect` | Logical and CSP-specific architecture, AI-integration patterns, NFRs, security, ADRs. |
| `diagram-specialist` | draw.io diagrams with official Azure / AWS / GCP / on-prem icons, plus an "Open in draw.io" link. |
| `deck-strategist` | Top-tier consulting-style executive decks (Slides artifact or PowerPoint). |

## Skills

| Skill | What it does | Try saying |
|---|---|---|
| `solution-engagement` | Runs the whole engagement end to end with review gates | "Act as my solutions consultant for an AI voice bot on Azure" |
| `discovery-questions` | Asks the few questions that change the design | "What do you need to know before designing this?" |
| `understanding-document` | Detailed understanding document (scope, as-is, to-be, FR/NFR, risks, open questions) | "Prepare an understanding document from these notes" |
| `solution-architecture` | System-design and enterprise AI-integration architecture, CSP service mapping, trade-offs, security | "Design the AWS target architecture" |
| `csp-architecture-diagram` | draw.io diagrams with official CSP icons, .drawio file and clickable draw.io link | "Draw the GCP deployment diagram with official icons" |
| `executive-deck` | Answer-first deck with action titles and a clear ask | "Create a C-suite deck on this architecture" |
| `partner-review` | Partner scorecard review and approval note | "Review this deck like a senior partner" |

## Connectors

| Connector | Why | Required |
|---|---|---|
| **draw.io** | Renders diagrams inline and searches the ~10,000-shape library for official cloud icons | Recommended. Without it the plugin still writes draw.io XML, the .drawio file and the open link. |
| Docs / wiki (Notion, Confluence, Google Drive, SharePoint) | Pulls client context and saves documents | Optional |
| GitHub | Stores artifacts or diagrams-as-code in a repo | Optional |

The plugin's connector config points draw.io at `https://mcp.draw.io/mcp`. If your organization uses a different draw.io connector, connect it in **Settings → Connectors**; the skills use whichever draw.io connector is connected.

## Setup in Cowork

1. **Install** — either open the `.plugin` file in the Claude desktop app and accept it, or add the GitHub repository `bedirachit/ai-solutions-consultant` as a plugin marketplace and install **ai-solutions-consultant** from it. In Claude Code:

   ```
   /plugin install ai-solutions-consultant --marketplace bedirachit/ai-solutions-consultant
   ```
2. **Connect draw.io** in Settings → Connectors (recommended).
3. Start a task and say: *"Act as my AI solutions consultant: [your problem]."*

## How the review gate works

Each artifact is scored 1–5 on its scorecard (e.g. for decks: storyline, action titles, evidence, audience fit, visual quality, the ask, consistency). It is approved only when every score is ≥ 4 and no must-fix items remain; otherwise it goes back to its author with numbered, exact fixes. You receive the approved artifact with a short partner review note: verdict, scores, what changed, residual risks.

## Principles

- Clarify before designing; quantify before choosing; justify every component.
- Never invent facts, figures, prices or vendor capabilities — placeholders and open questions instead.
- Least privilege, governed AI access, human or legacy fallback, compliance by design.
- Official CSP icons in every cloud diagram, always with a clickable draw.io link.

## Credits

The system-design and AI-integration knowledge is condensed and rewritten from ideas in the MIT-licensed [system-design-skills](https://github.com/proyecto26/system-design-skills) and [ai-integration-architect](https://github.com/pfbarros2/ai-integration-architect) plugins.

## Privacy

See [PRIVACY.md](PRIVACY.md). The plugin collects no data; connectors follow their own policies.

## License

MIT
