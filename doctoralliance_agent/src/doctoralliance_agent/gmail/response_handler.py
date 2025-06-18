from delivery.logger     import audit
from escalation.retry_agent import RetryAgent

def handle_response(parsed: dict):
    audit('email_reply', parsed, 'email')
    action = parsed.get('action')
    if action == 'retry':
        RetryAgent().retry(parsed.get('event_type','default'), parsed)
