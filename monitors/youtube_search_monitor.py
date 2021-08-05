from .monitor import Monitor
from youtubesearchpython import CustomSearch, VideoSortOrder


class YoutubeSearchMonitor(Monitor):
	"""Monitor class using youtube-search-python module"""
	def refresh(self, query=''):
		super().refresh(query)

		video_search = CustomSearch(self.query, VideoSortOrder.uploadDate, limit = 1)
		search_result = video_search.result()['result'][0]

		self.video_id = search_result['id']
		self.video_title = search_result['title']
		self.video_link = search_result['link']
