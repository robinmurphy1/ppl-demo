# Pulumi Cloud

[Pulumi Cloud - Robin](https://app.pulumi.com/robinmurphy1/dvt/dev/previews/5f0d5891-c17d-4ae7-b908-bba3335fb804) 

A secure cloud service to manage cloud environments and resources. It manages the environment states, handles deployments, integrates with CI/CD systems( eg Gitlab CI/CD)

## Features of Pulumi Cloud

## S3 resource example
Creating an S3 bucket with policies & bucket object <div id="S3-resource-example"></div>

```
     Type                               Name                 Plan       
 +   pulumi:pulumi:Stack                dvt-dev              create     
 +   ├─ aws:s3:BucketObject             index.html           create     
 +   ├─ aws:s3:Bucket                   ppl-dvt-pulumi-test  create     
 +   ├─ aws:s3:BucketOwnershipControls  ownership-controls   create     
 +   └─ aws:s3:BucketPublicAccessBlock  public-access-block  create     
 
Outputs:
    bucket_endpoint: output<string>

Resources:
    + 5 to create

```
Serverless API, API Gateway & Lambda
```
Updating (http-api)

     Type                             Name                                   Status
 +   pulumi:pulumi:Stack              aws-ts-apigatewayv2-http-api-http-api  created
 +   ├─ aws:apigatewayv2:Api          httpApiGateway                         created
 +   ├─ aws:iam:Role                  lambdaRole                             created
 +   ├─ aws:lambda:Function           lambdaFunction                         created
 +   ├─ aws:iam:RolePolicyAttachment  lambdaRoleAttachment                   created
 +   ├─ aws:lambda:Permission         lambdaPermission                       created
 +   ├─ aws:apigatewayv2:Integration  lambdaIntegration                      created
 +   ├─ aws:apigatewayv2:Route        apiRoute                               created
 +   └─ aws:apigatewayv2:Stage        apiStage                               created

Outputs:
    endpoint: "https://****.execute-api.us-east-2.amazonaws.com/http-api"

Resources:
    + 9 created

Duration: 33s

```
- Estimated resources: 9
- Estimated monthly cost : $3.28 USD / 6,570 credits

ECS cluster & RDS running in VPC
```
$ pulumi up
 +   pulumi:pulumi:Stack                  lamp-rds-wordpress-testing        create
 +   ├─ custom:resource:VPC               wp-example-net                    create
 +   │  ├─ aws:ec2:Vpc                    wp-example-net-vpc                create
 +   pulumi:pulumi:Stack                  lamp-rds-wordpress-testing        create.
 +   pulumi:pulumi:Stack                  lamp-rds-wordpress-testing        create
 +   │  ├─ aws:ec2:Subnet                 wp-example-net-subnet-us-west-2a  create
 +   │  ├─ aws:ec2:Subnet                 wp-example-net-subnet-us-west-2b  create
 +   │  ├─ aws:ec2:SecurityGroup          wp-example-net-rds-sg             create
 +   │  ├─ aws:ec2:SecurityGroup          wp-example-net-fe-sg              create
 +   │  ├─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-us-west-2a  create
 +   │  └─ aws:ec2:RouteTableAssociation  vpc-route-table-assoc-us-west-2b  create
 +   ├─ random:index:RandomPassword       db_password                       create
 +   ├─ custom:resource:Backend           wp-example-be                     create
 +   │  ├─ aws:rds:SubnetGroup            wp-example-be-sng                 create
 +   │  └─ aws:rds:Instance               wp-example-be-rds                 create
 +   └─ custom:resource:Frontend          wp-example-fe                     create
 +      ├─ aws:ecs:Cluster                wp-example-fe-ecs                 create
 +      ├─ aws:iam:Role                   wp-example-fe-task-role           create
 +      ├─ aws:lb:TargetGroup             wp-example-fe-app-tg              create
 +      ├─ aws:iam:RolePolicyAttachment   wp-example-fe-task-policy         create
 +      ├─ aws:lb:LoadBalancer            wp-example-fe-alb                 create
 +      ├─ aws:lb:Listener                wp-example-fe-listener            create
 +      └─ aws:ecs:Service                wp-example-fe-app-svc             create

```
- Estimated resources: 24
- Estimated monthly cost : $8.76 USD / 17,520 credits