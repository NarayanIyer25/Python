#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import  FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
flight_data = FlightData()
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = flight_data.return_data()
pprint(sheet_data)

for i in sheet_data:
    if i['iataCode'] != '':
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")
        flight_data.check_price(destination_code=i['iatacode'],departure_city=i['city'],price=i['lowest price'])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()