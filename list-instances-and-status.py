import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

def check_status():
    print()

described_instance = ec2_client.describe_instances()
reservations = described_instance["Reservations"]

for reservation in reservations:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"])
        print(instance["State"]["Name"])


check_status()