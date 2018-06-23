from aitk.utils.common import randstr, current_timestamp
import datetime
import math


def test_randstr():
    generated_str1 = randstr(32)
    assert 32 == len(generated_str1)

    generated_str2 = randstr(128, upper_case=False)
    assert generated_str2 != generated_str2.upper()

    generated_str3 = randstr(128, upper_case=True)
    assert generated_str3 == generated_str3.upper()


def test_current_timestamp():
    current = current_timestamp()

    timestamp = math.floor(datetime.datetime.now().timestamp())

    assert len(str(current)) == 10
    assert current == timestamp