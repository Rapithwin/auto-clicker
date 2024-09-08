def concat(s_unx, ms):
    """
    Takes the converted seconds since epoche and the given
    miliseconds in the conf.txt file and concatenate them
    to give miliseconds since epoche.
    Handles the zero aswell.
    """
    ms_len = len(str(ms))
    if ms_len == 3:
        return int(f"{s_unx}{ms}")
    elif ms_len == 2:
        return int(f"{s_unx}0{ms}")
    elif ms_len == 1:
        return int(f"{s_unx}00{ms}")
    else:
        print("Invalid")
