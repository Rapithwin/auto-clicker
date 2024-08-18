from api.time_api import get_time
from dateutil import parser
import datetime
import time

from input import input_time

input_list = input_time()

set_date_time = datetime.datetime(
    year=input_list[0],
    month=input_list[1],
    day=input_list[2],
    hour=input_list[3],
    minute=input_list[4],
    second=input_list[5],
    microsecond=input_list[6] * 1000,
)

set_date_time_unix = int(time.mktime(set_date_time.timetuple()))

print(set_date_time)
print(set_date_time_unix)


now_datetime_api = get_time()["datetime"]
now_datetime_unix: int = get_time()["unixtime"]
datetime_mili = f"{parser.parse(now_datetime_api)}"[0:23]

print(now_datetime_unix)

def compare_time():
    diff_time = set_date_time_unix - now_datetime_unix
    while True:
        if (diff_time <= 60000):
            now_datetime_unix: int = get_time()["unixtime"]
            print(now_datetime_unix)
            if (0 <= diff_time <= 1000):
                print("Click")
            # time.sleep(1)
        else:
            continue

compare_time()