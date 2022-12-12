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

def check_status(instance_id):
    status_pass = False
    while not status_pass:
        described_instance = ec2_client.describe_instances(
        InstanceIds=[instance_id,],
        DryRun=False,)
        
        time.sleep(5)
        print(described_instance["Reservations"][0]["Instances"][0]["State"]["Name"])

        if described_instance["Reservations"][0]["Instances"][0]["State"]["Name"] == "running":
            status_pass = True

check_status(instances[0].instance_id)