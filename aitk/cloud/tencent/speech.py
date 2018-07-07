from aitk.utils.audio import determine_audio_type, \
    base64_encode_audio_file_path
from aitk.utils.common import merge_two_dicts


SUPPORTED_FILE_TYPES = ['pcm', 'wav', 'amr', 'silk']
# TODO: `sndhdr` does not support pcm and silk, find the solution
FILE_TYPES_TO_CODE = {
    'pcm': 1,
    'wav': 2,
    'amr': 3,
    'silk': 4,
}


def check_extension(ext):
    if ext.lower() not in SUPPORTED_FILE_TYPES:
        raise Exception(
            'The audio type is {}, which is not supported by Tencent.'
            .format(ext))
    return True


def check_file_type(file_path):
    f_type, framerate = determine_audio_type(file_path)
    check_extension(f_type)
    return f_type, framerate


class TencentSpeech(object):

    def __init__(self, client):
        self.client = client

    def recognize_speech_short(self, speech, bit_rate=16000):
        # TODO: Eliminate bit_rate because it is an optional field
        f_type, framerate = check_file_type(speech)

        assert (framerate or bit_rate) in [
            8000, 16000], 'Framerate is not supported'

        json_res = self.client.http_post(
            '/aai/aai_asr',
            {
                'speech': base64_encode_audio_file_path(speech),
                'format': FILE_TYPES_TO_CODE[f_type],
                'rate': framerate or bit_rate,
            }
        )
        # FIXED: charset error
        # This stupid issue is because the Tencent AI team is using 'gbk'
        # instead of 'utf-8'
        return json_res

    def recognize_speech_long(self, speech=None, speech_url=None, format=None,
                              callback_url=None, bit_rate=16000):
        assert speech or speech_url, \
            'Either local speech file or speech_url must be provided'
        assert callback_url, 'callback_url must be provided'

        if speech_url:
            assert format, 'format mush be provided while using speech_url'
            check_extension(format)
            data = {
                'speech_url': speech_url,
                'format': FILE_TYPES_TO_CODE[format]
            }
        else:
            f_type, _ = check_file_type(speech)
            format_code = FILE_TYPES_TO_CODE[f_type]
            data = {
                'speech': base64_encode_audio_file_path(speech),
                'format': format_code,
            }

        data = merge_two_dicts(data, {'callback_url': callback_url})

        json_res = self.client.http_post(
            '/aai/aai_wxasrlong',
            data,
        )

        return json_res
