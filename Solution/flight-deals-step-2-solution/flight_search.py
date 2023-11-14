import requests
import pprint
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"
TEQUILA_API_KEY = "NwCVp80QooX_AYmKSKIg3S2HvH9GGiUD"

class FlightSearch:

    def get_destination_code(self, city_name):
        
        my_headers = {
            "apikey" : TEQUILA_API_KEY,
        }
        
        tequila_params = {
            
            "term" : city_name,
            "location_types" : "city",
            "limit" : 1,
            "locale" : "en-US"

        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}locations/query", params = tequila_params, headers = my_headers)
        response.raise_for_status()
        data = response.json()['locations']
        code = data[0]['code']
        return code
    

        
        # return self.iata_code
        
    
