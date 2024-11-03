import ntplib


def current_time_ntp():
    """
    Get the current IR time from time server
    """
    c = ntplib.NTPClient()
    try:
        response = c.request("0.pool.ntp.org", version=3)
    except Exception:
        print("ir server didn't respond, trying asia...")
        response = c.request("0.asia.pool.ntp.org", version=3)

    ms_since_epoch = int(response.tx_time * 1000)

    return ms_since_epoch
