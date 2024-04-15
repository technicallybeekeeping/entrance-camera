from config import config
import logging
from Mail import Mail
from IPAddressChecker import IPAddressChecker
from IPAddress import IPAddress


def run():
    logging.info("Task Check IP starting...")
    ip_checker = IPAddressChecker(ipaddress=IPAddress)

    if ip_checker.has_changed():
        mailer = Mail(config["mail"]["enabled"],
                      config["mail"]["sender"],
                      config["mail"]["app-password"],
                      config["mail"]["recipient"],
                      config["mail"]["port"],
                      config["mail"]["server"],
                      config["mail"]["footer"])

        mailer.send_ip_change(
            config["mail"]["ip-changed"]["subject"],
            config["mail"]["ip-changed"]["body"])
    logging.info("Task Check IP complete.")


if __name__ == "__main__":
    run()
