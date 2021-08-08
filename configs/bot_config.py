from .config import Config


class BotConfig(Config):
    Config.config_keywords = ['bot_name', 'avatar_url', 'search_interval', 'query', 'webhook_url', 'api_key']

    def __init__(self, filename: str = '', **kwargs):
        super().__init__(filename, **kwargs)
