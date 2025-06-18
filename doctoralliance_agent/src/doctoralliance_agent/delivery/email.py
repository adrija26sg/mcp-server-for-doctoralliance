import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

_sg   = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
FROM  = os.getenv("FROM_EMAIL")

def send_email(body: str, context: dict):
    to = context.get("user_email")
    msg = Mail(from_email=FROM, to_emails=to,
               subject="AI Agent Response", html_content=body)
    resp = _sg.send(msg)
    return {"status": resp.status_code}
