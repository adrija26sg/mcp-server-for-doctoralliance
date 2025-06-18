from .sms_gateway import send_sms
from .email       import send_email
from .popup       import send_popup
from .logger      import audit

def deliver(event_type: str, response: str, context: dict):
    results = {}
    for ch in context.get("channels", ["email"]):
        if ch == "sms":
            results["sms"] = send_sms(response, context)
        if ch == "email":
            results["email"] = send_email(response, context)
        if ch == "popup":
            results["popup"] = send_popup(response, context)
        audit(event_type, {"response": response}, ch)
    return results
