import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

described_snapshots = ec2_client.describe_snapshots(
        Filters=[
        {
            'Name': 'tag:created-by',
            'Values': [
                'python-script',
            ]
        },
    ],
)

for snapshot in described_snapshots['Snapshots']:
    client.delete_snapshot(SnapshotId=snapshot['SnapshotId'],)
    print(f"snapshot {snapshot['SnapshotId']} has been deleted")