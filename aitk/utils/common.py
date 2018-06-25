import random
import string
import calendar
import time

from future.standard_library import install_aliases

install_aliases()

from urllib.parse import urlencode
import hashlib


def randstr(length, upper_case=True):
    case = string.ascii_uppercase if upper_case else string.ascii_lowercase
    return ''.join(random.choice(case + string.digits)
                   for _ in range(length))


def current_timestamp():
    return calendar.timegm(time.gmtime())


def merge_two_dicts(a, b):
    c = a.copy()
    c.update(b)
    return c


def encode_dist(d):
    encoded = urlencode(d)
    return encoded


def md5(value):
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()
