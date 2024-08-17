import requests


def get_time():
    response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Tehran")

    if response.status_code == 200:
        return response.json()
