class BaiduChat(object):

    def __init__(self, client):
        self.client = client

    def chat_v1(self, scene_id, query, session_id=''):
        """Baidu Chat API

        Args:
            scene_id (int): ID for the scene, need to be created
            query (str): Text for chatting
            session_id (str, optional): Defaults to ''. Session ID,
                while empty, new session will be created

        Returns:
            dict: JSON response
        """

        post_data = {
            'scene_id': scene_id,
            'session_id': session_id,
            'query': query,
        }

        json_res = self.client.http_post(
            '/rpc/2.0/solution/v1/unit_utterance',
            post_data,
            is_json=True,
            prefix=False,
        )
        return json_res
