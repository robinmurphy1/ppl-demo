import pulumi
from pulumi_aws import s3
from pulumi import automation as auto

bucket = s3.Bucket('ppl-pulumi-state')

ownership_controls = s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule=s3.BucketOwnershipControlsRuleArgs(
        object_ownership='ObjectWriter'
    )
)

public_access_block = s3.BucketPublicAccessBlock(
    'public-access-block',
    bucket=bucket.id,
    block_public_acls=False
)

pulumi.export('bucket_name', bucket.id)
