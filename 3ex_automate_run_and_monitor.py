import boto3
ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

def create_vpc():
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

def get_vpc_id():
    my_vpcs = ec2_client.describe_vpcs(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    'My-VPC',
                ]
            },
        ],
        MaxResults=123
    ) 
    return my_vpcs['Vpcs']

my_vpcs = get_vpc_id()
#my_vpc = create_vpc
#print(my_vpc.VpcId)

if(len(my_vpcs)==0):
  print("no-vpc")
  create_vpc()

vpc_id = ""

for vpc in my_vpcs:
    print(vpc['VpcId'])
    vpc_id = vpc['VpcId']

my_subnet = ec2_client.create_subnet(
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'tag:Name',
                    'Value': 'My-Subnet'
                },
            ]
        },
    ],
    CidrBlock='10.0.1.0/28',
    VpcId=vpc_id,

)    

print(my_subnet['Subnet']['SubnetId'])

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