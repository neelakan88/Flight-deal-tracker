import requests
import pprint
from datetime import datetime, timedelta


SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0ff510926666f566c8437a980d29d386/flightDeals/prices"
MY_HEADERS = {
            "Authorization" : "Basic bnVsbDpudWxs",
            }


TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"
TEQUILA_API_KEY = "NwCVp80QooX_AYmKSKIg3S2HvH9GGiUD"

now = datetime.now()
delta = timedelta(days=180)
future_date = now + delta
formatted_future_date = future_date.strftime("%d/%m/%Y")
# print(formatted_date)
now_date = now.strftime("%d/%m/%Y")


class FlightData:
    def search_flights(self, city_code, price_to):
    
        my_headers = {

            "apikey" : TEQUILA_API_KEY,
            
        }

        tequila_params = {

            "fly_from" : "SFO",
            "fly_to" : city_code, # ---------- need to figure out this variable
            "date_from" : now_date,
            "date_to" : formatted_future_date,
            "nights_in_dst_from" : 7, #minimum length of stay is 7 days
            "nights_in_dst_to" : 28, #max length of stay 28 days
            "adults" : 1, # 1 adult
            "price_from" : 1, #minimum price
            "price_to" : price_to, #--------------- need to figure out this variable
            "max_stopovers" : 0, #direct flights only
            "limit" : 1,
            "curr" : "USD",

            }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params = tequila_params, headers = my_headers)
        response.raise_for_status()
        data = response.json()
        return data      
        # print(data)

        #This class is responsible for structuring the flight data.
        