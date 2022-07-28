from datetime import datetime, timedelta
from notification_manager import NotificationManager

from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

ORIGIN_CITY_IATA = "WAW"

# create DataManager object and get data(rows) from Sheety
Sheety = DataManager()
sheet_data = Sheety.get_destination_data()
print(sheet_data)

# create FlightSearch object and fill empty IATA codes with codes from FlightSearch API
FlightSearch = FlightSearch()
for row in sheet_data:
    if row["iataCode"] == "" or row["iataCode"] == "TESTING":
        row["iataCode"] = FlightSearch.get_destination_code(row["city"])
        Sheety.destination_data = sheet_data
Sheety.update_destination_codes()

# find price
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

notification_manager = NotificationManager()
for destination in sheet_data:
    flight = FlightSearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
        # do i want to update lowest price? <- i don't think so
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
