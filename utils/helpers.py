"""Helper Functions"""

from functools import wraps
import logging
import time

from .constants import MAX_RETRY_COUNT, RETRY_DELAY


def retry_on_error(max_retries: int = MAX_RETRY_COUNT, delay: int = RETRY_DELAY):
    """Retry decorator for error handling"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries == max_retries:
                        logging.error(f"Failed after {max_retries} retries: {str(e)}")
                        raise
                    logging.warning(f"Retry {retries}: {str(e)}")
                    time.sleep(delay)
            return None

        return wrapper

    return decorator


def calculate_time_cost(func):
    """Decorator for calculating function execution time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"Function {func.__name__} execution time: {duration:.2f} seconds")
        return result

    return wrapper


def format_redis_key(key: str):
    """Format Redis key name"""
    return key.strip().replace(" ", "_")


def chunk_list(lst, chunk_size):
    """Split list into fixed-size chunks"""
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]
