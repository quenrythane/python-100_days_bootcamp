import requests as req
from datetime import datetime

with open("access_data_2.txt", "r") as file:
    username, project_name, sheet_name = file.read().split()

sheet_name_post = {
    sheet_name[:-1]: {
        "date": "21/07/2022",
        "time": "12:00",
        "exercise": "Swimming",
        "duration": "4km",
        "calories": "100",
}}

sheety_endpoint = "https://api.sheety.co"
sheety_endpoint_complete = f"{sheety_endpoint}/{username}/{project_name}/{sheet_name}"

# GET
row_number = 2
response_get = req.get(f"{sheety_endpoint_complete}/{row_number}")
print(response_get.json())
print(response_get.text)

# POST
# generate new row
response_post = req.post(url=sheety_endpoint_complete, json=sheet_name_post)
print(response_post.json())
