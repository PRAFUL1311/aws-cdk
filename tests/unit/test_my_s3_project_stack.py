import aws_cdk as core
import aws_cdk.assertions as assertions

from my_s3_project.my_s3_project_stack import MyS3ProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_s3_project/my_s3_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyS3ProjectStack(app, "my-s3-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
