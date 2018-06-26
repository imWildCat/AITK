from PIL import Image


def resize(image, size):
    w, h = size
    image.resize(((w, h)))
    return image
