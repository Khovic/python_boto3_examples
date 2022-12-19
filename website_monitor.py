import requests
import smtplib
import os
import paramiko

"""
 This script will monitor a selected url, check if it is responding. 
 In case there is no response, it will notify by email and attempt to restart the container.
 ---------
 it is required to install (via pip) requests, smtplib, and paramiko.
 Aswell to set env.vars: EMAIL_ADDRESS, EMAIL_PASSWORD, WEB_URL, SERVER_IP.
 ---------
 The script is configured to ssh to ubuntu@SERVER_IP using key /home/ubuntu/.ssh/id_rsa,
 you might want to check line 33 prior to running.
 ---------
 for demonstration purpuses we used ngnix but restart_app() but can be configure to to restart any container.
 check line 38
"""
# Required for sending email notifications
EMAIL_ADDRESS   = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD  = os.environ.get('EMAIL_PASSWORD')
# Required for ssh'ing to the server and restarting the container
SERVER_IP       = os.environ.get('SERVER_IP')
# The URL of the website we want to monitor
website_address = os.environ.get('WEB_URL')
# The email message to best
email_message   = "Subject: Website is down \n Please take action"

#used to ssh to the server and restart the app docker container
def restart_app():
    print('Restarting the container')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=SERVER_IP, username='ubuntu',key_filename='/home/ubuntu/.ssh/id_rsa')
    #gets nginx container id and passes it app_container_id
    stdin, stdout, stderr = ssh.exec_command("docker ps -a | grep nginx | awk '{ print $1 }'")
    app_container_id = stdout.readlines()
    print(app_container_id[0])
    ssh.exec_command('docker restart ' + app_container_id[0])
    ssh.close()

#used to send email notifying of app failure
def send_email():
    print("Possible error with app, sending email notification")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, email_message)

try:
    response = requests.get(website_address)
    if response.status_code == 200:
        print("Success! Application is running")
    else:
        print('nginx responding but there is a configuration issue')
except:
    send_email()
    restart_app()


