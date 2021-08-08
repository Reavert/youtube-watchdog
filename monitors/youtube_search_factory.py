from .monitor_factory import MonitorFactory, Monitor
from .youtube_search_monitor import YoutubeSearchMonitor


class YoutubeSearchFactory(MonitorFactory):
    """YouTube search factory"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_monitor(self) -> Monitor:
        return YoutubeSearchMonitor(**self.kwargs)
