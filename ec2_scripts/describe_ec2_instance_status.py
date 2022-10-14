import boto3


def run(instance):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instance_status(
        InstanceIds=[instance]
    )
    return response
