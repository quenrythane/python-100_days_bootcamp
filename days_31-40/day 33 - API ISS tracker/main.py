import requests as req

response = req.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()  # raise error on web code
print(response)
print(response.status_code)
print(response.json())

data = response.json()
position = data['iss_position']
longitude = position['longitude']
latitude = position['latitude']
iss_position = (longitude, latitude)

