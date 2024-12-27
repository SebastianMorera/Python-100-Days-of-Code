import requests
from datetime import datetime
import smtplib

ISS_LOCATION_URL = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_URL = "https://api.sunrise-sunset.org/json"
MY_LATITUDE = 45.501690
MY_LONGITUDE = -73.567253
MY_EMAIL = "sebastiantestingenvironment@gmail.com"
MY_PASSWORD = "aiwy frmc vgeq tgfz"

def iss_location() -> (float, float):
    response = requests.get(url=ISS_LOCATION_URL)
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    print(f"ISS location: {iss_position}")
    return iss_position

def sunrise_sunset() -> (int ,int):
    parameters = {"lat": MY_LATITUDE, "lng": MY_LONGITUDE, "formatted": 0}
    response = requests.get(url=SUNRISE_SUNSET_URL, params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(f"Sunrise: {sunrise}h, Sunset: {sunset}h")
    return sunrise, sunset

def is_iss_overhead() -> bool:
    iss_latitude, iss_longitude = iss_location()
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True
    return False

def is_night() -> bool:
    sunrise, sunset = sunrise_sunset()
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

def iss_overhead_notifier() -> None:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="morerasebas999@gmail.com",
                                msg=f"Subject:Look up \n\nThe ISS is above you in the sky.")
            connection.close()
    else:
        print("The ISS is not above you in the sky.")

if __name__ == '__main__':
    iss_location()
    sunrise_sunset()
    iss_overhead_notifier()