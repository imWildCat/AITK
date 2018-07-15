class BaiduNLP(object):
    def __init__(self, client):
        self.client = client

    def analyze_entities(self, text):
        return self.client.http_post('nlp/v1/lexer', {
            'text': text
        }, is_json=True)
