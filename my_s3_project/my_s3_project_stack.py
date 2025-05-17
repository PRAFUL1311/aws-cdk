from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct

class MyS3ProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the S3 bucket
        s3.Bucket(self, "MyBucket",
            bucket_name="my-unique-bucket-name-1234ddd567890",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY  # for testing/dev
        )
