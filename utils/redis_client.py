"""Redis Client Utility"""

import logging
import redis


class RedisClient:
    @staticmethod
    def create_client(config):
        """Create Redis client connection"""
        try:
            client = redis.Redis(
                host=config["host"],
                port=config["port"],
                username=config.get("username"),
                password=config["password"],
                db=config.get("db", 0),
                ssl=config.get("ssl", False),
                ssl_cert_reqs=config.get("ssl_cert_reqs"),
                decode_responses=True,
            )
            client.ping()
            return client
        except redis.ConnectionError as e:
            logging.error(f"Redis connection failed: {str(e)}")
            return None
        except Exception as e:
            logging.error(f"Error creating Redis client: {str(e)}")
            return None
