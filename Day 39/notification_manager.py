from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to='+15794881110'
        )
        # Prints if successfully sent.
        print(message.sid)