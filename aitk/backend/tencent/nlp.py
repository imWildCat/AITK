class TencentNLP(object):

    def __init__(self, client):
        self.client = client

    def analyzing_entities(self, text):
        json_res = self.client.http_post(
            'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordpos',
            {u'text': text.encode('unicode-escape')})
        # FIXME: charset error
        print(json_res)
