from aitk.utils.audio import determine_audio_type, \
    base64_encode_audio_file_path


SUPPORTED_FILE_TYPES = ['pcm', 'wav', 'amr', 'silk']
# TODO: `sndhdr` does not support pcm and silk, find the solution
FILE_TYPES_TO_CODE = {
    'pcm': 1,
    'wav': 2,
    'amr': 3,
    'silk': 4,
}


def check_file_type(file_path):
    f_type, framerate = determine_audio_type(file_path)
    if f_type not in SUPPORTED_FILE_TYPES:
        raise Exception(
            'The audio type is {}, which is not supported by Tencent.'
            .format(f_type))
    return f_type, framerate


class TencentSpeech(object):

    def __init__(self, client):
        self.client = client

    def recognize_speech_short(self, speech, bit_rate=16000):
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
