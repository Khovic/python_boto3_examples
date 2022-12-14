import requests
import smtplib
import os

website_address = "129.159.151.65:8080"
email_message = "Subjet: DAMN NIGGA WEBSITE BE DOWN BRO \n pls fix"

EMAIL_ADDRESS  = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_email ():
    print("Possible error with app, sending email notification")

    if response.status_code == 200:
        print("Success")
    else: 
        print("Possible error with app, sending email notification")
        send_email()
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_PASSWORD, EMAIL_PASSWORD, email_message)

try:
    response = requests.get('http://129.159.151.65:8080')
except:
    send_email()



print(response.status_code)

