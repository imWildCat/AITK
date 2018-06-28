from aitk.utils.common import randstr, current_timestamp, merge_two_dicts, \
    encode_dist, md5
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


def test_merge_two_dicts():
    d_1 = {'a': 1, 'b': 2}
    d_2 = {'b': 3, 'c': 4}

    result = merge_two_dicts(d_1, d_2)
    assert {'a': 1, 'b': 3, 'c': 4} == result


def test_encode_dict():
    result = encode_dist({'a': 1, 'b': '>{'})
    assert "a=1&b=%3E%7B" == result
    # test sorted
    result_2 = encode_dist({'one': 1, 'five': 5})
    assert 'five=5&one=1' == result_2


def test_md5():
    result = md5(u'hello world')
    assert '5eb63bbbe01eeed093cb22bb8f5acdc3' == result
