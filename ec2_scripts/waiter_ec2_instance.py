import boto3

def run(instance, ec2_status):
    ec2 = boto3.client('ec2')
    waiter = ec2.get_waiter(ec2_status)
    waiter.wait(InstanceIds=[instance])
    return waiter

def wait_for_status_ok(instance):
    ec2 = boto3.client('ec2')
    waiter = ec2.get_waiter('instance_status_ok')
    waiter.wait(InstanceIds=[instance])
    return waiter