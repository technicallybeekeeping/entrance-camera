import logging
from config import config
from Photo import Photo
from Mail import Mail
from picamera2 import Picamera2
from FileNameFormatter import FileNameFormatter
from Application import Application


def run():
    logging.info("Task Photo starting ...")
    if not Application.is_daylight_hours():
        return

    cam1 = Picamera2()
    formatter1 = FileNameFormatter()
    cam = Photo(cam=cam1,
                formatter=formatter1,
                path=config["photos"]["path"])
    file_path = cam.capture()

    mailer = Mail(config["mail"]["enabled"],
                  config["mail"]["sender"],
                  config["mail"]["app-password"],
                  config["mail"]["recipient"],
                  config["mail"]["port"],
                  config["mail"]["server"])

    mailer.send_photo(file_path,
                      config["mail"]["photo"]["subject"],
                      config["mail"]["photo"]["body"])

    logging.info("Task Photo complete.")


if __name__ == "__main__":
    run()
