from funcitons.concat import concat
from funcitons.read_file import read_date_time
import pyautogui
import time
import threading
from ntp.ntp import current_time_ntp


set_date_time = read_date_time()[0]
ms = read_date_time()[1]
set_date_time_unix = int(time.mktime(set_date_time.timetuple()))
set_date_time_unix_ms = concat(set_date_time_unix, ms)


def compare_time():
    """
    Compares the time set by user and the current time from time server.
    If they are equal, it will call the click() function.
    """
    print("Running...\n")
    diff_time = set_date_time_unix_ms - current_time_ntp()
    if diff_time <= 0:
        print("Error: Enter a valid date and time in future")
    timer = threading.Timer(diff_time / 1000, click)
    timer.start()
    # So the terminal doesn't close automaticly # So the terminal doesn't close automaticly


def click():
    """
    Presses f12 or locates the button on the screen and clicks on it.
    """
    try:
        pyautogui.press("f12")
    except Exception as e:
        print(e)
        button_location = pyautogui.locateOnScreen("assets/button.png")
        pyautogui.click(button_location)
    input("Press enter to continue...")


def main():
    compare_time()


if __name__ == "__main__":
    main()
