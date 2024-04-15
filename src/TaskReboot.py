# note requires sudo
import subprocess
import logging


def run():
    logging.info("Task Reboot starting...")
    try:
        # Run the reboot command
        subprocess.run(["sudo", "reboot"])
    except Exception as e:
        logging.error("An error occurred while attempting to reboot", e)


if __name__ == "__main__":
    run()
