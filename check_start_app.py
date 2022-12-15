import boto3
import time
import paramiko

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

"""
instances = ec2_resource.create_instances(
    ImageId="ami-076309742d466ad69",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="poopy-oracle",

    NetworkInterfaces=[
            {
            'AssociatePublicIpAddress': True,
            'DeviceIndex': 0,
            'SubnetId' : 'subnet-073db04a00010f052'
            }
    ]
)



def check_status(instance_id):
    print(instance_id)
    
    status_pass = False
    while not status_pass:
        described_instance = ec2_client.describe_instances(
        InstanceIds=[instance_id,],
        DryRun=False,)
        
        time.sleep(5)
        print(described_instance["Reservations"][0]["Instances"][0]["State"]["Name"])

        if described_instance["Reservations"][0]["Instances"][0]["State"]["Name"] == "running":
            described_instance_status = ec2_client.describe_instance_status(InstanceIds=[instance_id],)
            for status in described_instance_status['InstanceStatuses']:
                    time.sleep(5)
                    if status['SystemStatus']['Status'] == 'ok':
                        print('Instance status and System status are OK!')
                        status_pass = True

sudo yum update
sudo systemctl start docker
sudo usermod -aG docker ec2-user
restart shell
docker run -d -p 8080:80 nginx
------------
open port TCP 8080
"""

def start_app(instance_id):
    instance_ip = '3.71.72.83'

    print(f'Application starting on instance {instance_id}.....')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=instance_ip, username='ec2-user',key_filename='/home/ubuntu/.ssh/id_rsa')
    
    stdin, stdout, stderr = ssh.exec_command('sudo yum update -y')
    print(stdin.read())
    print(stdout.read())
    print(stderr.read())
    stdin, stdout, stderr = ssh.exec_command('sudo yum -y install docker')
    print(stdin.read())
    print(stdout.read())
    print(stderr.read())
    stdin, stdout, stderr = ssh.exec_command('sudo usermod -aG docker ec2-user')
    print(stdin.read())
    print(stdout.read())
    print(stderr.read())
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl start docker')
    print(stdin.read())
    print(stdout.read())
    print(stderr.read())
    ssh.close()

    ssh.connect(hostname=instance_ip, username='ec2-user',key_filename='/home/ubuntu/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl start docker')
    stdin, stdout, stderr = ssh.exec_command('docker run -d -p 8080:80 nginx')
    print(f'application on Instance {instance_id} successfully started')


start_app('i-0ffa448c0b2d1f4b0')