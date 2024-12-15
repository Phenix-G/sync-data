import logging
import time
import schedule

from handlers.redis import RedisSyncManager
from settings.config import Config
from utils.redis_client import RedisClient
from utils.helpers import calculate_time_cost


@calculate_time_cost
def sync_data():
    """Execute data synchronization"""
    logging.info("Starting data synchronization...")

    # Get configurations
    source_config = Config.get_source_redis_config()
    dest_config = Config.get_dest_redis_config()
    sync_config = Config.get_sync_config()

    # Connect to Redis
    source = RedisClient.create_client(source_config)
    dest = RedisClient.create_client(dest_config)

    if not source:
        logging.error("Failed to connect to source Redis server")
        return

    try:
        # Create sync manager
        sync_manager = RedisSyncManager(source, dest)

        # Execute synchronization
        total_keys, success_keys = sync_manager.sync_pattern(
            pattern=sync_config["pattern"], batch_size=sync_config["batch_size"]
        )

        # Log sync results
        logging.info(
            f"Sync completed! Processed {total_keys} keys, successfully synced {success_keys} keys"
        )

    except Exception as e:
        logging.error(f"Error during synchronization: {str(e)}")
    finally:
        source.close()
        if dest:
            dest.close()


def setup_schedule(sync=False):
    if sync:
        """Setup schedule based on configuration"""
        sync_config = Config.get_sync_config()

        # If minutes is set, run every X minutes
        schedule.every(sync_config["minutes"]).minutes.do(sync_data)
        logging.info(f"Scheduled to run every {sync_config['minutes']} minutes")


def main():
    """Main function"""
    # Setup logging
    Config.setup_logging()
    logging.info("Data sync service started...")
    sync = False

    # Setup schedule
    setup_schedule()

    # Run sync immediately for the first time
    sync_data()

    # Keep running scheduled tasks
    logging.info("Starting schedule loop, press Ctrl+C to exit")
    try:
        while sync:
            schedule.run_pending()
            time.sleep(60 * 10)  # Wait for 60 seconds before next check
    except KeyboardInterrupt:
        logging.info("Service stopped by user")


if __name__ == "__main__":
    main()
