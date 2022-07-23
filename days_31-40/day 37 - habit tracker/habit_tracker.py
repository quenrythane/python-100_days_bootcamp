import requests as req

USERNAME = "quenry-thane"
TOKEN = "ndgalbdkg348buiadu2b8bf28bafb9u2f"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CREATE ACCOUNT and get response of successful creation
resposne = req.post(url=pixela_endpoint, json=user_params)
print(resposne.text, '\n')  # check for the response (and hipotetical errors/failures)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_header = {
    "X-USER-TOKEN": TOKEN,
}
graph_params = {
    "id": "graph1",
    "name": "programming",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

# CREATE GRAPH, get response of successful creation and link to view the graph
resposne = req.post(url=graph_endpoint, json=graph_params, headers=graph_header)
print(resposne.text)  # check for the response (and hipotetical errors/failures)
link_to_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}.html"
print(link_to_graph, '\n')

# POST VALUE to the graph


