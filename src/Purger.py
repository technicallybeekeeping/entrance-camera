import os
import datetime
import logging


class Purger:
    def __init__(self, path, ends_with, max_days):
        self.path = path
        self.ends_with = ends_with
        self.max_days = max_days

    def remove(self, file_path):
        logging.info("Purger remove")
        os.remove(file_path)

    # function to perform delete operation based on condition
    def purge_photos(self):
        try:
            for (root, dirs, files) in os.walk(self.path, topdown=True):
                for f in files:
                    if not f.endswith(self.ends_with):
                        continue

                    file_path = os.path.join(root, f)
                    modified_ts = os.path.getmtime(file_path)
                    modified_on = datetime.datetime.fromtimestamp(modified_ts)
                    delta = (datetime.datetime.now() - modified_on)
                    if delta.days > self.max_days:
                        logging.info(f"Delete : {f}, days old {delta.days}, max_days {self.max_days}")
                        os.remove(file_path)
                    else:
                        logging.info(f"!!! Do NOT Delete : {f}, days old {delta.days}, max_days {self.max_days}")
        except Exception as ex:
            template = "Exception of type {0} occurred in Purger module." \
                + "Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logging.error(message)


if __name__ == "__main__":
    from config import config

    sut = Purger(config["photos"]["path"],
                 config["photos"]["ends_with"],
                 config["photos"]["max_days_alive"])
    sut.purge_photos()
