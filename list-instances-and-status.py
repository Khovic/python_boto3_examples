import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

described_instance = ec2_client.describe_instances()
reservations = described_instance["Reservations"]

described_instance_statutes = ec2_client.describe_instance_status(
)

def check_status():
    for status in described_instance_statutes['InstanceStatuses']:
        print(f'instance {status["InstanceId"]} is {status["InstanceState"]["Name"]}')


check_status()