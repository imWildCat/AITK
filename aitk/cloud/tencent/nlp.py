class TencentNLP(object):

    def __init__(self, client):
        self.client = client

    def analyze_entities(self, text):
        json_res = self.client.http_post(
            '/nlp/nlp_wordpos',
            {'text': text.encode('gbk')})
        # FIXED: charset error
        # This stupid issue is because the Tencent AI team is using 'gbk'
        # instead of 'utf-8'
        return json_res

    def translate(self, text=None, source=None, target=None):
        """Translate API
        Original documentation: https://ai.qq.com/doc/nlptrans.shtml
        Note: the second API mentioned in the documentation is used.

        :param text: the text to be translated, defaults to None
        :param text: str, required
        :param source: source language, defaults to None
        :param source: str, required
        :param target: target language, defaults to None
        :param target: str, required
        :return: json response
        :rtype: object
        """
        assert text, 'text must be provided'
        assert source, 'source must be provided'
        assert target, 'target must be provided'

        json_res = self.client.http_post(
            'nlp/nlp_texttranslate',
            {
                'text': text,
                'source': source,
                'target': target
            }
        )

        return json_res
