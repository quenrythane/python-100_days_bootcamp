from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

Sheety = DataManager()
sheet_data = Sheety.get_destination_data()
print(sheet_data)

FlightSearch = FlightSearch()
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = FlightSearch.get_destination_code(row["city"])
        Sheety.destination_data = sheet_data
Sheety.update_destination_codes()







