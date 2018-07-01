from __future__ import absolute_import, division, print_function
import requests
import os

import base64

from aitk.utils.log import logger
from aitk.utils.image_transforms import any_image_to_base64


class TencentCV(object):

    def __init__(self, client):
        """ Construct TencentCV

        :param client: A TencentClient instance
        :type client: TencentClient
        """

        self.client = client

    def ocr(self, image):
        base64_image = any_image_to_base64(image)
        response_json = self.client.http_post(
            'ocr/ocr_generalocr',
            {
                'image': base64_image,
                # 'format': 1,
            })
        # FIXME: weird 'no auth' error of API, contacting Tencent.
        print(response_json)

    def detect_objects(self, image):
        """Detect objects

        :param image: a Pillow image, a file of image or a path to image
        :type image: file or str
        :return: json result
        :rtype: json
        """

        base64_image = any_image_to_base64(image)
        response_json = self.client.http_post(
            'vision/vision_objectr',
            {
                'image': base64_image,
                'topk': 5,
                'format': 1,
            })
        return response_json

    def detect_faces(self, image, mode=1):
        """Detect faces
        Documentation: https://ai.qq.com/doc/detectface.shtml

        :param image: a Pillow image, a file of image or a path to image
        :type image: file or str
        :param mode: mode, defaults to 1
        :param mode: int, optional
        """

        # FIXME: unreasonable error of API, contacting Tencent.

        base64_image = any_image_to_base64(image)
        response_json = self.client.http_post(
            'face/face_detectface',
            {
                'image': base64_image,
                'mode': int(mode)
            }
        )
        return response_json
