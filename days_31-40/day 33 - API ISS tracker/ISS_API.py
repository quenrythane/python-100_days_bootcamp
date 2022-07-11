import requests as req
from datetime import datetime
import ssl
import smtplib
import time


# https://www.latlong.net/Show-Latitude-Longitude.html
# http://open-notify.org/Open-Notify-API/iss-Location-Now/

# my position
my_latitude, my_longitude = 54.352024, 18.646639


def is_iss_overhead():
    response = req.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()  # raise error on web code
    iss_data = response.json()
    
    # iss position
    position = iss_data['iss_position']
    iss_latitude = float(position['latitude'])
    iss_longitude = float(position['longitude'])
    print(f"ISS position: {iss_latitude}, {iss_longitude}\n"
          f"My position: {my_latitude}, {my_longitude}\n")
    if my_latitude - 5 <= iss_latitude <= my_latitude + 5 and my_longitude - 5 <= iss_longitude <= my_longitude + 5:
        return True


def is_night():
    # https://sunrise-sunset.org/api
    parameters = {
        'lat': my_latitude,
        'lng': my_longitude,
        'formatted': 0,
    }
    response = req.get('https://api.sunrise-sunset.org/json?', params=parameters)
    response.raise_for_status()
    my_data = response.json()

    sunrise = my_data['results']['sunrise'].split("T")[1].split("+")[0]
    sunset = my_data['results']['sunset'].split("T")[1].split("+")[0]

    sunrise_hour = int(sunrise.split(":")[0])
    sunset_hour = int(sunset[0].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True


def send_email():
    # get access data
    with open("../access_data.txt", "r") as file:
        access_data = [line.split(": ") for line in file.read().splitlines()]
        sender = access_data[0][1]
        password = access_data[2][1]  # app password

    # create a secure SSL context and send email
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ssl_context) as smtp_connection:
        smtp_connection.login(user=sender, password=password)
        smtp_connection.sendmail(from_addr=sender,
                                 to_addrs="artur.babinski.g@gmail.com",
                                 msg=f"Subject:Look Up!\n\nThe ISS is overhead!")
    print("Email sent!")


# main program
while True:
    time.sleep(300) # check every 5 minutes
    if is_iss_overhead() and is_night():
        send_email()
