from api.time_api import get_time
from exception import InvalidInput
from dateutil import parser
import datetime
import time

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
            raise InvalidInput
    except Exception as e:
        print(e)
        continue

    break

while True:
    try:
        day: int = int(input("\nDay:"))
        if day <= 0 or day > 31:
            raise InvalidInput
    except Exception as e:
        print(e)
        continue

    break

while True:
    try:
        hours: int = int(input("\nHours(00:00 - 23:59):"))
        if hours < 0 or hours > 23:
            raise InvalidInput
    except Exception as e:
        print(e)
        continue

    break

while True:
    try:
        minutes: int = int(input("\nMinutes:"))
        if minutes < 0 or minutes > 60:
            raise InvalidInput
    except Exception as e:
        print(e)
        continue

    break

while True:
    try:
        seconds: int = int(input("\nSeconds:"))
        if seconds < 0 or seconds > 60:
            raise InvalidInput
    except Exception as e:
        print(e)
        continue

    break

while True:
    try:
        milliseconds: int = int(input("\nMilliseconds:"))
        if milliseconds < 0 or milliseconds > 999:
            raise InvalidInput
    except Exception as e:
        print(e)
        continue

    break


date_time = datetime.datetime(
    year=year,
    month=month,
    day=day,
    hour=hours,
    minute=minutes,
    second=seconds,
    microsecond=milliseconds * 1000,
)


print(int(time.mktime(date_time.timetuple())))


datetime_api = get_time()["datetime"]
datetime_unix: int = get_time()["unixtime"]
datetime_mili = f"{parser.parse(datetime_api)}"[0:23]

print(datetime_unix)
