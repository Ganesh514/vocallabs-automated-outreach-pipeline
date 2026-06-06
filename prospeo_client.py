import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PROSPEO_API_KEY")

def find_decision_makers(company):

    url = "https://api.prospeo.io/search-person"

    headers = {
        "X-KEY": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "page": 1,
        "filters": {
            "company": {
                "websites": {
                    "include": [company]
                }
            }
        }
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        data = response.json()

        contacts = []

        if "results" in data:

            for result in data["results"][:5]:

                person = result.get("person", {})

                contacts.append({
                    "name": person.get("full_name", "Unknown"),
                    "title": person.get("job_title", "Unknown"),
                    "linkedin": person.get("linkedin_url", ""),
                    "company": company
                })

        return contacts

    except Exception as e:
        print("Prospeo Error:", e)
        return []