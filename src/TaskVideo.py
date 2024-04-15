import logging
from config import config
from Video import Video
from Mail import Mail
from picamera2 import Picamera2
from FileNameFormatter import FileNameFormatter
from Application import Application


def run():
    logging.info("Task Video starting ...")
    if not Application.is_daylight_hours():
        return

    cam1 = Picamera2()
    formatter1 = FileNameFormatter()
    cam = Video(cam=cam1,
                formatter=formatter1,
                path=config["videos"]["path"])
    file_path = cam.capture(config["videos"]["duration_secs"])

    mailer = Mail(config["mail"]["enabled"],
                  config["mail"]["sender"],
                  config["mail"]["app-password"],
                  config["mail"]["recipient"],
                  config["mail"]["port"],
                  config["mail"]["server"],
                  config["mail"]["footer"])

    mailer.send_video(file_path,
                      config["mail"]["video"]["subject"],
                      config["mail"]["video"]["body"])

    logging.info("Task Video complete.")


if __name__ == "__main__":
    run()
