"""Constants Definition"""

# Redis data types
REDIS_TYPE_STRING = "string"
REDIS_TYPE_HASH = "hash"
REDIS_TYPE_LIST = "list"
REDIS_TYPE_SET = "set"
REDIS_TYPE_ZSET = "zset"

# Sync status
SYNC_STATUS_SUCCESS = "success"
SYNC_STATUS_FAILED = "failed"
SYNC_STATUS_PARTIAL = "partial"

# Time formats
DATE_FORMAT = "%Y%m%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Default values
DEFAULT_BATCH_SIZE = 1000
DEFAULT_SYNC_PATTERN = "*"
DEFAULT_DB = 0

# Retry configuration
MAX_RETRY_COUNT = 3
RETRY_DELAY = 5  # seconds
