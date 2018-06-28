from __future__ import absolute_import, division, print_function
import requests
import os
import base64

from aitk.utils.log import logger


class TencentCV(object):

    def __init__(self, client):
        """ Construct TencentCV

        :param client: A TencentClient instance
        :type client: TencentClient
        """

        self.client = client

    def ocr(self, image):
        base64_image = base64.b64encode(image.tobytes())
        response_json = self.client.http_post(
            'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr',
            {'image': base64_image})
        print(response_json)
