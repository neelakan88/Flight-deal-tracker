# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
import pprint
from datetime import datetime, timedelta


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for i in range(len(sheet_data)):
    from flight_data import FlightData
    raw_flight_data = FlightData()
    flight_data = raw_flight_data.search_flights(city_code = sheet_data[i]['iataCode'], price_to = sheet_data[i]['lowestPrice'])
    # if flight_data['data'][0] == None or flight_data['data'] == None:
    #     pass
    # else:
    try:
        city = flight_data["data"][0]["cityTo"]
        currency = flight_data["currency"]
        cost = flight_data["data"][0]["price"]
        date_of_departure = flight_data["data"][0]["local_departure"]
        # parse the ISO 8601 date strings
        departure_datetime = datetime.fromisoformat(date_of_departure.replace('Z', '+00:00'))
        # Format the datetime object into a human-readable string
        readable_departure = departure_datetime.strftime('%Y-%m-%d at %I:%M%p')

        # Calculate the return date based on departure and nights stayed
        date_of_return = flight_data["data"][0]["nightsInDest"]
        return_datetime = departure_datetime + timedelta(days=int(date_of_return))
        readable_return = return_datetime.strftime('%Y-%m-%d')



        print(f"{city}: ${cost}{currency}, leaving on {readable_departure} for {date_of_return} days, returning on {readable_return}.")
        message_body = f"{city}: ${cost}{currency}, leaving on {readable_departure} for {date_of_return} days, returning on {readable_return}."
        from notification_manager import NotificationManager
        notification_manager = NotificationManager()
        notification_manager.send_sms(message_body = message_body)

    except IndexError:
        pass



    

