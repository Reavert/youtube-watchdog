import time
import argparse
from configs.bot_config import BotConfig
from webhook_bot import WebhookBot
from monitors.youtube_search_factory import YoutubeSearchFactory
from monitors.youtube_api_factory import YoutubeAPIFactory


DEFAULT_FILE_NAME = 'default.json'

global webhook_bot


def on_detection(sender, video_info: dict):
    global webhook_bot

    timestamp = time.strftime('%H:%M:%S', time.localtime())

    video_title = video_info['title']
    video_link = video_info['link']

    print(f'[{timestamp}]: A new video was found for the query \'{sender.query}\': \'{video_title}\' ({video_link})')
    webhook_bot.send_message(f'A new video was found for the query \'{sender.query}\'\n{video_title}\n{video_link}')


def main():
    global webhook_bot

    parser = argparse.ArgumentParser(description='Tracking uploading new videos on YouTube and notifying in specific '
                                                 'discord channel via webhooks')
    parser.add_argument('-n', '--name', help='Discord bot name displayed in channel')
    parser.add_argument('-i', '--icon', help='Url to bot\'s avatar icon')
    parser.add_argument('-t', '--search-interval', help='Time in seconds for searching query', type=int)
    parser.add_argument('-q', '--query', help='Query string to tracking')
    parser.add_argument('-u', '--webhook-url', help='Discord bot\'s webhook url')
    parser.add_argument('-f', '--config-file', help='Path to config file')
    parser.add_argument('-a', '--api-key', help='Optional API-key for using YouTube API')

    arguments = parser.parse_args()

    if arguments.config_file:
        config = BotConfig(arguments.config_file, default_file=DEFAULT_FILE_NAME)
        print(f'Custom config \'{arguments.config_file}\' successfully loaded!')
    else:
        config = BotConfig(default_file=DEFAULT_FILE_NAME)
        print(f'Default config \'{DEFAULT_FILE_NAME}\' successfully loaded!')

    if arguments.name:
        config.bot_name = arguments.name
    if arguments.icon:
        config.avatar_url = arguments.icon
    if arguments.search_interval:
        config.search_interval = arguments.search_interval
    if arguments.query:
        config.query = arguments.query
    if arguments.webhook_url:
        config.webhook_url = arguments.webhook_url
    if arguments.api_key:
        config.api_key = arguments.api_key
    print(f'Info: {config}')

    webhook_bot = WebhookBot(
        config.webhook_url,
        username=config.bot_name,
        avatar_url=config.avatar_url
    )
    if config.api_key:
        factory = YoutubeAPIFactory(query=config.query, on_detect=on_detection, api_key=config.api_key)
        print('YouTube API search is used')
    else:
        factory = YoutubeSearchFactory(query=config.query, on_detect=on_detection)
        print('Default search is used')
    monitor = factory.get_monitor()
    while True:
        monitor.run()
        time.sleep(config.search_interval)


if __name__ == '__main__':
    main()
