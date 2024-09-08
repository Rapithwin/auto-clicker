import datetime


def read_date_time() -> list:
    """
    Read datetime from conf.txt
    """
    with open("conf.txt", "r") as f:
        file = f.read()
        file_len = len(file)
        date_time_str = file[0:-4]
        ms = file[20:file_len]
        format = r"%Y/%m/%d %H:%M:%S"
        date_time_obj = datetime.datetime.strptime(date_time_str, format)
    return date_time_obj, ms
