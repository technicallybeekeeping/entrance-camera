"""
Camera module for the Entrance
"""

import datetime as dt
import logging


class BeeCam:
    def __init__(self, cam=None):
        print("In BeeCam")
        dateStr = dt.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        self.path = "./photos/basic_photo_1-" + "-" + dateStr + ".jpg"
        self.cam = cam

    def start_and_capture_file(self):
        try:
            self.cam.start_and_capture_file(self.path, show_preview=False)
            logging.info("Capture successful: " + self.path)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logging.error(message)
            return False
        return True


#if __name__ == "__main__":
    # from picamera2 import Picamera2
    #beecam = BeeCam(cam=PiCamera2())
    #beecam.start_and_capture_file()