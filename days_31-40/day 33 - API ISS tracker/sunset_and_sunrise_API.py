import requests as req
from datetime import datetime

latitude, longitude = 54.352024, 18.646639

parameters = {
    'lat': latitude,
    'lng': longitude,
    'formatted': 0,
}

# https://sunrise-sunset.org/api
# endpoint ? param name = value & next param name = value
response = req.get('https://api.sunrise-sunset.org/json?', params=parameters)
response.raise_for_status()
data = response.json()

time_now = datetime.now()
sunrise = data['results']['sunrise'].split("T")[1].split("+")[0]
sunset = data['results']['sunset'].split("T")[1].split("+")[0]
print(sunrise, sunset)

time_now_hour = time_now.hour
sunrise_hour = sunrise.split(":")[0]
sunset_hour = sunset[0].split(":")[0]

