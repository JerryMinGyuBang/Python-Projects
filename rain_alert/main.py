import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")
account_sid = "ACa60412db42cdf4e529e68f29ada31400"
auth_token = os.getenv("AUTH_TOKEN")


weather_params = {
    "lat": 49.283764,
    "lon": -122.793205,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+14155240318",
        to="+16478348405"
    )
    print(message.status)