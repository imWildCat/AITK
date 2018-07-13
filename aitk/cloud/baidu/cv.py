from aitk.utils.image_transforms import any_image_to_base64


class BaiduCV(object):
    def __init__(self, client):
        """Construct BaiduCV

        Args:
            client (:obj:`BaiduClient`): a BaiduClient instance
        """
        self.client = client

    def _ocr(self, uri, image):
        base64_image = any_image_to_base64(image)
        response_json = self.client.http_post(
            uri,
            {
                'image': base64_image,
            })
        return response_json

    def ocr_accurate_basic(self, image):
        """Perform accurate OCR to an image
        Doc: http://ai.baidu.com/docs#/OCR-API/top

        Args:
            image (:obj:`str`, :obj:`PIL.Image.Image`, :obj:`file`):
                path to image file, or a PIL image, or a file-like object.
                Supported formats: jpg, png and bmp.
        """
        return self._ocr('ocr/v1/accurate_basic', image)

    def ocr_general_basic(self, image):
        """Perform general OCR to an image
        Doc: http://ai.baidu.com/docs#/OCR-API/top

        Args:
            image (:obj:`str`, :obj:`PIL.Image.Image`, :obj:`file`):
                path to image file, or a PIL image, or a file-like object.
                Supported formats: jpg, png and bmp.
        """
        return self._ocr('ocr/v1/general_basic', image)
