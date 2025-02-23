from dotenv import load_dotenv
import os
import requests

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9921eea2d7359459e2eabcb56ffe3231/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/9921eea2d7359459e2eabcb56ffe3231/flightDeals/users"

class DataManager:
    def __init__(self):
        self.token = os.environ.get("BEARER_TOKEN_SHEETY_API")
        self.header = {"Authorization": f"Bearer {self.token}"}
        self.sheet_data = self.get_destination_data()
        self.customer_data = self.get_customer_emails()

    def get_destination_data(self):
        try:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.header)
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

            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=self.header)
            response.raise_for_status()

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.header)
        data = response.json()
        # pprint(data)  # See how Sheet data is formatted so that you use the correct column name!
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data
