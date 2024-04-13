from config import config
import logging
import schedule
import time
from Photo import Photo
from Video import Video
from Mail import Mail
from Purger import Purger
from picamera2 import Picamera2
from FileNameFormatter import FileNameFormatter
from IPAddressChecker import IPAddressChecker
from IPAddress import IPAddress
from ProcessLocker import ProcessLocker


class Application:
    def __init__(self):
        self.ip_checker = IPAddressChecker(ipaddress=IPAddress)
        self.mailer = Mail(config["mail"]["enabled"],
                           config["mail"]["sender"],
                           config["mail"]["app-password"],
                           config["mail"]["recipient"],
                           config["mail"]["port"],
                           config["mail"]["server"])
        self.purger = Purger(config["photos"]["path"],
                             config["photos"]["ends_with"],
                             config["photos"]["max_days_alive"])

    def is_daylight_hours(self):
        current_hour = int(time.strftime('%H'))
        if 6 <= current_hour < 24:
            return True
        return False

    def task_photo(self):
        logging.info("Task Photo starting ...")
        if not self.is_daylight_hours():
            return

        cam1 = Picamera2()
        formatter1 = FileNameFormatter()
        cam = Photo(cam=cam1, formatter=formatter1)
        file_path = cam.capture()

        self.mailer.send_photo(file_path,
                               config["mail"]["photo"]["subject"],
                               config["mail"]["photo"]["body"])

        logging.info("Task Photo Complete")

    def task_check_ip(self):
        if self.ip_checker.has_changed():
            self.mailer.send_ip_change(config["mail"]["ip-changed"]["subject"],
                                       config["mail"]["ip-changed"]["body"])

    def task_video(self):
        logging.info("Task Video starting ...")
        if not self.is_daylight_hours():
            return

        cam1 = Picamera2()
        formatter1 = FileNameFormatter()
        cam = Video(cam=cam1, formatter=formatter1)
        file_path = cam.capture(config["videos"]["duration_secs"])

        self.mailer.send_video(file_path,
                               config["mail"]["video"]["subject"],
                               config["mail"]["video"]["body"])

        logging.info("Task Video Complete")

    def task_purge(self):
        self.purger.purge_photos()

    def schedule_tasks(self):
        schedule.every().minute.do(self.task_check_ip)
        schedule.every().hour.at(":00").do(self.task_photo)
        schedule.every().hour.at(":30").do(self.task_video)
        schedule.every().day.at("12:15").do(self.task_purge)

    def run(self):
        locker = ProcessLocker()
        if not locker.acquire_lock():
            logging.error(
                "Another instance of Application.py is already running."
                )
            return

        try:
            logging.info("Application starting ...")
            self.schedule_tasks()
            while True:
                schedule.run_pending()
                time.sleep(1)
        finally:
            locker.release_lock()


if __name__ == "__main__":
    app = Application()
    app.run()
