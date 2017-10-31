"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""
import time
import datetime


def make_readable(seconds):

    if seconds < 86400:
        return time.strftime('%H:%M:%S', time.gmtime(seconds))
    else:

        t = time.strftime('%H:%M:%S', time.gmtime(seconds))
        x = datetime.timedelta(0, seconds).days
        d = 24 * int(x)+ int(t[:2])
        return str(d) + t[2:]
