import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

described_instance = ec2_client.describe_instances()
reservations = described_instance["Reservations"]

def check_status():
    for reservation in reservations:
        for instance in reservation["Instances"]:
            print(f'instance {instance["InstanceId"]} is {instance["State"]["Name"]}')


check_status()