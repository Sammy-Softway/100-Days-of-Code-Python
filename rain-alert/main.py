import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

OPEN_WEATHER_MAP_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

# LATITUDE = 6.451140
# LONGITUDE = 3.388400
LATITUDE = 43.653225
LONGITUDE = -79.383186

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 7,
}

response = requests.get(OPEN_WEATHER_MAP_ENDPOINT, params=weather_params)
status_code = response.status_code
response.raise_for_status()
data = response.json()

print(status_code)
print(data)

weather_id = data["list"][0]["weather"][0]["id"]
weather_description = data["list"][0]["weather"][0]["description"]
# print(weather_id)
# print(weather_description)


will_rain = False
for hourly_data in data["list"]:
    weather_id = hourly_data["weather"][0]["id"]
    # print(weather_id)
    if weather_id < 700:
        will_rain = True
if will_rain:
    # print("Bring an umbrella!")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="it's going to rain today. Remember to bring an umbrella! ☔",
        from_="+12694042693",
        to="+2348146191616",
    )
    print(message.status)
else:
    print("It won't rain today!")
