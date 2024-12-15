import logging

from .redis_handlers import HANDLERS


class RedisSyncManager:
    """Redis Synchronization Manager"""

    def __init__(self, source, dest=None):
        self.source = source
        self.dest = dest
        self.handlers = {
            data_type: handler_class(source, dest)
            for data_type, handler_class in HANDLERS.items()
        }

    def sync_key(self, key: str) -> bool:
        """Synchronize a single key"""
        try:
            key_type = self.source.type(key)
            handler = self.handlers.get(key_type)
            if handler:
                return handler.sync(key)
            else:
                logging.warning(f"Unsupported data type: {key_type}, key: {key}")
                return False
        except Exception as e:
            logging.error(f"Failed to sync key {key}: {str(e)}")
            return False

    def sync_pattern(self, pattern: str = "*", batch_size: int = 1000):
        """Synchronize keys matching the pattern"""
        total_keys = 0
        success_keys = 0

        try:
            keys = self.source.keys(pattern)
            total_keys = len(keys)

            for key in keys:
                if self.sync_key(key):
                    success_keys += 1

                if success_keys % batch_size == 0:
                    logging.info(f"Synced {success_keys}/{total_keys} keys")

        except Exception as e:
            logging.error(f"Failed to sync pattern {pattern}: {str(e)}")

        return total_keys, success_keys
