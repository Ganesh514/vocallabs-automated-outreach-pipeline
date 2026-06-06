import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")

def send_email(to_email, subject, body):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "Ganesh Tech",
            "email": "ganesh@ganeshtech9.online"
        },
        "to": [
            {
                "email": to_email
            }
        ],
        "subject": subject,
        "htmlContent": f"<html><body><pre>{body}</pre></body></html>"
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    return response.status_code