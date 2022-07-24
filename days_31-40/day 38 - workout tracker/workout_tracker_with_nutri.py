import requests as req
from datetime import datetime

# get access data
with open("access_data.txt", "r") as file:
    APP_ID, API_KEY = file.read().split()

# nutri_food_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
nutri_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"  # post request
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "x-remote-user-id": "0",
}

# activity = input("What activity did you do: ")
activity = "swimming 4km and running 2km"
activity_params = {
    "query": activity,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 180,
    "age": 25,
}

response = req.post(url=nutri_exercise_endpoint, json=activity_params, headers=HEADERS).json()
print(response)

