import requests
import os

from aitk.utils.common import current_timestamp, randstr, merge_two_dicts, \
    encode_dist, md5

from .cv import TencentCV


class TencentClient(object):

    app_id = None
    app_key = None

    def __init__(self, *args, **kwargs):
        if 'app_id' in kwargs and 'app_key' in kwargs:
            self.app_id = kwargs.get('app_id')
            self.app_key = kwargs.get('app_key')
        else:
            self.app_id = os.getenv('TENCENT_APP_ID')
            self.app_key = os.getenv('TENCENT_APP_KEY')

        # Init abilities
        self.cv = TencentCV(self)

    def get_id(self):
        return self.app_id

    def get_key(self):
        return self.app_key

    def http_post(self, url, data):
        post_data = {
            'app_id': self.app_id,
            'time_stamp': current_timestamp(),
            'nonce_str': randstr(32),
        }
        post_data = merge_two_dicts(post_data, data)

        encoded = encode_dist(post_data)
        encoded += '&app_key=' + self.app_key

        # print('post_data:', post_data)
        # print('======')
        # print('encoded:', encoded)

        signature = md5(encoded)

        post_data['sign'] = signature

        # print('===after===')
        # print(post_data)

        r = requests.post(url, data=post_data)

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return None
