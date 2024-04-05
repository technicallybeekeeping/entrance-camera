import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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
                 smtp_server: str
                 ):
        self.enabled = enabled
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.smtp_port = smtp_port
        self.smtp_server = smtp_server

    def is_email_disabled(self):
        if (self.enabled != 1):
            logging.warning("Email is disabled. " +
                            "Please update the email credentials " +
                            "and enabled = 1 in config.py.")
            return False
        return True

    def send_photo(self, file_path: str, subject, body):
        if (self.is_email_disabled() is False):
            return

        body = body.format(ip_address=IPAddress.get())

        try:
            with open(file_path, 'rb') as f:
                part = MIMEImage(f.read())
                part.add_header('Content-ID', '<image>')
                file_name = os.path.basename(file_path)
                part.add_header('Content-Disposition', 'inline',
                                filename=file_name)
                msg = MIMEMultipart()
                msg['Subject'] = subject
                msg['From'] = self.sender_email
                msg['To'] = self.recipient_email
                html_part = MIMEText(body)
                msg.attach(html_part)
                msg.attach(part)

                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()
                    server.login(self.sender_email, self.sender_password)
                    server.send_message(msg)

        except Exception as ex:
            template = "Exception of type {0} occurred in Mail module." \
                + "Arguments:\n{1!r}"
            msg = template.format(type(ex).__name__, ex.args)
            logging.error(msg)

    def send_video(self, file_path, subject, body):
        if (self.is_email_disabled() is False):
            return

        body = body.format(ip_address=IPAddress.get())

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.recipient_email
        msg['Subject'] = subject

        # Attach body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file
        with open(file_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        f'attachment; filename= {file_path}')

        msg.attach(part)

        # Connect to SMTP server and send the email
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(msg)

    def send_ip_change(self, subject, body):
        if (self.is_email_disabled() is False):
            return

        body = body.format(ip_address=IPAddress.get())

        try:
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            html_part = MIMEText(body)
            msg.attach(html_part)

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

        except Exception as ex:
            template = "Exception of type {0} occurred in Mail module." \
                + "Arguments:\n{1!r}"
            msg = template.format(type(ex).__name__, ex.args)
            logging.error(msg)


if __name__ == "__main__":
    sut = Mail(config["mail"]["enabled"],
               config["mail"]["sender"],
               config["mail"]["app-password"],
               config["mail"]["recipient"],
               config["mail"]["port"],
               config["mail"]["server"])

    sut.send_ip_change("Test - " + config["mail"]["ip-changed"]["subject"],
                       "Test - " + config["mail"]["ip-changed"]["body"])

    sut.send_photo("../tests/artifacts/test-email-photo-1.jpeg",
                   "Test - " + config["mail"]["photo"]["subject"],
                   "Test - " + config["mail"]["photo"]["body"])

    sut.send_video("../tests/artifacts/test-video-1.mp4",
                   "Test - " + config["mail"]["video"]["subject"],
                   "Test - " + config["mail"]["video"]["body"])
