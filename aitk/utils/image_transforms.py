import base64
from io import BytesIO
import PIL


def any_image_to_base64(any_image, format=None):
    """Convert an image to base64-encoded string

    :param any_image: a PIL.Image.Image instance, file-like object
                        or path to an image file
    :type any_image: PIL.Image.Image/file/str
    :param format: The format which the PIL image to be converted to,
                    can be 'JPEG' or 'PNG, defaults to None
    :param format: str, optional
    :return: base64-encoded string
    :rtype: str
    """

    if isinstance(any_image, str):
        # If this object is an instance of str, assme it as the path
        # to an image
        with open(any_image, 'rb') as image_file:
            return base64.b64encode(image_file.read())
    elif isinstance(any_image, PIL.Image.Image):
        buffered = BytesIO()
        any_image.save(buffered, format=format or any_image.format)
        img_str = base64.b64encode(buffered.getvalue())
        return img_str
    else:
        # Assue this object is a file-like one, which can be read()
        return base64.b64encode(any_image.read())
