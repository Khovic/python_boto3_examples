import boto3
ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

"""
create_vpc = ec2_resource.create_vpc(
    CidrBlock='10.0.1.0/24',
    AmazonProvidedIpv6CidrBlock=False,
    TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'My-VPC'
                },
            ]
        },
    ]
)
"""

described_vpcs = ec2_client.describe_vpcs(

    MaxResults=123
)

my_vpc = create_vpc
print(my_vpc.VpcId)
print(described_vpcs)

"""
instances = ec2.create_instances(
    ImageId="ami-076309742d466ad69",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="desktop-win-keypair",

    NetworkInterfaces=[
            {
            'AssociatePublicIpAddress': True,
            'DeviceIndex': 0,
            'SubnetId' : "subnet-086b4620def7441b6"
            }
        ]
)
"""