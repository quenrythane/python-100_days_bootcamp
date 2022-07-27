from access_data import AD
import requests as req

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = AD.tequila_api_key

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code
