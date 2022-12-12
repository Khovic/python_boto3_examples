import boto3
import time

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

instances = ec2_resource.create_instances(
    ImageId="ami-076309742d466ad69",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="poopy-oracle",

    NetworkInterfaces=[
            {
            'AssociatePublicIpAddress': True,
            'DeviceIndex': 0,
            'SubnetId' : 'subnet-073db04a00010f052'
            }
    ]
)

print(instances[0].instance_id)

described_instance = client.describe_instances(
    InstanceIds=[
        instances[0].instance_id,
    ],
    DryRun=False,
    MaxResults=123,
)

print(described_instance["Reservations"][0]["Instances"][0]["Monitoring"]["State"])

