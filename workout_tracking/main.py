import requests
from datetime import datetime
from dotenv import load_dotenv
import os

WEIGHT = 90
HEIGHT = 90
AGE = 28

app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
sheet_endpoint = os.getenv("SHEET_ENDPOINT")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


query_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

params = {
    "query": query_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()

# Format display date and display time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Make post request to the spreadsheet using Sheety (API)

header = {
    "Authorization" : "Basic amVycnliYW5nOmplcnJ5YmFuZzAyMDM="
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=header)
    print(sheet_response.text)