import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_GET_ENDPOINT = ("https://api.sheety.co/678861f7ba35a03802c4b"
                       "28e8d214600/flightDealsForSoftway/prices")

class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._auth_header = os.environ["SHEETY_AUTH_HEADER"]
        self.headers = {"Authorization": self._auth_header}
        self.location_data = {}


    def get_location_data(self):
        response = requests.get(SHEETY_GET_ENDPOINT, headers=self.headers)
        data = response.json()
        self.location_data = data["prices"]
        return self.location_data

    def update_lowest_price(self, row_id, new_price):
        updated_price = {
            "prices": {
                "lowestPrice": new_price
            }
        }
        requests.put(f"{SHEETY_GET_ENDPOINT}/{row_id}", headers=self.headers, json=updated_price)