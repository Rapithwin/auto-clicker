import datetime
from api.time_api import get_time_worldtime
from dateutil import parser

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


date_time = get_time_worldtime()[0]["datetime"][0:23]
parsed_time = parser.parse(date_time)

print(set_date_time == parsed_time)