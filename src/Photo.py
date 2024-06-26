import logging


class Photo:
    def __init__(self, cam=None, formatter=None, path=None):
        name = formatter.get_file_name()
        self.path = path + name + ".jpg"
        self.cam = cam

    def capture(self):
        try:
            logging.info("path=" + self.path)
            self.cam.start_and_capture_file(self.path, show_preview=False)
            logging.info("Capture successful: " + self.path)
            return self.path
        except Exception as ex:
            template = "Exception of type {0} occurred in Photo capture." \
                + "Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logging.error(message)
            return None
        finally:
            self.cam.close()


if __name__ == "__main__":
    from picamera2 import Picamera2
    from config import config
    from FileNameFormatter import FileNameFormatter
    sut = Photo(cam=Picamera2(),
                formatter=FileNameFormatter(),
                path=config["photos"]["path"])
    sut.capture()
