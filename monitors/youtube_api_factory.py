from .monitor_factory import MonitorFactory, Monitor
from .youtube_api_monitor import YoutubeAPIMonitor


class YoutubeAPIFactory(MonitorFactory):
    """YouTube API factory"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_monitor(self) -> Monitor:
        return YoutubeAPIMonitor(**self.kwargs)
