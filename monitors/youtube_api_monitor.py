from .monitor import Monitor
from googleapiclient.discovery import build


YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

class YoutubeAPIMonitor(Monitor):
	"""Monitor class using YouTube API"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self._api_key = kwargs.get('api_key')
		if not self._api_key:
			raise Exception('Set the YouTube API key to use this implementation')

		self._youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    		developerKey=self._api_key)

	def refresh(self, query=''):
		super().refresh(query)

		search_response = self._youtube.search().list(
		    q=self.query,
		    part='id,snippet',
		    maxResults=1
		  ).execute()
		search_result = search_response.get('items', [])[0]

		self.video_id = search_result['id']['videoId']
		self.video_title = search_result['snippet']['title']
		self.video_link = f'https://www.youtube.com/watch?v={self.video_id}'
