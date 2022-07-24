import requests as req
from datetime import datetime

with open("access_data_2.txt", "r") as file:
    username, project_name, sheet_name = file.read().split()

sheety_endpoint = "https://api.sheety.co"
sheety_endpoint_complete = f"{sheety_endpoint}/{username}/{project_name}/{sheet_name}"

# generate new row
response_get = req.get(f"{sheety_endpoint_complete}/2")
print(response_get.json())
