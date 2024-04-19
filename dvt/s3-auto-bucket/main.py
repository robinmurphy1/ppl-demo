import json
import sys

import pulumi
from pulumi_aws import s3
from pulumi import automation as auto

AWS_REGION = "eu-west-1"

def pulumi_inline():
    print("executing inline function")
    state_bucket = s3.Bucket('ppl-pulumi-state')

    public_access_block = s3.get_account_public_access_block("statePublicAccessBlock")

    s3.BucketPolicy('bucket-policy', bucket=state_bucket.id, policy=state_bucket.id.apply(
        lambda id: json.dumps({
            "Version": "2012-10-17",
            "Statement": {
                "Effect": "",
                "Principle": "",
                "Action": ["s3:GetObject"],
                "Resource": ["arn:aws:s3:::{id}/*"]
            }
        })
    ), opts=pulumi.ResourceOptions(depends_on=public_access_block))

    pulumi.export("Pulumi state bucket arn: ", state_bucket.arn)
    print("created bucket & set policy")

    destroy = False
    args = sys.argv[1:]
    if len(args) > 0:
        if args[0] == "destroy":
            destroy = True

    project_name = "PPL_Auto_Start"
    stack_name="dev"
    # stack_name= auto.fully_qualified_stack_name("PPL", "pulumi-demo", "dev")

    stack = auto.create_or_select_stack(stack_name=stack_name,
                                        project_name=project_name,
                                        program=pulumi_inline)

    stack.workspace.install_plugin("aws", "v4.0.0")
    stack.set_config("aws:region", auto.ConfigValue(value=AWS_REGION))
    stack.refresh(on_output=print)

    if destroy:
        stack.destroy(on_output=print)
        sys.exit()

    up_res= stack.up(on_output=print)

    print(f"Summary: \n{json.dumps(up_res.summary.resource_changes, indent=4)}")


