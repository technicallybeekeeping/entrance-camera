import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage




class BeeMail:
    def __init__(self):
        self.sender_email = "REDACTED"
        self.sender_password = "REDACTED"
        self.recipient_email = "REDACTED"
        self.subject = "Entrance Cam for Hive 1"
        self.body = "This is the body"

    def myfunc(self):
        print("Hello my name is " + self.subject)

    def sendImage(self, fileName):
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
                server.sendmail(self.sender_email, self.recipient_email, message.as_string())


p1 = BeeMail()
p1.sendImage("./photos/hive1.jpg")
