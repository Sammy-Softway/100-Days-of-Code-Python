import os
from twilio.rest import Client

TWILIO_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")
TWILIO_WHATSAPP_RECEPIENT = os.environ.get("TWILIO_WHATSAPP_RECEPIENT")

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ["TWILIO_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.client = Client(self.account_sid, self.auth_token)

    def text_message(self, price, departure_airport, arrival_airport, departure_date, arrival_date):
        message = self.client.messages.create(
            body=f"Low price alert! Only £{price} to fly from {departure_airport} "
                 f"to {arrival_airport} on {departure_date} until {arrival_date}",
            from_=TWILIO_NUMBER,
            to=VERIFIED_NUMBER,
        )

    def whatsapp_message(self, price, departure_airport, arrival_airport, departure_date, arrival_date):
        message = self.client.messages.create(
            body=f"Low price alert! Only £{price} to fly from {departure_airport} "
                 f"to {arrival_airport} on {departure_date} until {arrival_date}",
            from_=TWILIO_WHATSAPP_NUMBER,
            to=TWILIO_WHATSAPP_RECEPIENT,
        )


    # whatsapp_message(price=250, departure_airport="Lagos", arrival_airport="London",
    #              departure_date="06/08/2026", arrival_date="26/08/2026")
    # text_message(price=250, departure_airport="Lagos", arrival_airport="London",
    #              departure_date="06/08/2026", arrival_date="26/08/2026")