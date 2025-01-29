import datetime as dt
import os
import requests
from dotenv import load_dotenv

NUTRITIONIX_API_URL = "https://trackapi.nutritionix.com"
SHEETY_API_URL = "https://api.sheety.co/9921eea2d7359459e2eabcb56ffe3231/workoutTracker/workouts"


def ask_user_exercise_information() -> (str, str, int, int, int):
    description = str(input("The exercise description? "))
    gender = str(input("Your gender? "))
    weight_kg = int(input("Your weight in kg? "))
    height_cm = int(input("Your height in cm? "))
    age = int(input("Your age? "))
    return description, gender, weight_kg, height_cm, age


def get_nutritionix_exercises(app_id: str, app_key: str) -> (str, int, int):
    if app_id is None or app_key is None:
        raise ValueError("App ID and App Key must not be None")

    headers = {
        "x-app-id": app_id,
        "x-app-key": app_key
    }

    description, gender, weight, height, age = ask_user_exercise_information()
    nutri_params = {
        "query": description,
        "gender": gender,
        "weight_kg": weight,
        "height_cm": height,
        "age": age
    }

    response = requests.post(url=f"{NUTRITIONIX_API_URL}/v2/natural/exercise", json=nutri_params, headers=headers)
    response_json = response.json()
    exercises = response_json.get("exercises")
    if exercises is None:
        raise ValueError("Nutritionix API response does not contain 'exercises' key")

    exercise = exercises[0]
    user_input = exercise.get("user_input")
    duration_min = exercise.get("duration_min")
    nf_calories = exercise.get("nf_calories")

    if user_input is None or duration_min is None or nf_calories is None:
        raise ValueError("Nutritionix API response is missing required fields")

    return user_input, duration_min, nf_calories


def add_exercise(app_id: str, app_key: str, token: str) -> None:
    if app_id is None or app_key is None:
        raise ValueError("App ID and App Key must not be None")

    exercise, duration, calories = get_nutritionix_exercises(app_id, app_key)
    if exercise is None or duration is None or calories is None:
        raise ValueError("Nutritionix API response is missing required fields")

    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%X")

    google_sheets_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.post(url=SHEETY_API_URL, json=google_sheets_params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request to Sheety API failed: {e}")


if __name__ == '__main__':
    load_dotenv()
    application_id = os.environ.get("NUTRITIONIX_API_APPLICATION_ID")
    application_key = os.environ.get("NUTRITIONIX_API_APPLICATION_KEY")
    sheety_token = os.environ.get("BEARER_TOKEN_SHEETY_API")
    add_exercise(application_id, application_key, sheety_token)
