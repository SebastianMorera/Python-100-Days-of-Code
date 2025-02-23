from dotenv import load_dotenv
import smtplib
import os
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_TESTING_GOOGLE_EMAIL"]
        self.email_password = os.environ["MY_TESTING_GOOGLE_APP_PASSWORD"]

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to='+15794881110'
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP(self.smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(self.email, self.email_password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )