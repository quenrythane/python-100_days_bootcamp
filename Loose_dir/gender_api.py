import requests as req
name = "Artur"

url = f"https://api.genderize.io?name={name}"
response = req.get(url)
gender = response.json()["gender"]

print(gender)
