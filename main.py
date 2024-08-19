from api.time_api import get_time_keybit
from exception import NegativeNumberException
import datetime
import pyautogui
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
        try:
            diff_time = set_date_time_unix - get_time_keybit()[0]["unix"]["en"]
            if diff_time < 0:
                raise NegativeNumberException
        except NegativeNumberException:
            print("Enter a valid date in the future")
            
        
        print(diff_time)
        if diff_time <= 10:
            
            print("here")
            # now_datetime_unix2 = get_time_keybit()[0]["unix"]["en"]
            # print(now_datetime_unix2)
            if diff_time == 0:
                print("Click")
                break

        else:
            time.sleep(diff_time - 10)


def click():
    pass

compare_time()
