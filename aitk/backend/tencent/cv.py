from __future__ import absolute_import, division, print_function
import requests
import os
from io import BytesIO
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
        base64_image = self.pil_image_to_base64(image)
        response_json = self.client.http_post(
            'ocr/ocr_generalocr',
            {
                'image': base64_image,
                # 'format': 1,
            })
        # FIXME: weird 'no auth' error
        print(response_json)

    def detect_objects(self, image):
        base64_image = self.pil_image_to_base64(image)
        response_json = self.client.http_post(
            'vision/vision_objectr',
            {
                'image': base64_image,
                'topk': 5,
                'format': 1,
            })
        return response_json

    def pil_image_to_base64(self, image):
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        return img_str
