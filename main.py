from api.time_api import get_time_keybit, get_time_worldtime
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


time_api = get_time_keybit()
now_datetime_unix = time_api[0]["unix"]["en"]


print(now_datetime_unix)


def compare_time():
    
    while True:
        diff_time = set_date_time_unix - get_time_keybit()[0]["unix"]["en"]
        print(diff_time)
        if diff_time <= 30:
            print("here")
            now_datetime_unix2 = get_time_keybit()[0]["unix"]["en"]
            print(now_datetime_unix2)
            if 0 <= diff_time <= 1:
                print("Click")
                break

        else:
            time.sleep(diff_time - 30)


compare_time()
