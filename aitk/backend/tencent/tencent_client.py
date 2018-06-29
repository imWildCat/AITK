import requests
import os

from aitk.utils.common import current_timestamp, randstr, merge_two_dicts, \
    encode_dist, md5, urljoin, is_debug

from .cv import TencentCV
from .nlp import TencentNLP

HTTP_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}


class TencentClient(object):

    BASE_URL = 'https://api.ai.qq.com/'

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
        self.nlp = TencentNLP(self)

    def get_id(self):
        return self.app_id

    def get_key(self):
        return self.app_key

    def http_post(self, url, data):
        post_data = {
            'app_id': self.app_id,
            'time_stamp': current_timestamp(),
            'nonce_str': randstr(15, upper_case=False),
        }
        post_data = merge_two_dicts(post_data, data)

        encoded = encode_dist(post_data)
        encoded += '&app_key=' + self.app_key

        signature = md5(encoded).upper()

        post_data['sign'] = signature
        # post_data['app_key'] = self.app_key

        request_url = urljoin(self.BASE_URL, 'fcgi-bin/' + url)
        r = requests.post(request_url, data=post_data,
                          headers=HTTP_HEADERS, verify=not is_debug())

        if r.status_code == requests.codes.ok:
            return r.json()
        elif r.status_code == 404:
            raise requests.exceptions.BaseHTTPError('404 Not Found')
        else:
            return None
