import sys
import logging
import time
from TaskSingleton import TaskSingleton
from config import config

class Application:
    def __init__(self):
        pass

    @staticmethod
    def is_daylight_hours(self):
        current_hour = int(time.strftime('%H'))
        if 6 <= current_hour < 20:
            return True
        return False


if __name__ == "__main__":
    logging.info("Application started...")
    if len(sys.argv) == 2:
        script = sys.argv[1]
        task = TaskSingleton(script + ".py")
        task.kill_previous_instance()
        task.run_script()
    else:
        logging.error("No command-line argument provided. " +
                      "Please enter task name.")
        sys.exit(1)  # Exit the script with a non-zero exit code
    logging.info("Application complete.")