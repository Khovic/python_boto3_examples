import boto3
import time
import paramiko
import requests
import smtplib
import os
import schedule

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

ssh_key_file = r"/home/ubuntu/.ssh/id_rsa"

app_failures = 0

instances = ec2_resource.create_instances(
    ImageId="ami-076309742d466ad69",
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName="desktop-win-keypair",



    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeviceIndex': 0,
            'SubnetId': 'subnet-073db04a00010f052'
        }
    ]
)


def check_status(instance_id):
    print(instance_id)

    status_pass = False
    while not status_pass:
        described_instance = ec2_client.describe_instances(
            InstanceIds=[instance_id, ],
            DryRun=False, )

        time.sleep(5)
        print(described_instance["Reservations"][0]["Instances"][0]["State"]["Name"])

        if described_instance["Reservations"][0]["Instances"][0]["State"]["Name"] == "running":
            described_instance_status = ec2_client.describe_instance_status(InstanceIds=[instance_id], )
            for status in described_instance_status['InstanceStatuses']:
                time.sleep(5)
                if status['SystemStatus']['Status'] == 'ok':
                    print('Instance status and System status are OK!')
                    status_pass = True


def start_app(instance_id):
    # to get the instance public ip
    instance = ec2_resource.Instance(instance_id)
    print(instance.public_ip_address)
    instance_ip = instance.public_ip_address

    print(f'Application starting on instance {instance_id}.....')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=instance_ip, username='ec2-user', key_filename=ssh_key_file)

    print('updating yum..')
    stdin, stdout, stderr = ssh.exec_command('sudo yum update -y')
    print(stdout.readlines())
    print('installing docker..')
    stdin, stdout, stderr = ssh.exec_command('sudo yum -y install docker')
    print(stdout.readlines())
    stdin, stdout, stderr = ssh.exec_command('sudo usermod -aG docker ec2-user')
    print(stdout.readlines())
    stdin, stdout, stderr = ssh.exec_command('sudo systemctl start docker')
    print(stdout.readlines())
    print('running nginx..')
    stdin, stdout, stderr = ssh.exec_command('sudo docker run -d -p 8080:80 nginx')
    print(stdout.readlines())

    print(f'Application on instance {instance_id} successfully started')

    return instance_ip


def open_port(instance_id):
    instance = ec2_resource.Instance(instance_id)
    instance_sg = instance.security_groups[0]["GroupId"]

    ec2_client.authorize_security_group_ingress(
        GroupId=instance_sg,
        IpPermissions=[
            {
                'FromPort': 8080,
                'ToPort': 8080,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0'
                    }
                ]
            }
        ]
    )


# used to ssh to the server and restart the app docker container
def restart_app(instance_ip):
    print('Restarting the container')

    ssh = paramiko.SSHClient()
    # to accept the "add missing host prompt"
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=instance_ip, username='ec2-user', key_filename=r'C:\Users\Khovic\.ssh\id_rsa')
    stdin, stdout, stderr = ssh.exec_command("docker ps -a | grep nginx | awk '{ print $1 }'")
    app_container_id = stdout.readlines()
    print(app_container_id[0])
    ssh.exec_command('docker restart ' + app_container_id[0])
    ssh.close()


# used to send email notifying of app failure
def send_email():
    print("Possible error with app, sending email notification")
    email_message = "Subject: DAMN NIGGA WEBSITE BE DOWN BRO\npls fix"

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_message)


def app_monitor(instance_ip):
    global app_failures
    print("Monitoring application...")
    print("Failures: " + str(app_failures))
    try:
        response = requests.get(f'http://{instance_ip}:8080')
        if response.status_code == 200:
            print("Success! Application is running")
            app_failures = 0
        else:
            print('nginx responding but there is a configuration issue')
    except:
        #send_email()
        print("application failed")
        app_failures = app_failures + 1

    if app_failures > 4:
        restart_app(instance_ip)

    return


check_status(instances[0].instance_id)

instance_ip = start_app(instances[0].instance_id)

try:
    open_port(instances[0].instance_id)
except:
    print("Port is already open")

print("running monitor...")

schedule.every(6).seconds.do(app_monitor, instance_ip)

while True:
    schedule.run_pending()
