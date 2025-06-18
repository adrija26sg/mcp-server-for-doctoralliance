import os
from twilio.rest import Client

_client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
FROM    = os.getenv("TWILIO_FROM_NUMBER")

def send_sms(body: str, context: dict):
    to  = context.get("user_phone")
    msg = _client.messages.create(body=body, from_=FROM, to=to)
    return {"sid": msg.sid}
