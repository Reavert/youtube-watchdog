class Monitor:
	"""Base class for monitors"""
	def __init__(self, **kwargs):
		"""Base monitor constructor

		Keyword arguments:
		query: query to search (str)
		on_detect: detection callback (function)
		"""
		self.query = kwargs.get('query')
		self.on_detect = kwargs.get('on_detect')

		self.video_id = ''
		self.video_link = ''
		self.video_title = ''

	def refresh(self, query=''):
		"""Updates last video information"""
		if query:
			self.query = query

	def get_last_video_info(self):
		"""Returns dictionary with 'id', 'title', 'link' keys"""
		return {
			'id': self.get_last_video_link(),
			'title': self.get_last_video_title(),
			'link': self.get_last_video_link()
		}

	def get_last_video_id(self):
		"""Returns last video id"""
		return self.video_id

	def get_last_video_title(self):
		"""Returns last video title"""
		return self.video_title

	def get_last_video_link(self):
		"""Return last video link"""
		return self.video_link

	def run(self):
		"""Checks new video uploading""" 
		last_video_id = self.get_last_video_id()
		
		self.refresh()
		video_id = self.get_last_video_id()

		if last_video_id != video_id:
			if last_video_id:
				self.on_detect(self, self.get_last_video_info())
