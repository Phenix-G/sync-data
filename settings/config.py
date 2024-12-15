"""Unified Configuration Entry Point"""

from .redis import SOURCE_REDIS, DEST_REDIS, SYNC_CONFIG
from .log import LOGGING_CONFIG, LOG_FILE, setup_logging


class Config:
    """Configuration Management Class"""

    @classmethod
    def get_source_redis_config(cls):
        """Get source Redis configuration"""
        return SOURCE_REDIS

    @classmethod
    def get_dest_redis_config(cls):
        """Get destination Redis configuration"""
        return DEST_REDIS

    @classmethod
    def get_sync_config(cls):
        """Get synchronization configuration"""
        return SYNC_CONFIG

    @classmethod
    def get_logging_config(cls):
        """Get logging configuration"""
        return LOGGING_CONFIG

    @classmethod
    def get_log_path(cls):
        """Get log file path"""
        return LOG_FILE

    @classmethod
    def setup_logging(cls):
        """Setup logging configuration"""
        setup_logging()
