# Cloud service map

Equivalent services by capability. Verify current names and regional availability before finalizing; mark anything uncertain `[verify]`.

| Capability | Azure | AWS | GCP | On-prem / generic |
|---|---|---|---|---|
| Landing zone / org structure | Management groups, subscriptions, Azure Landing Zone | AWS Organizations, Control Tower | Resource hierarchy, folders, projects | Data center zones |
| Virtual network | Virtual Network (VNet), hub-spoke, Virtual WAN | VPC, Transit Gateway | VPC, Shared VPC, NCC | VLANs, DMZ |
| Private service access | Private Endpoint / Private Link | PrivateLink, VPC endpoints | Private Service Connect | — |
| Dedicated connectivity | ExpressRoute, VPN Gateway | Direct Connect, Site-to-Site VPN | Cloud Interconnect, Cloud VPN | MPLS, leased lines |
| Edge / WAF | Front Door, Application Gateway + WAF | CloudFront, ALB, AWS WAF | Cloud CDN, Cloud Load Balancing, Cloud Armor | F5 / NGINX, WAF appliance |
| Firewall | Azure Firewall | Network Firewall | Cloud NGFW | NGFW appliances |
| API management | API Management | API Gateway | Apigee, API Gateway | Kong, MuleSoft, IBM API Connect |
| AI gateway | API Management AI gateway policies | API Gateway + Bedrock guardrails `[verify]` | Apigee AI policies `[verify]` | LiteLLM, Kong AI Gateway |
| Foundation models | Azure OpenAI / Azure AI Foundry | Amazon Bedrock | Vertex AI (Gemini, Model Garden) | Self-hosted open-weight models (vLLM, Triton) |
| ML platform | Azure Machine Learning | SageMaker | Vertex AI | Kubeflow, MLflow |
| Content safety | Azure AI Content Safety | Bedrock Guardrails | Vertex AI safety filters, Model Armor | Guardrail libraries |
| Speech (ASR/TTS) | Azure AI Speech | Transcribe, Polly | Speech-to-Text, Text-to-Speech | Vendor ASR/TTS |
| Contact center | Azure Communication Services, Dynamics 365 Contact Center | Amazon Connect | Contact Center AI Platform | Genesys, Avaya, Cisco |
| Search / vector | Azure AI Search | OpenSearch Service, Kendra, Bedrock Knowledge Bases | Vertex AI Search, Vector Search | Elasticsearch, OpenSearch, pgvector |
| Relational DB | Azure SQL, PostgreSQL Flexible Server | RDS, Aurora | Cloud SQL, AlloyDB, Spanner | Oracle, SQL Server, PostgreSQL |
| NoSQL | Cosmos DB | DynamoDB | Firestore, Bigtable | MongoDB, Cassandra |
| Cache | Azure Cache for Redis / Managed Redis | ElastiCache | Memorystore | Redis |
| Object storage | Blob Storage, ADLS Gen2 | S3 | Cloud Storage | MinIO, NAS |
| Messaging | Service Bus, Event Grid | SQS, SNS, EventBridge | Pub/Sub, Eventarc | IBM MQ, RabbitMQ |
| Streaming | Event Hubs | Kinesis, MSK | Pub/Sub, Managed Kafka | Kafka |
| Workflow | Logic Apps, Durable Functions | Step Functions | Workflows | Temporal, Camunda |
| Containers | AKS, Container Apps | EKS, ECS, Fargate | GKE, Cloud Run | OpenShift, Kubernetes |
| Serverless | Azure Functions | Lambda | Cloud Run functions | — |
| Identity | Microsoft Entra ID, managed identities | IAM, IAM Identity Center, Cognito | Cloud IAM, Identity Platform | AD, Keycloak, Ping |
| Secrets / keys | Key Vault, Managed HSM | Secrets Manager, KMS, CloudHSM | Secret Manager, Cloud KMS, Cloud HSM | HashiCorp Vault, HSM |
| Monitoring | Azure Monitor, Application Insights, Log Analytics | CloudWatch, X-Ray | Cloud Monitoring, Cloud Logging, Cloud Trace | Prometheus, Grafana, ELK |
| SIEM | Microsoft Sentinel | Security Hub, GuardDuty | Security Command Center, Chronicle | Splunk, QRadar |
| Data / analytics | Fabric, Synapse, Databricks | Redshift, Glue, Athena | BigQuery, Dataflow | Teradata, Hadoop |
| DevOps / IaC | Azure DevOps, GitHub Actions, Bicep, Terraform | CodePipeline, CloudFormation, CDK, Terraform | Cloud Build, Deployment Manager, Terraform | Jenkins, GitLab |
| Knowledge sources | SharePoint, OneDrive (Microsoft 365) | S3, WorkDocs `[verify]` | Google Drive | Confluence, file shares |
