import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import logging
from config import config
from IPAddress import IPAddress
import os


class Mail:
    def __init__(self,
                 enabled: int,
                 sender_email: str,
                 sender_password: str,
                 recipient_email: str,
                 smtp_port: int,
                 smtp_server: str,
                 subject: str,
                 body: str):
        self.enabled = enabled
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.smtp_port = smtp_port
        self.smtp_server = smtp_server
        self.subject = subject
        self.body = body

    def send_photo(self, file_path: str):
        if (self.enabled != 1):
            logging.warning("Email is disabled. " +
                            "Please update the email credentials " +
                            "and enabled = 1 in config.py.")
            return

        address = IPAddress.get()
        body = self.body.format(ip_address=address)

        try:
            with open(file_path, 'rb') as f:
                image_part = MIMEImage(f.read())
                image_part.add_header('Content-ID', '<image>')
                file_name = os.path.basename(file_path)
                image_part.add_header('Content-Disposition', 'inline',
                                      filename=file_name)
                message = MIMEMultipart()
                message['Subject'] = self.subject
                message['From'] = self.sender_email
                message['To'] = self.recipient_email
                html_part = MIMEText(body)
                message.attach(html_part)
                message.attach(image_part)
                with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                    server.login(self.sender_email, self.sender_password)
                    server.sendmail(self.sender_email,
                                    self.recipient_email,
                                    message.as_string())
        except Exception as ex:
            template = "Exception of type {0} occurred in Mail module." \
                + "Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logging.error(message)


if __name__ == "__main__":
    p1 = Mail(config["mail"]["enabled"],
              config["mail"]["sender"],
              config["mail"]["app-password"],
              config["mail"]["recipient"],
              config["mail"]["port"],
              config["mail"]["server"],
              "Test " + config["mail"]["subject"],
              "Test " + config["mail"]["body"])

    p1.send_photo("../tests/artifacts/test-email-photo-1.jpeg")
