import socket
import datetime as dt
import logging


class FileNameFormatter:
    def __init__(self):
        self.hostName = socket.gethostname()

    def get_file_name(self):
        dateStr = dt.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        result = self.hostName + '-' + dateStr
        logging.info("result = " + result)
        return result


if __name__ == "__main__":
    sut = FileNameFormatter()
    result = sut.get_file_name()
    print("result -> " + result)
