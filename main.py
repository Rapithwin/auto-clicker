from funcitons.concat import concat
from funcitons.read_file import read_date_time
import pyautogui
import time
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
    try:
        time.sleep((diff_time) / 1000)
    except:
        print("Error: Enter a valid date and time in future")
    click()
    input(
        "\nPress enter to continue."
    )  # Preventing terminal from closing automatically


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


def main():
    compare_time()


if __name__ == "__main__":
    main()
