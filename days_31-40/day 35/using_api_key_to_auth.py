import requests as req

with open("api_key.txt", "r") as file:
    api_key = file.read()

lat, lon = 54.361, 18.690
part = "current,minutely,daily"

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": part,
}

current_endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
one_call_endpoint = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"
# one_call_endpoint_3 = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"  # I have access to 3.0 API

response = req.get(one_call_endpoint)
response2 = req.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()


def do_take_umbrella(weather_id):
    # weather codes:  https: // openweathermap.org / weather - conditions  # Weather-Condition-Codes-2
    if weather_id < 700:
        message = "take umbrella"
    else:
        message = "no umbrella"
    return f'{hourly_weather["id"]}, {message}'


for i in range(12):
    hourly_weather = data["hourly"][i]["weather"][0]  # id, main, description, icon
    print(do_take_umbrella(hourly_weather["id"]))
