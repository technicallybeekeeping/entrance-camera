import logging


class IPAddressChecker:
    def __init__(self, ipaddress=None):
        self.IPAddress = ipaddress
        self.last_recorded = None

    def has_changed(self):
        current = self.IPAddress.get()
        if (self.last_recorded is None):
            # First reading, ignore
            self.last_recorded = current
            return False
        elif (self.last_recorded == current):
            return False
        logging.info("IP Address has changed" +
                     " from {self.last_recorded} to {current}")
        self.last_recorded = current
        return True


if __name__ == "__main__":
    from IPAddress import IPAddress
    sut = IPAddressChecker(ipaddress=IPAddress)
    result = sut.has_changed()
    print("Result of check = {result}")
