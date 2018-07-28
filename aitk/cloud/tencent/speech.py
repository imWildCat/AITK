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

TEXT_TO_SPEECH_FORMATS = {
    'pcm': 1,
    'wav': 2,
    'mp3': 3,
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
        """Initializer

        Args:
            client (:obj:`TencentClient`): a TencentClient instance
        """
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

    def recognize_speech_long(self, speech=None, speech_url=None,
                              audio_format=None, callback_url=None,
                              bit_rate=16000):
        assert speech or speech_url, \
            'Either local speech file or speech_url must be provided'
        assert callback_url, 'callback_url must be provided'

        if speech_url:
            assert audio_format, \
                'format mush be provided while using speech_url'
            check_extension(audio_format)
            data = {
                'speech_url': speech_url,
                'format': FILE_TYPES_TO_CODE[audio_format]
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

    def text_to_speech(self, text, speed=100, volume=0, audio_format='mp3',
                       speaker=1, ant=0, apc=58):
        assert text, 'text cannot be None'
        assert len(text) > 0, 'text length must be larger than 0'
        assert speed >= 50 and speed <= 200, \
            'speed must be in range between 50 and 200'
        assert volume >= -10 and volume <= 10, \
            'volume must be in range between -10 and 10'
        assert audio_format.lower() in TEXT_TO_SPEECH_FORMATS \
            .keys(), 'format should be mp3, wav or pcm'
        assert speaker in [1, 5, 6, 7], \
            'speaker must be 1, 5, 6 or 7 as defined in Tencent documentation'
        assert ant >= -24 and ant <= 24, 'ant must be in [-24, 24]'
        assert apc >= 0 and apc <= 100, 'apc must be in [0, 100]'

        json_res = self.client.http_post('/aai/aai_tts', {
            'speaker': speaker,
            'format': TEXT_TO_SPEECH_FORMATS[audio_format.lower()],
            'volume': volume,
            'speed': speed,
            'text': text.encode('utf-8'),
            'aht': ant,
            'apc': apc,
        })

        return json_res
