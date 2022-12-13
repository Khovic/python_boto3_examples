import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

described_instance = ec2_client.describe_instances()
reservations = described_instance["Reservations"]

described_instance_statutes = ec2_client.describe_instance_status(
)

described_volume = ec2_client.describe_volumes(
)

def create_snapshots():
    for status in described_instance_statutes['InstanceStatuses']:
        #the follwing prints the volumes attached to each instance
        described_volumes = ec2_client.describe_volumes(
        Filters=[{'Name': 'attachment.instance-id', 'Values': [status["InstanceId"]]}]
        )

        for volume in described_volumes['Volumes']:
            print("attached volumes: ")
            for attachment in volume['Attachments']:
                print(f"volume {attachment['VolumeId']} attached to instance {status['InstanceId']}")

                volume = ec2_resource.Volume(attachment['VolumeId'])
                snapshot = volume.create_snapshot(
                    TagSpecifications=[
                        {
                            'ResourceType': 'snapshot'
                            'Tags': [
                                {
                                    'Key': 'tag:created-by',
                                    'Value': 'python-script'
                                },
                            ]
                        },
                    ],
                )

                print(snapshot.snapshot_id)


create_snapshots()