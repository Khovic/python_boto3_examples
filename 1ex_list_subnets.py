import boto3

ec2_client = boto3.client('ec2')
described_subnets = ec2_client.describe_subnets()['Subnets']

#print(described_subnets)

for subnet in range(0,len(described_subnets)):
    response = ec2_client.describe_subnets()['Subnets'][subnet]['SubnetId']
    print(response)
