import requests as req
from datetime import datetime, timedelta

# my account: https://pixe.la/@quenry-thane
USERNAME = "quenry-thane"
TOKEN = "ndgalbdkg348buiadu2b8bf28bafb9u2f"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph1_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
request_header = {
    "X-USER-TOKEN": TOKEN,
}

# CREATE ACCOUNT and get response of successful creation
"""
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

resposne = req.post(url=pixela_endpoint, json=user_params)
print(resposne.text, '\n')  # check for the response (and hipotetical errors/failures)
"""

# CREATE GRAPH, get response of successful creation and link to view the graph
"""
graph1_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
request_header = {
    "X-USER-TOKEN": TOKEN,
}
graph_params = {
    "id": GRAPH_ID,
    "name": "programming",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

resposne = req.post(url=graph1_endpoint, json=graph_params, headers=request_header)
print(resposne.text)  # check for the response (and hipotetical errors/failures)
link_to_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}.html"
print(link_to_graph, '\n')
"""

# POST VALUE to the graph
today = datetime.now()
input_date = today.strftime("%Y%m%d")
# input_date = "20220722"

# quantity_input = input("What number of minutes did you spend on programming today?: ")
quantity_input = str(20)
pixel_params = {
    "date": input_date,
    "quantity": quantity_input,
}

resposne = req.post(url=f"{graph1_endpoint}/{GRAPH_ID}", json=pixel_params, headers=request_header)
print(resposne.text)  # check for the response (and hipotetical errors/failures)
print(f"{graph1_endpoint}/{GRAPH_ID}.html", '\n')

# GET WEEKLY VALUES
def week_interval(date: tuple):
    today = datetime(date[0], date[1], date[2])
    start_week = datetime(today.year, today.month, today.day - (today.isoweekday() - 1))
    end_week = start_week + timedelta(days=6)
    return start_week.strftime("%Y%m%d"), end_week.strftime("%Y%m%d")

from_period, to_period = week_interval(date=(2022, 7, 24))
get_endpoint = f"{graph1_endpoint}/{GRAPH_ID}/pixels"
pixels_params ={
    "from": from_period,
    "to": to_period,
    "withBody": "true",
}

resposne = req.get(url=get_endpoint, params=pixels_params, headers=request_header)
# print(resposne.text)  # check for the response (and hipotetical errors/failures)

pixels_sum = sum(int(pixel["quantity"]) for pixel in resposne.json()["pixels"])
print(f"You have spent {pixels_sum} minutes on programming this week ({from_period}-{to_period}).")



