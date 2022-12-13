import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

described_snapshots = ec2_client.describe_snapshots()

for snapshot in described_snapshots{'Snapshots'}
    print(snapshot['SnapshotId'])