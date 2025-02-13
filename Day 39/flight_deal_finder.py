import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "YMQ"

if __name__ == '__main__':
    data_manager = DataManager()
    flight_search = FlightSearch()

    if not any(item.get('iataCode') for item in data_manager.sheet_data):
        for item in data_manager.sheet_data:
            iata_code = flight_search.get_destination_code(item["city"])
            item["iataCode"] = iata_code
        data_manager.update_iata_code_data()

    for destination in data_manager.sheet_data:
        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=(dt.datetime.now() + dt.timedelta(days=1)).strftime("%Y-%m-%d"),
            to_time=(dt.datetime.now() + dt.timedelta(days=30*6)).strftime("%Y-%m-%d")
        )
        cheapest_flight = find_cheapest_flight(flights)
        if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
            print(f"{destination['city']}: ${cheapest_flight.price}")
            notification_manager = NotificationManager()
            notification_manager.send_sms(
                message_body=f"Low price alert! Only ${cheapest_flight.price} to fly "
                             f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                             f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )