import requests as req


pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "ndgalbdkg348buiadu2b8bf28bafb9u2f",
    "username": "quenry-thane",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

resposne = req.post(url=pixela_endpoint, json=user_params)
print(resposne.text)
