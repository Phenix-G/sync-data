"""Redis Configuration File"""

import logging
import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    logging.warning("No .env file found, using default configuration")


def str_to_bool(value: str) -> bool:
    """Convert string to boolean value"""
    return value.lower() in ("true", "1", "yes", "on")


# Source Redis Configuration
SOURCE_REDIS = {
    "host": os.getenv("SOURCE_REDIS_HOST"),
    "port": os.getenv("SOURCE_REDIS_PORT"),
    "username": os.getenv("SOURCE_REDIS_USERNAME"),
    "password": os.getenv("SOURCE_REDIS_PASSWORD"),
    "ssl": str_to_bool(os.getenv("SOURCE_REDIS_SSL", "true")),
    "protocol": os.getenv("SOURCE_REDIS_PROTOCOL", 3),
}

# Destination Redis Configuration
DEST_REDIS = {
    "host": os.getenv("DEST_REDIS_HOST"),
    "port": os.getenv("DEST_REDIS_PORT"),
    "username": os.getenv("DEST_REDIS_USERNAME"),
    "password": os.getenv("DEST_REDIS_PASSWORD"),
    "ssl": str_to_bool(os.getenv("DEST_REDIS_SSL", "true")),
    "protocol": os.getenv("DEST_REDIS_PROTOCOL", 3),
}


# Sync Configuration
SYNC_CONFIG = {
    "schedule_time": "02:00",  # Daily sync time
    "batch_size": 1000,  # Batch processing size
    "pattern": "*",  # Default sync pattern
    "retry_times": 3,  # Number of retries
    "retry_delay": 5,  # Retry delay in seconds
    "minutes": 10,  # Sync interval in minutes
    "hours": 0,  # Sync interval in hours
    "days": 0,  # Sync interval in days
    "weeks": 0,  # Sync interval in weeks
    "months": 0,  # Sync interval in months
    "years": 0,  # Sync interval in years
}
