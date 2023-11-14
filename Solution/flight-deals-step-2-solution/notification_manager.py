import os
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

# TWILIO_ACCOUNT_SID = "AC67cc095aac920f8648354a0b4adf3ef1"
# TWILIO_AUTH_TOKEN = "89d66e2a495647b75a08defc798a1a2c"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)


class NotificationManager:
    def __init__(self):
        account_sid = "AC67cc095aac920f8648354a0b4adf3ef1"
        auth_token = "89d66e2a495647b75a08defc798a1a2c"
        # client = Client(account_sid, auth_token)
        self.client = Client(account_sid , auth_token)



    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, message_body):
        message = self.client.messages.create(
            body = message_body,
            from_= "+18447316443",
            to = "+14087185986",

        )

        return message.sid

    # def send_emails(self, signup_email, email_body):
    #     msg = EmailMessage()
    #     msg['Subject'] = "Deal Alert"
    #     msg['From'] = "ravi.neelakantan88@gmail.com"
    #     msg['To'] = signup_email, #set this variable equal to the fucking emails
    #     msg.set_content(email_body)

    #     smtp_server = 
    #     smtp_port =
    #     your_email = 
    #     your_password = 

    #     with smtplib.SMTP(smtp_server, smtp_port) as server:
    #         server.starttls()
    #         server.login(your_email, your_password)
    #         server.send_message(msg)

            


        #in here we want to take a string, if it exists, and send it out to my personal number
        