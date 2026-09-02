import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.environ.get("API_KEY")
app_id = os.environ.get("APP_ID")
sheety_username = os.environ.get("SHEETY_USERNAME")
sheety_password = os.environ.get("SHEETY_PASSWORD")
sheety_auth = os.environ.get("SHEETY_AUTH")

sheety_header = {"Authorization": sheety_auth}

today =datetime.today()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%H:%M:%S")
# print(today)
# print(formatted_date)
# print(formatted_time)

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = "https://api.sheety.co/678861f7ba35a03802c4b28e8d214600/workoutTracking/workouts"

user_input = input("What exercise did you do today? ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": app_id,
    "x-app-key": api_key
}

data = {
   "query": user_input,
   "weight_kg": 52,
    "height_cm": 167,
    "age": 29,
    "gender": "male"
}

response = requests.post(url=nutrition_endpoint, headers=headers, json=data)
result = response.json()
# print(response.text)
# print(response.status_code)
print(result)

exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
print(exercise)
print(duration)
print(calories)

for activity in result["exercises"]:
    new_row = {
        "workout":{
            "date": formatted_date,
            "time": formatted_time,
            "exercise": activity["name"].title(),
            "duration": activity["duration_min"],
            "calories": activity["nf_calories"]
        }
    }
    #No Authentication
    # sheety_response = requests.post(sheety_endpoint, json=new_row)

    #Basic Authentication
    sheety_response = requests.post(sheety_endpoint, json=new_row, headers=sheety_header)
    print(sheety_response.text)
