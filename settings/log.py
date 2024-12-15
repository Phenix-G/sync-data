"""Logging Configuration File"""

from datetime import datetime
import logging
import os

# Log directory
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Log filename (by date)
LOG_FILE = os.path.join(LOG_DIR, f"sync_{datetime.now().strftime('%Y%m%d')}.log")

# Logging configuration
LOGGING_CONFIG = {
    "level": logging.INFO,
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "handlers": [
        {
            "type": "file",
            "filename": LOG_FILE,
        },
        {
            "type": "stream",
        },
    ],
}


def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=LOGGING_CONFIG["level"],
        format=LOGGING_CONFIG["format"],
        handlers=[
            logging.FileHandler(LOGGING_CONFIG["handlers"][0]["filename"]),
            logging.StreamHandler(),
        ],
    )
