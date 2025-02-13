from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):
        self.api_key = os.environ.get("AMADEUS_API_KEY")
        self.api_secret = os.environ.get("AMADEUS_API_SECRET")
        self.token = self._get_new_token()
        self.header_token = {"Authorization": f"Bearer {self.token}"}

    def _get_new_token(self) -> str:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, data=params, headers=headers)
        return response.json()["access_token"]

    def get_destination_code(self, city_name) -> str:
        params = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        response = requests.get(url=IATA_ENDPOINT, params=params, headers=self.header_token)

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time,
            "returnDate": to_time,
            "adults": 1,
            "currencyCode": "CAD",
            "max": 5
        }

        response = requests.get(url=FLIGHT_ENDPOINT, params=params, headers=self.header_token)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.")
            print("Response body:", response.text)
            return None

        return response.json()