from datetime import datetime
from dotenv import load_dotenv
import os
import requests

PIXELA_API_URL = "https://pixe.la/v1/users"
USERNAME = "homer10simpson"
GRAPH_ID = "graph1"


def ask_user_for_date() -> datetime:
    year = int(input("Enter the year:"))
    month = int(input("Enter the month:"))
    day = int(input("Enter the day:"))
    date = datetime(year=year, month=month, day=day)
    return date


def user_creation(api_token: str) -> None:
    params = {
        "token": api_token,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=PIXELA_API_URL, json=params)
    print(response.text)


def graph_creation(api_token: str) -> None:
    headers = {
        "X-USER-TOKEN": api_token
    }

    params = {
        "id": GRAPH_ID,
        "name": "Cardio",
        "unit": "minutes",
        "type": "int",
        "color": "sora",
        "timezone": "America/Montreal",
        "startOnMonday": True,
    }

    response = requests.post(url=f"{PIXELA_API_URL}/{USERNAME}/graphs", json=params, headers=headers)
    print(response.text)


def add_graph_entry(api_token: str) -> None:
    headers = {
        "X-USER-TOKEN": api_token
    }

    date = ask_user_for_date()
    quantity = input("Enter the quantity:")
    params = {
        "date": date.strftime("%Y%m%d"),
        "quantity": quantity,
    }

    response = requests.post(url=f"{PIXELA_API_URL}/{USERNAME}/graphs/{GRAPH_ID}", json=params, headers=headers)
    print(response.text)


def update_graph_entry(api_token: str) -> None:
    headers = {
        "X-USER-TOKEN": api_token
    }

    date = ask_user_for_date()
    new_value = input("Enter the new value:")
    params = {
        "quantity": new_value,
    }

    response = requests.put(url=f"{PIXELA_API_URL}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime("%Y%m%d")}",
                            json=params, headers=headers)
    print(response.text)


def delete_graph_entry(api_token: str) -> None:
    headers = {
        "X-USER-TOKEN": api_token
    }

    date = ask_user_for_date()
    response = requests.delete(url=f"{PIXELA_API_URL}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime("%Y%m%d")}",
                               headers=headers)
    print(response.text)


def habit_tracker(api_token: str) -> None:
    create_user = input("Do you want to create a new user? (yes/no):")
    if create_user == "yes":
        user_creation(api_token)

    create_graph = input("Do you want to create a new graph? (yes/no):")
    if create_graph == "yes":
        graph_creation(api_token)

    add_entry = input("Do you want to add an entry? (yes/no):")
    if add_entry == "yes":
        add_graph_entry(api_token)

    update_entry = input("Do you want to update an entry? (yes/no):")
    if update_entry == "yes":
        update_graph_entry(api_token)

    delete_entry = input("Do you want to delete an entry? (yes/no):")
    if delete_entry == "yes":
        delete_graph_entry(api_token)


if __name__ == "__main__":
    load_dotenv()
    pixela_api_token = os.environ.get("PIXELA_API_TOKEN")
    habit_tracker(pixela_api_token)
