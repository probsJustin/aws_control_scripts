import boto3

def run():
    response_to_return = list()
    list_of_instances = list()

    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    for reservations in response['Reservations']:
        for instance in reservations['Instances']:
            list_of_instances.append(instance['InstanceId'])

    ec2_resource = boto3.resource('ec2')
    for instance in list_of_instances:
        response = ec2_resource.Instance(instance).restart()
        response_to_return.append(f'{response}')
    return response_to_return