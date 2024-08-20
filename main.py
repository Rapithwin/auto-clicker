from funcitons.concat import concat
from exception import NegativeNumberException
import datetime
import pyautogui
import time
from funcitons.input import input_time
from ntp.ntp import current_time_ntp


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
set_date_time_unix_ms = concat(set_date_time_unix, input_list[6])

print(set_date_time)
print(set_date_time_unix_ms)



def compare_time():
    """
    Compares the time set by user and the current time from API.
    if they are equal, it will press f12
    """
    while True:
        try:
            diff_time = set_date_time_unix_ms - current_time_ntp()
            # If the date entered is in the past, raise an exception
            if diff_time < 0:
                raise NegativeNumberException
        except NegativeNumberException:
            print("Enter a valid date in the future")
            break
            
        
        print(diff_time / 1000)
        if 0 < diff_time < 150:
            
            click()
            break

        else:
            time.sleep((diff_time - 151) / 1000)


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