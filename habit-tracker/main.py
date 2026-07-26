import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"

today = datetime.now()
specified_day = datetime(year=2021, month=3, day=12)
back_dated = specified_day.strftime("%Y%m%d")
print(specified_day.strftime("%Y-%m-%d"))
# formatted_date = today.strftime("%Y-%m-%d")
formatted_date = today.strftime("%Y%m%d")
print(formatted_date)

pixela_endpoint = "https://pixe.la/v1/users"

user_data = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_data)
# print(response.text)

# graph_endpoint = "https://pixe.la/v1/users/softway/graphs"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_data = {
    "id": GRAPH_ID,
    "name": "Jogging Graph",
    "unit": "miles",
    "type": "float",
    "color":"shibafu"
}

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_data)
# print(response.text)

post_value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

requested_data = {
    "date": formatted_date,
    "quantity": input("How many miles did you jog today? "),
}

response = requests.post(url=post_value_endpoint, json=requested_data, headers=headers)
print(response.text)

update_value_endpoint = f"{post_value_endpoint}/{formatted_date}"

updated_value_data = {
    "quantity": "9.55"
}

# response = requests.put(url=update_value_endpoint, headers=headers, json=updated_value1_data)
# print(response.text)

to_be_deleted_endpoint = f"{post_value_endpoint}/{back_dated}"

# response = requests.delete(url=to_be_deleted_endpoint, headers=headers)
# print(response.text)