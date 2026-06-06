import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("EAZYREACH_CLIENT_ID")
CLIENT_SECRET = os.getenv("EAZYREACH_CLIENT_SECRET")

# Step 1 - Get token
auth_response = requests.post(
    "https://api.superflow.run/b2b/createAuthToken/",
    json={
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET
    }
)

token = auth_response.json()["authToken"]

print("Token received")

# Step 2 - Lookup email
lookup_response = requests.post(
    "https://api.superflow.run/b2b/linkedin-emails",
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    },
    json={
        "linkedinUrl": "https://www.linkedin.com/in/satyanadella/"
    }
)

print(lookup_response.status_code)
print(lookup_response.text)