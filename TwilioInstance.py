from twilio.rest import Client
import os

class TwilioInstance:
    def __init__(self):
        self.client = Client(
            os.environ["TWILIO_ACCOUNT_SID"],
            os.environ["TWILIO_AUTH_TOKEN"]
        )
        self.from_whatsapp_number = f"whatsapp:{os.environ['TWILIO_PHONE_NUMBER']}"
        self.to_whatsapp_number = f"whatsapp:{os.environ['TARGET_PHONE_NUMBER']}"

    def send_sms_whatsapp(self, message):
        try:
            message = self.client.messages.create(
                to=self.to_whatsapp_number,
                from_=self.from_whatsapp_number,
                body=message
            )
            print(message.sid)
            return {
                "status": "success",
                "message_sid": message.sid
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }