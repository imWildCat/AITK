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
