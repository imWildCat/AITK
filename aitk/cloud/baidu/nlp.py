class BaiduNLP(object):
    def __init__(self, client):
        """Initializer

        Args:
            client (:obj:`BaiduClient`): a BaiduClient instance
        """

        self.client = client

    def analyze_entities(self, text):
        """Analyze entities
        Documentation: https://ai.baidu.com/tech/nlp/lexical

        Args:
            text (str): text to be analyzed

        Returns:
            dict: JSON response
        """

        return self.client.http_post('nlp/v1/lexer', {
            'text': text
        }, is_json=True)
