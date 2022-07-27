import requests as req
from access_data import AD

# https://api.sheety.co/username/projectName/emails
sheety_endpoint = "https://api.sheety.co"
sheety_endpoint_complete = f"{sheety_endpoint}/{AD.sheety_username}/{AD.sheety_project_name}/{AD.sheet_name}"
# the way how we autorize
header = {"Authorization": f"Bearer {AD.bearer_headers}"}


#This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # GET
        response = req.get(url=sheety_endpoint_complete, headers=header)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    # POST
    """
    parameters = {
        f"{sheet_name[:-1]}": {
            "city": ,  # str
            "iataCode": ,  # str
            "lowestPrice": ,  # float
        }
    }
    """
    """
    print(response)
    print(response.json()["prices"][0]["lowestPrice"])
    print(type(response.json()["prices"][0]["lowestPrice"]))
    """
