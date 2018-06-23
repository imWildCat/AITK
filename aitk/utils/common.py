import random
import string
import calendar
import time


def randstr(length, upper_case=True):
    case = string.ascii_uppercase if upper_case else string.ascii_lowercase
    return ''.join(random.choice(case + string.digits)
                   for _ in range(length))


def current_timestamp():
    return calendar.timegm(time.gmtime())
