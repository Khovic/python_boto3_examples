import boto3
ec2 = boto3.resource('ec2')

response = ec2.create_vpc(
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

/*
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
*/