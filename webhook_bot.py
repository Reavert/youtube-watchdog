import json
import requests


class WebhookBot:
    def __init__(self, webhook_url: str, **kwargs):
        self.username = kwargs.get('username')
        self.avatar_url = kwargs.get('avatar_url')
        self.webhook_url = webhook_url

    def __get_webhook_json(self, content):
        return {
            'username': self.username,
            'avatar_url': self.avatar_url,
            'content': content
        }

    def send_message(self, content: str):
        if self.webhook_url:
            data = json.dumps(self.__get_webhook_json(content))
            requests.post(self.webhook_url, data=data, headers={'Content-Type': 'application/json'})
