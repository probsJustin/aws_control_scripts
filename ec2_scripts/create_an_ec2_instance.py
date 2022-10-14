import boto3
from ec2_scripts import constants


def mprint(message):
    print(str(message).replace("'",'"'))

ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags":[{
                "Key": "Name",
                "Value": f'Deployment-App-{constants.APPLICATION_NAME}'
            }]
        }],
        ImageId=f'{constants.AWS_LINUX_IMAGE_ID}',
        MinCount=1,
        MaxCount=1,
        InstanceType=f'{constants.AWS_INSTANCE_TYPE}',
        KeyName=f'{constants.KEY_NAME}'
    )
mprint(instances)