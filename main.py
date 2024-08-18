from api.time_api import get_time
from dateutil import parser
import datetime
import time

from input import input_time

input_list = input_time()

date_time = datetime.datetime(
    year=input_list[0],
    month=input_list[1],
    day=input_list[2],
    hour=input_list[3],
    minute=input_list[4],
    second=input_list[5],
    microsecond=input_list[6] * 1000,
)

print(date_time)
print(int(time.mktime(date_time.timetuple())))


datetime_api = get_time()["datetime"]
datetime_unix: int = get_time()["unixtime"]
datetime_mili = f"{parser.parse(datetime_api)}"[0:23]

print(datetime_unix)
