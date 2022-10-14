import boto3



def run(application_name, image_id, instance_type, key_name, security_groups):
    if(application_name is None):
        raise Exception(f'Need to pass a application_name to create instance. Received: {application_name}')
    if(image_id is None):
        raise Exception(f'Need to pass a image_id to create instance. Received: {image_id}')
    if(instance_type is None):
        raise Exception(f'Need to pass a instance_type to create instance. Received: {instance_type}')
    if(key_name is None):
        raise Exception(f'Need to pass a key_name to create instance. Received: {key_name}')

    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
            TagSpecifications=[{
                "ResourceType": "instance",
                "Tags":[{
                    "Key": "Name",
                    "Value": f'{application_name}'
                }]
            }],
            ImageId=f'{image_id}',
            MinCount=1,
            MaxCount=1,
            InstanceType=f'{instance_type}',
            KeyName=f'{key_name}',
            SecurityGroups=security_groups
        )
    return instances