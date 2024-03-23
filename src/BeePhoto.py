"""
Camera module for the Entrance
"""
import logging


class BeePhoto:
    def __init__(self, cam=None, formatter=None):
        name = formatter.get_file_name()
        self.path = "../photos/" + name + ".jpg"
        self.cam = cam

    def capture_photo(self):
        try:
            logging.info("path=" + self.path)
            self.cam.start_and_capture_file(self.path, show_preview=False)
            logging.info("Capture successful: " + self.path)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logging.error(message)
            return False
        return True


if __name__ == "__main__":
    from picamera2 import Picamera2
    import FileNameFormatter
    sut = BeePhoto(cam=Picamera2(),formatter=FileNameFormatter())
    sut.capture_photo()
