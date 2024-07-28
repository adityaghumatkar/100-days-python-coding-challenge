# Work out tracking using Google sheets

import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

BASE_URL = "https://trackapi.nutritionix.com"
APP_ID = "<app id>>"
API_KEY = "<api key>"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query = input("What did you exercise today?")
body = {
    "query": query,
    "weight_kg": 65,
    "height_cm": 175,
    "age": 27
}
response = requests.post(url=f"{BASE_URL}/v2/natural/exercise", headers=headers, json=body)
response.raise_for_status()
data = response.json()

SHEETY_ENDPOINT = "https://api.sheety.co/e25ff9efe32e0582acab9e2e66697751/myWorkoutsTracking/workouts"
sheety_header = {
    "Content-Type": "application/json"
}
date = datetime.now()

date_col = date.strftime("%d/%m/%Y")
time_col = date.strftime("%X")

USER = "<username>"
PASSWORD = "<password>"
auth = HTTPBasicAuth(USER,PASSWORD)
TOKEN = "<your token>"
bearer_header = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

for exercise in data["exercises"]:
    body = {
        "workout": {
            "date": date_col,
            "time": time_col,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    requests.post(
        url=SHEETY_ENDPOINT,
        headers=bearer_header,
        json= body
    )
