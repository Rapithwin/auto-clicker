import ntplib


def current_time_ntp():
    """
    Get the current IR time from time server
    """
    c = ntplib.NTPClient()
    try:
        response = c.request("ir.pool.ntp.org", version=3)
    except Exception:
        print("Server didn't respond, trying asia...")
        try:
            response = c.request("2.asia.pool.ntp.org", version=3)
        except Exception as e:
            print(f"Server didn't respond: {e}")

    ms_since_epoch = int(response.tx_time * 1000)

    return ms_since_epoch
