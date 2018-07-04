import base64
import sndhdr
from collections import namedtuple


def determine_audio_type(file_path):
    ret = sndhdr.what(file_path)
    if isinstance(ret, tuple):
        return ret.filetype, ret.framerate
    else:
        return ret, None


def base64_encode_audio_file(audio_file):
    audio_content = audio_file.read()
    return base64.b64encode(audio_content)


def base64_encode_audio_file_path(file_path):
    with open(file_path, 'rb') as f:
        return base64_encode_audio_file(f)
