"""Custom Exception Classes"""


class SyncError(Exception):
    """Base exception class for synchronization process"""

    pass


class ConnectionError(SyncError):
    """Connection error"""

    pass


class ConfigError(SyncError):
    """Configuration error"""

    pass


class SyncDataError(SyncError):
    """Data synchronization error"""

    pass


class UnsupportedTypeError(SyncError):
    """Unsupported data type error"""

    pass
