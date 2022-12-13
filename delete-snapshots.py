import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')
def delete_snapshots(tag_name, tag_value):
    described_snapshots = ec2_client.describe_snapshots(
            Filters=[
            {
                'Name': 'tag:'+tag_name,
                'Values': [
                    tag_value,
                ]
            },
        ],
    )

    for snapshot in described_snapshots['Snapshots']:
        ec2_client.delete_snapshot(SnapshotId=snapshot['SnapshotId'],)
        print(f"snapshot {snapshot['SnapshotId']} has been deleted")

delete_snapshots('created-by', 'python-script')