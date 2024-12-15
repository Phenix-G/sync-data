import logging

from .base_redis_handler import BaseRedisHandler


class StringHandler(BaseRedisHandler):
    def sync(self, key: str) -> bool:
        try:
            value = self.source.get(key)
            if self.dest and value:
                self.dest.set(key, value)
            return True
        except Exception as e:
            logging.error(f"Failed to sync string key {key}: {str(e)}")
            return False


class HashHandler(BaseRedisHandler):
    def sync(self, key: str) -> bool:
        try:
            value = self.source.hgetall(key)
            if self.dest and value:
                self.dest.hmset(key, value)
            return True
        except Exception as e:
            logging.error(f"Failed to sync hash key {key}: {str(e)}")
            return False


class ListHandler(BaseRedisHandler):
    def sync(self, key: str) -> bool:
        try:
            value = self.source.lrange(key, 0, -1)
            if self.dest and value:
                self.dest.delete(key)
                self.dest.rpush(key, *value)
            return True
        except Exception as e:
            logging.error(f"Failed to sync list key {key}: {str(e)}")
            return False


class SetHandler(BaseRedisHandler):
    def sync(self, key: str) -> bool:
        try:
            value = self.source.smembers(key)
            if self.dest and value:
                self.dest.delete(key)
                self.dest.sadd(key, *value)
            return True
        except Exception as e:
            logging.error(f"Failed to sync set key {key}: {str(e)}")
            return False


class ZSetHandler(BaseRedisHandler):
    def sync(self, key: str) -> bool:
        try:
            value = self.source.zrange(key, 0, -1, withscores=True)
            if self.dest and value:
                self.dest.delete(key)
                self.dest.zadd(key, dict(value))
            return True
        except Exception as e:
            logging.error(f"Failed to sync zset key {key}: {str(e)}")
            return False


# Handler mapping
HANDLERS = {
    "string": StringHandler,
    "hash": HashHandler,
    "list": ListHandler,
    "set": SetHandler,
    "zset": ZSetHandler,
}
