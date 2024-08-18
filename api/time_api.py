import requests
from exception import RequestFailException


def get_time_worldtime():
    response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Tehran")

    if response.status_code == 200:
        print("OK")
        return response.json()
    else:
        print(response.status_code)
        print(response.reason)
        raise RequestFailException


def get_time_keybit():
    response = requests.get("https://api.keybit.ir/time")

    if response.status_code == 200:
        print("OK")
        return response.json()
    else:
        print(response.status_code)
        print(response.reason)
        raise RequestFailException
