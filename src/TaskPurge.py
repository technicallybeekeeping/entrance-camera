import logging
import time
from Purger import Purger
from config import config


def run():
    logging.info("Task Purge starting ...")
    purger = Purger(config["photos"]["path"],
                    config["photos"]["ends_with"],
                    config["photos"]["max_days_alive"])

    purger.purge_photos()
    logging.info("Task Purge complete.")


if __name__ == "__main__":
    run()
