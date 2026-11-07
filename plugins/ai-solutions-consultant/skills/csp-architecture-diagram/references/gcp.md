# Google Cloud — official icons in draw.io

Libraries: **gcp2** (Google Cloud Platform icons, `shape=mxgraph.gcp2.*`) and the current Google Cloud product icons returned by `search_shapes` as embedded SVG images. Prefer the current product icons when search returns them (e.g. "Compute Cloud Run"); fall back to `gcp2`, then `gcp3`.

Example (Cloud Run, gcp3 shape):
```
sketch=0;html=1;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;align=center;fontSize=11;fontStyle=0;fontColor=#000000;aspect=fixed;pointerEvents=1;shape=mxgraph.gcp3.cloudrun;fillColor=#4285f4
```

## Common services → query
Vertex AI (`gcp vertex ai`), Gemini, Vertex AI Search, Speech-to-Text, Text-to-Speech, Dialogflow CX, Contact Center AI, Apigee, API Gateway, Cloud Run, GKE, Cloud Functions, Pub/Sub, Eventarc, Workflows, BigQuery, Cloud SQL, AlloyDB, Spanner, Firestore, Bigtable, Cloud Storage, Memorystore, Cloud Load Balancing, Cloud Armor, Cloud CDN, Cloud DNS, Cloud Interconnect, Cloud VPN, Private Service Connect, Cloud IAM, Secret Manager, Cloud KMS, Cloud Logging, Cloud Monitoring, Security Command Center.

## Grouping (Google reference-architecture convention)
- Google Cloud boundary: rounded rectangle, white fill with gray border `#DADCE0`, label "Google Cloud" with logo top-left.
- Project: fill `#F8F9FA`, border `#DADCE0`.
- Region / zone: dashed gray border.
- VPC: border `#4285F4`, fill `#E8F0FE`.
- Accent: Google blue `#4285F4`; secondary `#34A853`, `#FBBC04`, `#EA4335` only for status.
