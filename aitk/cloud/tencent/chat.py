class TencentChat(object):

    def __init__(self, client):
        """Initializer

        Args:
            client (:obj:`TencentClient`): a TencentClient instance
        """
        self.client = client

    def chat(self, session_id, text):
        """Chat API
        Documentation: https://ai.qq.com/doc/nlpchat.shtml

        :param session_id: the ID of session, maximum length: 32
        :type session_id: str
        :param text: the text for chatting
        :type text: str
        :return: JSON response
        :rtype: dict
        """

        json_res = self.client.http_post(
            'nlp/nlp_textchat',
            {
                'question': text.encode('utf-8'),
                'session': session_id,
            }
        )
        return json_res
