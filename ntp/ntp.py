import ntplib


def current_time_ntp():
    try:
        c = ntplib.NTPClient()
        response = c.request("ir.pool.ntp.org", version=3)
    except ntplib.NTPException:
        print("NTP exception")

    ms_since_epoch = int(response.tx_time * 1000)
    print(ms_since_epoch)
    print(response.delay)

    return ms_since_epoch