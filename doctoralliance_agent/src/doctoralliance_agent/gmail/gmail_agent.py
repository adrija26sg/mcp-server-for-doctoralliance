import os, base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from .nlp_parser      import parse_reply
from .response_handler import handle_response

def listen_inbox():
    creds = Credentials.from_authorized_user_file(
        os.getenv("GMAIL_CREDENTIALS_PATH"),
        ['https://www.googleapis.com/auth/gmail.modify']
    )
    svc = build('gmail','v1',credentials=creds)
    msgs = svc.users().messages().list(
        userId='me',labelIds=['INBOX'],q='is:unread'
    ).execute()
    for m in msgs.get('messages', []):
        data = svc.users().messages().get(
            userId='me', id=m['id'], format='full'
        ).execute()
        raw = data['payload']['parts'][0]['body']['data']
        text = base64.urlsafe_b64decode(raw).decode()
        parsed = parse_reply(text)
        handle_response(parsed)
