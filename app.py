import boto3

def mprint(message):
    print(str(message).replace("'",'"'))

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
mprint(response)