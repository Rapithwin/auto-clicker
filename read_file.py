import datetime


def read_date_time() -> list:
    with open("conf.txt", "r") as f:
        file = f.read()
        date_time_str = file[0:-4]
        ms = file[20:25]
        format = r"%Y/%m/%d %H:%M:%S"
        date_time_obj = datetime.datetime.strptime(date_time_str, format)
    return date_time_obj, ms