import requests
import os
import pickle

from aitk.utils.common import current_timestamp, is_debug, merge_two_dicts, \
    urljoin

from .cv import BaiduCV
from .nlp import BaiduNLP

from .chat import BaiduChat

TOKEN_CACHE_FILE = '/tmp/aitk_baidu.p'


def _touch_file(path):
    with open(path, 'a'):
        os.utime(path, None)


class BaiduClient(object):

    BASE_URL = 'https://aip.baidubce.com'

    def __init__(self, *args, **kwargs):
        if 'api_key' in kwargs and 'secret_key' in kwargs:
            self.api_key = kwargs.get('api_key')
            self.secret_key = kwargs.get('secret_key')
        else:
            self.api_key = os.getenv('BAIDU_API_KEY')
            self.secret_key = os.getenv('BAIDU_SECRET_KEY')

        self.cv = BaiduCV(self)
        self.nlp = BaiduNLP(self)
        self.chat = BaiduChat(self)

    def _request_token_data(self):
        params = (
            ('grant_type', 'client_credentials'),
            ('client_id', self.api_key),
            ('client_secret', self.secret_key),
        )

        response = requests.get(
            'https://aip.baidubce.com/oauth/2.0/token',
            params=params, verify=not is_debug)

        if response and response.status_code == 200 and \
                'access_token' in response.json():

            # Save token
            json_data = response.json()
            json_data['expires_at'] = \
                json_data['expires_in'] \
                + current_timestamp()
            self._save_token_data(json_data)

            return json_data
        else:
            return None

    def _save_token_data(self, token_data):
        if not os.path.isfile(TOKEN_CACHE_FILE):
            _touch_file(TOKEN_CACHE_FILE)
        with open(TOKEN_CACHE_FILE, 'wb') as f:
            pickle.dump(token_data, f)

    def _request_and_cache_token_data(self):
        if os.path.isfile(TOKEN_CACHE_FILE):
            # TODO: cache in memoery
            with open(TOKEN_CACHE_FILE, 'rb') as f:
                try:
                    cached = pickle.load(f)
                    if cached and cached['expires_at'] > current_timestamp():
                        return cached
                except EOFError:
                    pass
        return self._request_token_data()

    def _get_access_token(self):
        token_data = self._request_and_cache_token_data()
        assert 'access_token' in token_data
        return token_data['access_token']

    def http_post(self, uri, data, is_json=False, prefix=True):
        """Post data to api
        Documentation: http://ai.baidu.com/docs#/UNIT-API/top
        Please note that creating app which has the permission to use UNIT is
        tricky. Try https://console.bce.baidu.com/ai/#/ai/unit/app/list

        Args:
            uri (str): API URI
            data (dict): data as a dict
            is_json (bool, optional): Defaults to False. Post as JSON data
            prefix (bool, optional): Defaults to True.
                                     Whether to add prefix for request URI

        Raises:
            requests.exceptions.BaseHTTPError: When this URL is not found

        Returns:
            dict: data in JSON
        """
        post_data = {
            'access_token': self._get_access_token(),
        }

        post_data = merge_two_dicts(post_data, data)

        if prefix:
            request_url = urljoin(self.BASE_URL, '/rest/2.0/' + uri)
        else:
            request_url = urljoin(self.BASE_URL, uri)

        if is_json:
            access_token = post_data.pop('access_token')
            r = requests.post(request_url + '?access_token=' + access_token,
                              json=post_data, verify=not is_debug())
        else:
            r = requests.post(request_url, data=post_data,
                              verify=not is_debug())

        if r.status_code == requests.codes.ok:
            return r.json()
        elif r.status_code == 404:
            raise requests.exceptions.BaseHTTPError('404 Not Found')
        else:
            return None
