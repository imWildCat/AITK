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

    def detect_faces(self, image):
        """Detect faces
        Documentation: http://ai.baidu.com/docs#/Face-Detect-V3/top

        Args:
            image (:obj:`str`, :obj:`PIL.Image.Image`, :obj:`file`):
                path to image file, or a PIL image, or a file-like object.
                Supported formats: jpg, png and bmp.

        Returns:
            [dict]: JSON response
        """

        params = {
            'image': any_image_to_base64(image).decode('utf-8'),
            'image_type': 'BASE64',
            'face_field': 'age,beauty,expression,faceshape,gender,' +
            'glasses,landmark,race,quality,facetype',
            'max_face_num': 10,
            'face_type': 'LIVE',
        }

        return self.client.http_post('face/v3/detect', params, is_json=True)

    def detect_objects(self, image):
        """Detect objects
        Documentation: https://ai.baidu.com/docs#/ImageClassify-API/ed0a8379

        Args:
            image (:obj:`str`, :obj:`PIL.Image.Image`, :obj:`file`):
                path to image file, or a PIL image, or a file-like object.
                Supported formats: jpg, png and bmp.

        Returns:
            [dict]: JSON response
        """
        params = {
            'image': any_image_to_base64(image),
        }
        return self.client.http_post('image-classify/v1/object_detect', params)
