ResourceMap = {
    "aws.account": "c7n.resources.account.Account",
    "aws.acm-certificate": "c7n.resources.acm.Certificate",
    "aws.alarm": "c7n.resources.cw.Alarm",
    "aws.ami": "c7n.resources.ami.AMI",
    "aws.app-elb": "c7n.resources.appelb.AppELB",
    "aws.app-elb-target-group": "c7n.resources.appelb.AppELBTargetGroup",
    "aws.asg": "c7n.resources.asg.ASG",
    "aws.backup-plan": "c7n.resources.backup.BackupPlan",
    "aws.batch-compute": "c7n.resources.batch.ComputeEnvironment",
    "aws.batch-definition": "c7n.resources.batch.JobDefinition",
    "aws.cache-cluster": "c7n.resources.elasticache.ElastiCacheCluster",
    "aws.cache-snapshot": "c7n.resources.elasticache.ElastiCacheSnapshot",
    "aws.cache-subnet-group": "c7n.resources.elasticache.ElastiCacheSubnetGroup",
    "aws.cfn": "c7n.resources.cfn.CloudFormation",
    "aws.cloud-directory": "c7n.resources.directory.CloudDirectory",
    "aws.cloudhsm-cluster": "c7n.resources.hsm.CloudHSMCluster",
    "aws.cloudsearch": "c7n.resources.cloudsearch.CloudSearch",
    "aws.cloudtrail": "c7n.resources.cloudtrail.CloudTrail",
    "aws.codebuild": "c7n.resources.code.CodeBuildProject",
    "aws.codecommit": "c7n.resources.code.CodeRepository",
    "aws.codepipeline": "c7n.resources.code.CodeDeployPipeline",
    "aws.config-recorder": "c7n.resources.config.ConfigRecorder",
    "aws.config-rule": "c7n.resources.config.ConfigRule",
    "aws.customer-gateway": "c7n.resources.vpc.CustomerGateway",
    "aws.datapipeline": "c7n.resources.datapipeline.DataPipeline",
    "aws.dax": "c7n.resources.dynamodb.DynamoDbAccelerator",
    "aws.directconnect": "c7n.resources.directconnect.DirectConnect",
    "aws.directory": "c7n.resources.directory.Directory",
    "aws.distribution": "c7n.resources.cloudfront.Distribution",
    "aws.dlm-policy": "c7n.resources.dlm.DLMPolicy",
    "aws.dms-endpoint": "c7n.resources.dms.DmsEndpoints",
    "aws.dms-instance": "c7n.resources.dms.ReplicationInstance",
    "aws.dynamodb-backup": "c7n.resources.dynamodb.Backup",
    "aws.dynamodb-stream": "c7n.resources.dynamodb.Stream",
    "aws.dynamodb-table": "c7n.resources.dynamodb.Table",
    "aws.ebs": "c7n.resources.ebs.EBS",
    "aws.ebs-snapshot": "c7n.resources.ebs.Snapshot",
    "aws.ec2": "c7n.resources.ec2.EC2",
    "aws.ec2-reserved": "c7n.resources.ec2.ReservedInstance",
    "aws.ecr": "c7n.resources.ecr.ECR",
    "aws.ecs": "c7n.resources.ecs.ECSCluster",
    "aws.ecs-container-instance": "c7n.resources.ecs.ContainerInstance",
    "aws.ecs-service": "c7n.resources.ecs.Service",
    "aws.ecs-task": "c7n.resources.ecs.Task",
    "aws.ecs-task-definition": "c7n.resources.ecs.TaskDefinition",
    "aws.efs": "c7n.resources.efs.ElasticFileSystem",
    "aws.efs-mount-target": "c7n.resources.efs.ElasticFileSystemMountTarget",
    "aws.eks": "c7n.resources.eks.EKS",
    "aws.elasticbeanstalk": "c7n.resources.elasticbeanstalk.ElasticBeanstalk",
    "aws.elasticbeanstalk-environment": (
        "c7n.resources.elasticbeanstalk.ElasticBeanstalkEnvironment"),
    "aws.elasticsearch": "c7n.resources.elasticsearch.ElasticSearchDomain",
    "aws.elb": "c7n.resources.elb.ELB",
    "aws.emr": "c7n.resources.emr.EMRCluster",
    "aws.eni": "c7n.resources.vpc.NetworkInterface",
    "aws.event-rule": "c7n.resources.cw.EventRule",
    "aws.event-rule-target": "c7n.resources.cw.EventRuleTarget",
    "aws.firehose": "c7n.resources.kinesis.DeliveryStream",
    "aws.fsx": "c7n.resources.fsx.FSx",
    "aws.fsx-backup": "c7n.resources.fsx.FSxBackup",
    "aws.gamelift-build": "c7n.resources.gamelift.GameLiftBuild",
    "aws.gamelift-fleet": "c7n.resources.gamelift.GameLiftFleet",
    "aws.glacier": "c7n.resources.glacier.Glacier",
    "aws.glue-connection": "c7n.resources.glue.GlueConnection",
    "aws.glue-crawler": "c7n.resources.glue.GlueCrawler",
    "aws.glue-database": "c7n.resources.glue.GlueDatabase",
    "aws.glue-dev-endpoint": "c7n.resources.glue.GlueDevEndpoint",
    "aws.glue-job": "c7n.resources.glue.GlueJob",
    "aws.glue-table": "c7n.resources.glue.GlueTable",
    "aws.health-event": "c7n.resources.health.HealthEvents",
    "aws.healthcheck": "c7n.resources.route53.HealthCheck",
    "aws.hostedzone": "c7n.resources.route53.HostedZone",
    "aws.hsm": "c7n.resources.hsm.CloudHSM",
    "aws.hsm-client": "c7n.resources.hsm.HSMClient",
    "aws.hsm-hapg": "c7n.resources.hsm.PartitionGroup",
    "aws.iam-certificate": "c7n.resources.iam.ServerCertificate",
    "aws.iam-group": "c7n.resources.iam.Group",
    "aws.iam-policy": "c7n.resources.iam.Policy",
    "aws.iam-profile": "c7n.resources.iam.InstanceProfile",
    "aws.iam-role": "c7n.resources.iam.Role",
    "aws.iam-user": "c7n.resources.iam.User",
    "aws.identity-pool": "c7n.resources.cognito.CognitoIdentityPool",
    "aws.internet-gateway": "c7n.resources.vpc.InternetGateway",
    "aws.iot": "c7n.resources.iot.IoT",
    "aws.kafka": "c7n.resources.kafka.Kafka",
    "aws.key-pair": "c7n.resources.vpc.KeyPair",
    "aws.kinesis": "c7n.resources.kinesis.KinesisStream",
    "aws.kinesis-analytics": "c7n.resources.kinesis.AnalyticsApp",
    "aws.kms": "c7n.resources.kms.KeyAlias",
    "aws.kms-key": "c7n.resources.kms.Key",
    "aws.lambda": "c7n.resources.awslambda.AWSLambda",
    "aws.lambda-layer": "c7n.resources.awslambda.LambdaLayerVersion",
    "aws.launch-config": "c7n.resources.asg.LaunchConfig",
    "aws.launch-template-version": "c7n.resources.ec2.LaunchTemplate",
    "aws.lightsail-db": "c7n.resources.lightsail.Database",
    "aws.lightsail-elb": "c7n.resources.lightsail.LoadBalancer",
    "aws.lightsail-instance": "c7n.resources.lightsail.Instance",
    "aws.log-group": "c7n.resources.cw.LogGroup",
    "aws.message-broker": "c7n.resources.mq.MessageBroker",
    "aws.ml-model": "c7n.resources.ml.MLModel",
    "aws.nat-gateway": "c7n.resources.vpc.NATGateway",
    "aws.network-acl": "c7n.resources.vpc.NetworkAcl",
    "aws.network-addr": "c7n.resources.vpc.NetworkAddress",
    "aws.ops-item": "c7n.resources.ssm.OpsItem",
    "aws.opswork-cm": "c7n.resources.opsworks.OpsworksCM",
    "aws.opswork-stack": "c7n.resources.opsworks.OpsworkStack",
    "aws.peering-connection": "c7n.resources.vpc.PeeringConnection",
    'aws.qldb': 'c7n.resources.qldb.QLDB',
    "aws.r53domain": "c7n.resources.route53.Route53Domain",
    "aws.rds": "c7n.resources.rds.RDS",
    "aws.rds-cluster": "c7n.resources.rdscluster.RDSCluster",
    "aws.rds-cluster-param-group": "c7n.resources.rdsparamgroup.RDSClusterParamGroup",
    "aws.rds-cluster-snapshot": "c7n.resources.rdscluster.RDSClusterSnapshot",
    "aws.rds-param-group": "c7n.resources.rdsparamgroup.RDSParamGroup",
    "aws.rds-reserved": "c7n.resources.rds.ReservedRDS",
    "aws.rds-snapshot": "c7n.resources.rds.RDSSnapshot",
    "aws.rds-subnet-group": "c7n.resources.rds.RDSSubnetGroup",
    "aws.rds-subscription": "c7n.resources.rds.RDSSubscription",
    "aws.redshift": "c7n.resources.redshift.Redshift",
    "aws.redshift-snapshot": "c7n.resources.redshift.RedshiftSnapshot",
    "aws.redshift-subnet-group": "c7n.resources.redshift.RedshiftSubnetGroup",
    "aws.rest-account": "c7n.resources.apigw.RestAccount",
    "aws.rest-api": "c7n.resources.apigw.RestApi",
    "aws.rest-resource": "c7n.resources.apigw.RestResource",
    "aws.rest-stage": "c7n.resources.apigw.RestStage",
    "aws.rest-vpclink": "c7n.resources.apigw.RestApiVpcLink",
    "aws.route-table": "c7n.resources.vpc.RouteTable",
    "aws.rrset": "c7n.resources.route53.ResourceRecordSet",
    "aws.s3": "c7n.resources.s3.S3",
    "aws.sagemaker-endpoint": "c7n.resources.sagemaker.SagemakerEndpoint",
    "aws.sagemaker-endpoint-config": "c7n.resources.sagemaker.SagemakerEndpointConfig",
    "aws.sagemaker-job": "c7n.resources.sagemaker.SagemakerJob",
    "aws.sagemaker-model": "c7n.resources.sagemaker.Model",
    "aws.sagemaker-notebook": "c7n.resources.sagemaker.NotebookInstance",
    "aws.sagemaker-transform-job": "c7n.resources.sagemaker.SagemakerTransformJob",
    "aws.secrets-manager": "c7n.resources.secretsmanager.SecretsManager",
    "aws.security-group": "c7n.resources.vpc.SecurityGroup",
    "aws.shield-attack": "c7n.resources.shield.ShieldAttack",
    "aws.shield-protection": "c7n.resources.shield.ShieldProtection",
    "aws.simpledb": "c7n.resources.simpledb.SimpleDB",
    "aws.snowball": "c7n.resources.snowball.Snowball",
    "aws.snowball-cluster": "c7n.resources.snowball.SnowballCluster",
    "aws.sns": "c7n.resources.sns.SNS",
    "aws.sqs": "c7n.resources.sqs.SQS",
    "aws.ssm-activation": "c7n.resources.ssm.SSMActivation",
    "aws.ssm-managed-instance": "c7n.resources.ssm.ManagedInstance",
    "aws.ssm-parameter": "c7n.resources.ssm.SSMParameter",
    "aws.step-machine": "c7n.resources.sfn.StepFunction",
    "aws.storage-gateway": "c7n.resources.storagegw.StorageGateway",
    "aws.streaming-distribution": "c7n.resources.cloudfront.StreamingDistribution",
    "aws.subnet": "c7n.resources.vpc.Subnet",
    "aws.support-case": "c7n.resources.support.SupportCase",
    "aws.transit-attachment": "c7n.resources.vpc.TransitGatewayAttachment",
    "aws.transit-gateway": "c7n.resources.vpc.TransitGateway",
    "aws.user-pool": "c7n.resources.cognito.CognitoUserPool",
    "aws.vpc": "c7n.resources.vpc.Vpc",
    "aws.vpc-endpoint": "c7n.resources.vpc.VpcEndpoint",
    "aws.vpn-connection": "c7n.resources.vpc.VPNConnection",
    "aws.vpn-gateway": "c7n.resources.vpc.VPNGateway",
    "aws.waf": "c7n.resources.waf.WAF",
    "aws.waf-regional": "c7n.resources.waf.RegionalWAF",
    "aws.workspaces": "c7n.resources.workspaces.Workspace"
}
