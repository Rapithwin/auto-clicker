
from exception import InvalidInputException


def input_time() -> list:
    while True:
        try:
            year: int = int(input("\nYear:"))

        except Exception as e:
            print(e)
            continue
        break

    while True:
        try:
            month: int = int(input("\nMonth:"))
            if month <= 0 or month > 12:
                raise InvalidInputException
        except Exception as e:
            print(e)
            continue

        break

    while True:
        try:
            day: int = int(input("\nDay:"))
            if day <= 0 or day > 31:
                raise InvalidInputException
        except Exception as e:
            print(e)
            continue

        break

    while True:
        try:
            hours: int = int(input("\nHour(00 - 23):"))
            if hours < 0 or hours > 23:
                raise InvalidInputException
        except Exception as e:
            print(e)
            continue

        break

    while True:
        try:
            minutes: int = int(input("\nMinute:"))
            if minutes < 0 or minutes > 60:
                raise InvalidInputException
        except Exception as e:
            print(e)
            continue

        break

    while True:
        try:
            seconds: int = int(input("\nSecond:"))
            if seconds < 0 or seconds > 60:
                raise InvalidInputException
        except Exception as e:
            print(e)
            continue

        break

    while True:
        try:
            milliseconds: int = int(input("\nMillisecond:"))
            if milliseconds < 0 or milliseconds > 999:
                raise InvalidInputException
        except Exception as e:
            print(e)
            continue

        break

    return year, month, day, hours, minutes, seconds, milliseconds
