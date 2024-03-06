"""
Camera module for the Entrance
"""

import datetime as dt


class BeeCam:
    def __init__(self, cam=None):
        dateStr = dt.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        self.path = "./photos/basic_photo_1-" + "-" + dateStr + ".jpg"
        self.cam = cam

    def start_and_capture_file(self):
        try:
            self.cam.start_and_capture_file(self.path, show_preview=False)
        except:
            return False
        return True


#if __name__ == "__main__":
    # from picamera2 import Picamera2
    #beecam = BeeCam(cam=PiCamera2())
    #beecam.start_and_capture_file()