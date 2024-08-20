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
   # microsecond=input_list[6] * 1000,
)

set_date_time_unix = int(time.mktime(set_date_time.timetuple()))

print(set_date_time)
print(set_date_time_unix)



time_api = get_time_keybit()
now_datetime_unix = time_api[0]["unix"]["en"]


print(now_datetime_unix)


def compare_time():
    counter = 0
    """
    Compares the time set by user and the current time from API.
    if they are equal, it will press f12
    """
    while True:
        try:
            diff_time = set_date_time_unix - get_time_keybit()[0]["unix"]["en"]
            # If the date entered is in the past, raise an exception
            if diff_time < 0:
                raise NegativeNumberException
        except NegativeNumberException:
            print("Enter a valid date in the future")
            break
            
        
        print(diff_time)
        counter +=1
        if diff_time == 1:
            time.sleep((1000 + input_list[6]) / 1000)
            click()
            break

        else:
            time.sleep(diff_time - 1)


    print(f"counter: {counter}")

def click():
    """
    Pressing f12 using pyautogui
    """
    
    try:
        pyautogui.press("f12")
    except Exception as e:
        print(e)
        button_location = pyautogui.locateOnScreen("assets/button.png")
        pyautogui.click(button_location)


def main():
    compare_time()


if __name__ == "__main__":
    main()