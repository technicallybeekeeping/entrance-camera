import socket


class IPAddress:
    @staticmethod
    def get():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


if __name__ == "__main__":
    result = IPAddress.get()
    print(result)
