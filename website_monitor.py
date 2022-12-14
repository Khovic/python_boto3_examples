import requests
import smtplib
import os
import paramiko


website_address = "129.159.151.65:8080"
email_message = "Subject: DAMN NIGGA WEBSITE BE DOWN BRO\npls fix"

EMAIL_ADDRESS  = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

#used to ssh to the server and restart the app docker container
def restart_app():
    ssh = paramiko.SSHClient()
    #to accept the "add missing host prompt"
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='129.159.151.65', username='ubuntu',key_filename='/home/ubuntu/.ssh/id_rsa')
    stdin, stdout, stderr = ssh.exec_command("docker ps -a | grep nginx | awk '{ print $1 }'")
    app_container_id = stdout.readlines()
    print(app_container_id[0])
    ssh.exec_command(f'docker restart {app_container_id}')
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
    response = requests.get('http://129.159.151.65:8080')
    if response.status_code == 200:
        print("Success")
except:
    print("Possible error with app, sending email notification")
   # send_email()
    restart_app()



#print(response.status_code)

