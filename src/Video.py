import logging


class Video:
    def __init__(self, cam=None, formatter=None):
        name = formatter.get_file_name()
        self.path = "../videos/" + name + ".mp4"
        self.cam = cam

    def capture(self):
        try:
            logging.info("path=" + self.path)
            self.cam.start_and_record_video(self.path, duration=5)
            logging.info("Capture successful: " + self.path)
            return self.path
        except Exception as ex:
            template = "Exception of type {0} occurred in Video capture." \
                + "Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logging.error(message)
            return None
        finally:
            self.cam.close()


if __name__ == "__main__":
    from picamera2 import Picamera2
    from FileNameFormatter import FileNameFormatter
    sut = Video(cam=Picamera2(), formatter=FileNameFormatter())
    sut.capture()
