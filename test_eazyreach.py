import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("EAZYREACH_CLIENT_ID")
CLIENT_SECRET = os.getenv("EAZYREACH_CLIENT_SECRET")

url = "https://api.superflow.run/b2b/createAuthToken/"

payload = {
    "clientId": CLIENT_ID,
    "clientSecret": CLIENT_SECRET
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.text)