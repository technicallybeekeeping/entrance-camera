import config
import logging
import schedule
import time
import Photo
import Video
import Mail
import Purger
from picamera2 import Picamera2
from FileNameFormatter import FileNameFormatter


def photo_task():
    logging.info("TechBeeCam task")
    cam = Photo(cam=Picamera2(), formatter=FileNameFormatter())
    file_path = cam.capture()
    mail = Mail()
    mail.send_photo(file_path)
    purger = Purger()
    purger.remove(file_path)


if __name__ == "__main__":
    logging.info("TechBeeCam starting ...")
    schedule.every(1).minutes.do(photo_task)

    while True:
        schedule.run_pending()
        time.sleep(1)
