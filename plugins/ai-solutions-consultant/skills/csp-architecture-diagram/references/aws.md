# AWS — official icons in draw.io

Library: **aws4** (current AWS Architecture Icons). Do not use `aws3` or `aws3d`.

Service icon style (example, Lambda):
```
sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;
```
`fillColor` is the service category color; take it from `search_shapes` (`aws4 <service>`).

Category colors (AWS 2023+ icon set): Compute / containers `#ED7100`; Storage `#7AA116`; Database `#C925D1`; Networking `#8C4FFF`; Security / identity `#DD344C`; AI/ML `#01A88D`; App integration `#E7157B`; Management `#E7157B`; Analytics `#8C4FFF`. Confirm via search results.

## Group containers
VPC:
```
sketch=0;outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#AAB7B8;dashed=0;
```
Other `grIcon` values: `group_aws_cloud_alt` (AWS Cloud), `group_region` (Region, dashed), `group_availability_zone` (dashed), `group_security_group` (red), `group_public_subnet` (green fill `#E9F3E6`), `group_private_subnet` (blue fill `#E6F2F8`), `group_corporate_data_center`, `group_account`.

## Common services → query
Bedrock (`aws4 bedrock`), SageMaker, Transcribe, Polly, Lex, Connect, Kendra, OpenSearch, API Gateway, Lambda, ECS/EKS/Fargate, Step Functions, SQS/SNS/EventBridge, Kinesis/MSK, DynamoDB, RDS/Aurora, S3, ElastiCache, CloudFront, WAF, Shield, Route 53, Direct Connect, Transit Gateway, PrivateLink, IAM, Secrets Manager, KMS, CloudWatch, CloudTrail, GuardDuty, Security Hub.

Nesting order: AWS Cloud → Region → VPC → AZ → subnet → resources.
