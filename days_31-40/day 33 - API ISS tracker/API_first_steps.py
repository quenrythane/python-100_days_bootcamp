import requests as req

# https://www.latlong.net/Show-Latitude-Longitude.html
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

response = req.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()  # raise error on web code
print(response)
print(response.status_code)
print(response.json())

data = response.json()
position = data['iss_position']
latitude = position['latitude']
longitude = position['longitude']
iss_position = (longitude, latitude)
