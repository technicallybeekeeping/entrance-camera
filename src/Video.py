import logging


class Video:
    def __init__(self, cam=None, formatter=None, path=None):
        name = formatter.get_file_name()
        self.path = path + name + ".mp4"
        self.cam = cam

    def capture(self, duration):
        try:
            logging.info("path=" + self.path)
            self.cam.start_and_record_video(self.path, duration=duration)
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
    from config import config

    sut = Video(cam=Picamera2(),
                formatter=FileNameFormatter(),
                path=config["videos"]["path"])
    sut.capture(config["videos"]["duration_secs"])
