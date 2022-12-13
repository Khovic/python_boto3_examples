import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

described_instance = ec2_client.describe_instances()
reservations = described_instance["Reservations"]

described_instance_statutes = ec2_client.describe_instance_status(
)

described_volume = client.describe_volumes(
   VolumeIds=[
        'string',
    ],
)

def check_status():
    for status in described_instance_statutes['InstanceStatuses']:
        print(f'instance {status["InstanceId"]} is {status["InstanceState"]["Name"]} and system status is {status["SystemStatus"]["Status"]}')

        described_volumes = ec2_client.describe_volumes(
        Filters=[{'Name': 'attachment.instance-id', 'Values': [status["InstanceId"]]}]
        )

        for volume in described_volumes['Volumes']:
            print("attached volumes: ")
            for attachment in volume['Attachments']:
                print(f"{attachment['VolumeId']}")


check_status()