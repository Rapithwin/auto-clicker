import datetime
import time
from api.time_api import get_time_worldtime
from dateutil import parser

from input import input_time


# Now
date_time = get_time_worldtime()[0]["datetime"][0:23]
parsed_time = parser.parse(date_time)

# parsed_time = parser.parse(date_time)
# unixtime_ms = round(time.mktime(parsed_time.timetuple()) * 1000 + int(str(parsed_time)[20:23]))

# Set
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


def convert_to_unx(date_time):
    print(time.mktime(date_time.timetuple()))
    unixtime_ms = round(time.mktime(date_time.timetuple()) * 1000 + int(str(date_time)[20:23]))
    return unixtime_ms


print(convert_to_unx(parsed_time))
print(convert_to_unx(set_date_time))
# print(parsed_time)
# print(unixtime_ms)
# print(int(str(parsed_time)[20:23]))

print(convert_to_unx)