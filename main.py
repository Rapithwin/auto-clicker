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

time_api = get_time()

now_datetime_api = time_api["datetime"]
now_datetime_unix: int = time_api["unixtime"]
datetime_mili = f"{parser.parse(now_datetime_api)}"[0:23]

print(now_datetime_unix)


def compare_time():
    diff_time = set_date_time_unix - now_datetime_unix
    while True:
        if diff_time <= 60:
            now_datetime_unix2 = get_time()["unixtime"]
            print(now_datetime_unix2)
            if 0 <= diff_time <= 10:
                print("Click")
                break

        else:
            time.sleep(diff_time - 60)


compare_time()
