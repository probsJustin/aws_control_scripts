import boto3

def mprint(message):
    print(str(message).replace("'",'"'))

ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
        ImageId="ami-0f924dc71d44d23e2",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="test"
    )
mprint(instances)