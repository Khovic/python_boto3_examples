import boto3
from operator import itemgetter

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

    #sorts the described_snapshots in a descending order.
    sorted_snapshots = sorted(described_snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    #loops through sorted_snapshots skipping first 2 items and deletes old snapshots
    for snapshot in sorted_snapshots[2:]:
        ec2_client.delete_snapshot(SnapshotId=snapshot['SnapshotId'],)
        print(f"snapshot {snapshot['SnapshotId']} dated {snapshot['StartTime']} has been deleted")

delete_snapshots('created-by', 'python-script')