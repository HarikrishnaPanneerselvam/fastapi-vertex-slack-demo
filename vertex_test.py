import requests
import json
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Load service account JSON
credentials = service_account.Credentials.from_service_account_file(
    "path/to/your/service-account.json",
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Get access token
auth_req = Request()
credentials.refresh(auth_req)
token = credentials.token

url = "https://us-central1-aiplatform.googleapis.com/v1/projects/inspiring-team-472217-n0/locations/us-central1/publishers/google/models/gemini-1.5-flash:predict"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "instances": [
        {"content": "Summarize: FastAPI server error connection refused"}
    ]
}

resp = requests.post(url, headers=headers, data=json.dumps(data))
print(resp.json())
