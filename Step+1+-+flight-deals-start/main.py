import requests_cache
from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# ==================== Conserve requests and preserve your free plan ====================
# requests_cache.install_cache(
#     "flight_cache",
#     urls_expire_after={
#         "*.sheety.co*": requests_cache.DO_NOT_CACHE,
#         "*": 3600,
#     }
# )
requests_cache.install_cache(
    'flight_cache',
    backend='sqlite',
    expire_after=3600 * 168,
    ignorable_urls=['https://sheety.co']
)

# ==================== Set the Dates ====================
today = datetime.today()
# print(today)
tomorrow = today + timedelta(days=1)
six_month_from_today = today + timedelta(days=30 * 6)
# print(six_month_from_today.date())

# today_formatted = today.strftime('%Y-%m-%d')
# six_month_from_today_formatted = six_month_from_today.strftime('%Y-%m-%d')
today_formatted = today.date()
tomorrow_formatted = tomorrow.date()
six_month_from_today_formatted = six_month_from_today.date()

# ==================== Talk to Sheety ====================
data_manager = DataManager()
sheet_data = data_manager.get_location_data()
pprint(sheet_data)

# # ==================== Do a Flight Search ====================
# flight_search = FlightSearch()
#
# flight_details = flight_search.check_flights(
#     origin_city_code="LOS",
#     destination_city_code="CDG",
#     departure_date="2026-08-03",
#     return_date="2026-08-04"
# )
# # pprint(flight_details)
#
# # ==================== Show the Cheapest Flight ====================
# cheapest_flight = find_cheapest_flight(flight_details, six_month_from_today_formatted)
# pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")
#
# if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]["lowestPrice"]:
#     pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
#     data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price)

# ==================== Search all the destinations ====================

# My origin airport (MMA Lagos)
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LOS"

for rows in sheet_data:
    flight_details = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=rows["iataCode"],
        departure_date=tomorrow_formatted,
        return_date=six_month_from_today_formatted
    )

    # ==================== Show the Cheapest Flight ====================
    cheapest_flight = find_cheapest_flight(flight_details, six_month_from_today_formatted)
    pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]["lowestPrice"]:
        pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
        data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price)

        # ==================== Notification Manager ====================
        notification_manager = NotificationManager()
        notification_manager.whatsapp_message(
            price=cheapest_flight.price,
            departure_airport=ORIGIN_CITY_IATA,
            arrival_airport=rows["iataCode"],
            departure_date=tomorrow_formatted,
            arrival_date=six_month_from_today_formatted,
        )



# notification_manager = NotificationManager()
# notification_manager.whatsapp_message(
#     price=250,
#     departure_airport="MMA Lagos",
#     arrival_airport="Heatrow, London",
#     departure_date=tomorrow_formatted,
#     arrival_date=six_month_from_today_formatted,
# )