import boto3

def run():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    return response



def find_instance(ec2_name):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instances in reservation['Instances']:
            for tag in instances['Tags']:
                if (tag['Key'] == 'Name' and tag['Value'] == ec2_name):
                    return instances