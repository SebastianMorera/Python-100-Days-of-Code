from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

MY_LONGITUDE = -73.5878
MY_LATITUDE = 45.5088
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def rain_alert() -> None:
    # Get environments variables
    load_dotenv()
    api_key = os.environ.get("WEATHER_API_KEY")
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    parameters_forecast = {
        "lon": MY_LONGITUDE,
        "lat": MY_LATITUDE,
        "cnt": 4,
        "appid": api_key,
    }

    response = requests.get(url=FORECAST_URL, params=parameters_forecast)
    response.raise_for_status()
    data = response.json()
    for forecast in data["list"]:
        if forecast["weather"][0]["id"] < 700:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='+16282126440',
                body="It's going to rain today. Remember to bring an ☂️",
                to='+18777804236'
            )
            print(f"It's going to rain today! The text message has been sent with status code {message.status}.")
            break


if __name__ == "__main__":
    rain_alert()
