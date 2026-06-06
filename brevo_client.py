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
        "htmlContent": f"""
        <html>
        <body>
        <pre>{body}</pre>
        </body>
        </html>
        """
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        print("\n==========================")
        print("BREVO DEBUG")
        print("==========================")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        print("==========================\n")

        return response.status_code

    except Exception as e:
        print("Brevo Error:", e)
        return None