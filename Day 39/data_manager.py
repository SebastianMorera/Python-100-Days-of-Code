from dotenv import load_dotenv
import os
import requests

load_dotenv()

SHEETY_API_URL = "https://api.sheety.co/9921eea2d7359459e2eabcb56ffe3231/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.token = os.environ.get("BEARER_TOKEN_SHEETY_API")
        self.header = {"Authorization": f"Bearer {self.token}"}
        self.sheet_data = self.get_destination_data()

    def get_destination_data(self):
        try:
            response = requests.get(url=SHEETY_API_URL, headers=self.header)
            response.raise_for_status()
            return response.json()["prices"]
        except requests.exceptions.RequestException as e:
            print(f"Request to Sheety API failed: {e}")


    def update_iata_code_data(self) -> None:
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEETY_API_URL}/{city['id']}", json=new_data, headers=self.header)
            response.raise_for_status()

    def post_data(self, data):
        response = requests.post(url=SHEETY_API_URL, json=data, headers={"Authorization": f"Bearer {self.token}"})
        response.raise_for_status()
        return response
