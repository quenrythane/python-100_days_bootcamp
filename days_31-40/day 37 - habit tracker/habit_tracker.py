import requests as req
from datetime import datetime

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

pixel_params = {
    "date": input_date,
    "quantity": "120",
}

resposne = req.post(url=f"{graph1_endpoint}/{GRAPH_ID}", json=pixel_params, headers=request_header)
print(resposne.text, '\n')  # check for the response (and hipotetical errors/failures)
