import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "cd84944992698431db38e1015eff7ead"

weather_params = {
    "lat": 43.653225,
    "lon": -79.383186,
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
    print("Bring an umbrella.")