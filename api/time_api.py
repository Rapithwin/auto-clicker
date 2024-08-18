import requests
from exception import RequestFailException


def get_time_worldtime() -> list:

    try:
        response = requests.get(
            "http://worldtimeapi.org/api/timezone/Asia/Tehran", timeout=1
        )

        print("OK")
        return response.json(), True
    except requests.exceptions.RequestException or requests.exceptions.Timeout as e:
        # print(response.status_code)
        print(e)
        return response.status_code, False


def get_time_keybit() -> list:
    try:
        response = requests.get("https://api.keybit.ir/time", timeout=1)

        print("OK")
        return response.json(), True
    except requests.exceptions.RequestException or requests.exceptions.Timeout as e:
        # print(response.status_code)
        print(e)
        return response.status_code, False
