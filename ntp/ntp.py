import ntplib


def current_time_ntp():
    c = ntplib.NTPClient()
    try:
        response = c.request("ir.pool.ntp.org", version=3)
    except Exception as e:
        print(e)
        response = c.request("2.asia.pool.ntp.org", version=3)

    ms_since_epoch = int(response.tx_time * 1000)

    return ms_since_epoch