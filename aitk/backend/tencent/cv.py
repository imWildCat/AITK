from __future__ import absolute_import, division, print_function
import requests
import os

from aitk.utils.log import logger


class TencentCV(object):

    app_id = None
    app_key = None

    def __init__(self, *args, **kwargs):
        if 'app_id' in kwargs and 'app_key' in kwargs:
            self.app_id = kwargs.get('app_id')
            self.app_key = kwargs.get('app_key')
        else:
            self.app_id = os.getenv('TENCENT_APP_ID')
            self.app_key = os.getenv('TENCENT_APP_KEY')

        logger.info(self)
