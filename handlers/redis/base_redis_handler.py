from abc import ABC, abstractmethod


class BaseRedisHandler(ABC):
    """Base Redis Sync Handler"""

    def __init__(self, source, dest=None):
        self.source = source
        self.dest = dest

    @abstractmethod
    def sync(self, key: str) -> bool:
        """Sync method to be implemented by subclasses"""
        pass
