# [YouTube Watchdog](https://github.com/Ryavell/youtube-watchdog)
__________________________________________________________________
## For what
##### Monitoring of latest uploading YouTube video and notifying in specific discord channel via webhooks.

## Installing
```commandline
git clone https://github.com/Ryavell/youtube-watchdog
cd youtube-watchdog
pip install -r requirements.txt
python app.py
```
## Parameters
By default `app.py` takes the configuration information from the `default.json` file.

You can copy this file and set the custom bot config or use following structure _(use -f parameter to set custom config file)_.
```json
{
	"bot_name": "Your Bot Name",
	"avatar_url": "https://your.avatar.url.com/amazing_avatar.png",
	"search_interval": 600,
	"query": "Music",
	"webhook_url": "https://discord.com/api/webhooks/channel/webhook_url",
	"api_key": ""
}
```
Also, you can set the config parameters from the command line:
- **-n, --name:** _Discord bot name displayed in channel_
- **-i, --icon:** _Url to bot's avatar icon_
- **-t, --search-interval:** _Time in seconds for searching query_
- **-q, --query:** _Query string to tracking_
- **-u, --webhook-url:** _Discord bot's webhook url_
- **-f, --config-file:** _Path to config file_
- **-a, --api-key:** _Optional developer API-key for using YouTube Data API v3_
#### If you use YouTube Data API, then it costs 100 quota scores per request
## External modules
* For default search was used [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)
* For YouTube API search used [Youtube Data API v3](https://developers.google.com/youtube/v3)