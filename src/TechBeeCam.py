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
import IPAddressChecker
import IPAddress

ip_checker = IPAddressChecker(ipaddress=IPAddress)
mailer = Mail(config["mail"]["enabled"],
              config["mail"]["sender"],
              config["mail"]["app-password"],
              config["mail"]["recipient"],
              config["mail"]["port"],
              config["mail"]["server"],
              config["mail"]["subject"],
              config["mail"]["body"])

purger = Purger(config["photos"]["path"],
                config["photos"]["ends_with"],
                config["photos"]["max_days_alive"])


def task_photo():
    logging.info("Task Photo starting ...")
    global mailer
    cam1 = Picamera2()
    formatter1 = FileNameFormatter()
    cam = Photo(cam=cam1, formatter=formatter1)
    file_path = cam.capture()

    mailer.send_photo(file_path,
                      config["mail"]["photo"]["subject"],
                      config["mail"]["photo"]["body"])

    logging.info("Task Photo Complete")


def task_check_ip():
    global ip_checker
    if (ip_checker.has_changed() is True):
        global mailer

        mailer.send_ip_change(config["mail"]["ip-changed"]["subject"],
                              config["mail"]["ip-changed"]["body"])


def task_video():
    logging.info("Task Video starting ...")
    global mailer
    cam1 = Picamera2()
    formatter1 = FileNameFormatter()
    cam = Video(cam=cam1, formatter=formatter1)
    file_path = cam.capture()

    mailer.send_video(file_path,
                      config["mail"]["video"]["subject"],
                      config["mail"]["video"]["body"])

    logging.info("Task Video Complete")


def task_purge():
    global purger
    purger.purge_photos()


if __name__ == "__main__":
    logging.info("TechBeeCam starting ...")

    schedule.every().minute.do(task_check_ip)
    schedule.every().hour.at(":00").do(task_photo)
    schedule.every().hour.at(":30").do(task_video)
    schedule.every().day.at("12:15").do(task_purge)

    while True:
        schedule.run_pending()
        time.sleep(1)
