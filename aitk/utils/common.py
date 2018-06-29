import random
import string
import calendar
import time
import os

from future.standard_library import install_aliases

install_aliases()

from urllib.parse import urlencode, quote, urljoin
import hashlib

DEBUG = len(os.getenv('AITK_DEBUG', '')) > 0


def is_debug():
    """Whether AITK is in debug mode

    :return: the flag for debug mode
    :rtype: bool
    """
    return DEBUG


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
    sorted_dict = sorted(d.items(), key=lambda val: val[0])
    encoded = urlencode(sorted_dict, encoding='unicode-escape')
    return encoded


def encode_text(text):
    return text.encode('utf8')


def md5(value):
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()
