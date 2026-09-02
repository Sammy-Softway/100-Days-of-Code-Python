import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPAPI_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, departure_date, return_date):
        serpapi_params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": departure_date,
            "return_date": return_date,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
        }

        response = requests.get(SERPAPI_ENDPOINT, params=serpapi_params)

        if response.status_code != 200:
            print(f"Response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data