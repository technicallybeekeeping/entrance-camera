import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class EMail:
    def __init__(self,
                 sender_email: str,
                 sender_password: str,
                 recipient_email: str,
                 subject: str,
                 body: str):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.subject = subject
        self.body = body

    def sendPhoto(self, fileName: str):
        with open(fileName, 'rb') as f:
            image_part = MIMEImage(f.read())
            message = MIMEMultipart()
            message['Subject'] = self.subject
            message['From'] = self.sender_email
            message['To'] = self.recipient_email
            html_part = MIMEText(self.body)
            message.attach(html_part)
            message.attach(image_part)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email,
                                self.recipient_email,
                                message.as_string())


if __name__ == "__main__":
    p1 = EMail("REDACTED",
                "REDACTED",
                "REDACTED",
                "This is the subject",
                "This is the body")
    
    p1.sendPhoto("./photos/hive1.jpg")
