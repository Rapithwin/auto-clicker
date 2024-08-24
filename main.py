from funcitons.concat import concat
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
)

set_date_time_unix = int(time.mktime(set_date_time.timetuple()))
set_date_time_unix_ms = concat(set_date_time_unix, input_list[6])


def compare_time():
    """
    Compares the time set by user and the current time from API.
    if they are equal, it will press f12
    """

    diff_time = set_date_time_unix_ms - current_time_ntp()
    time.sleep((diff_time + 200) / 1000)
    click()


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