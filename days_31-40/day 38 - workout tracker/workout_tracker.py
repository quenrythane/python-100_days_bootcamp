import requests as req
from datetime import datetime

# get access data
GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 25
with open("access_data_3.txt", "r") as file:
    APP_ID, API_KEY, username, project_name, sheet_name = file.read().split()

## NUTRI
# nutri_food_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
nutri_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"  # post request
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# activity = input("What activity did you do: ")
activity = "swimming 4km and running 2km"
activity_params = {
    "query": activity,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutri_response = req.post(url=nutri_exercise_endpoint, json=activity_params, headers=HEADERS).json()

## SHEETY
sheety_endpoint = "https://api.sheety.co"
sheety_endpoint_complete = f"{sheety_endpoint}/{username}/{project_name}/{sheet_name}"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for activity in nutri_response["exercises"]:
    sheet_name_post = {
        sheet_name[:-1]: {
            "date": today_date,
            "time": now_time,
            "exercise": activity["name"],
            "duration": activity["duration_min"],
            "calories": activity["nf_calories"],
        }
    }

    sheety_response = req.post(url=sheety_endpoint_complete, json=sheet_name_post)
    print(f"POST: {sheety_response.json()['workout']}")

