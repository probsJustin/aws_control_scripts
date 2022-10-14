import boto3

def run():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    return response



def find_instances(ec2_name):
    instances_to_return = list()
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instances in reservation['Instances']:
            for tag in instances['Tags']:
                if (tag['Key'] == 'Name' and tag['Value'] == ec2_name):
                    instances_to_return.append(instances)
    return instances_to_return


def find_running_instances(ec2_name):
    instances_to_return = list()
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instances in reservation['Instances']:
            for tag in instances['Tags']:
                if (tag['Key'] == 'Name' and tag['Value'] == ec2_name and instances['State']['Name'] == "running"):
                    instances_to_return.append(instances)
    return instances_to_return

def find_instances_not_terminated(ec2_name):
    instances_to_return = list()
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instances in reservation['Instances']:
            for tag in instances['Tags']:
                if (tag['Key'] == 'Name' and tag['Value'] == ec2_name and instances['State']['Name'] != "terminated"):
                    instances_to_return.append(instances)
    return instances_to_return


def get_instance_status_running(tag_name):
    describe_response = run()
    ec2_instance = find_instances_not_terminated(tag_name)
    for instance in ec2_instance:
        if(instance['State']['Name'] == 'running'):
            return True
        else:
            return False