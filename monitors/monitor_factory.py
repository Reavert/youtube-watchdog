from .monitor import Monitor
from abc import ABC, abstractmethod


class MonitorFactory(ABC):
    """Factory class for monitors"""

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @abstractmethod
    def get_monitor(self) -> Monitor:
        pass
