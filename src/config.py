import logging
from logging.handlers import TimedRotatingFileHandler
import os

config = {
    "photos": {
        "path": "../photos/",
        "ends_with": "jpg",
        "max_days_alive": 1
    },
    "videos": {
        "path": "../videos/",
        "ends_with": "mp4",
        "max_days_alive": 1,
        "duration_secs": 30
    },
    "mail": {
        "enabled": 0,
        "sender": "MODIFY-SENDER-EMAIL-ADDRESS",
        "app-password": "MODIFY-APP-PASSWORD",
        "recipient": "MODIFY-RECIPIENT-EMAIL-ADDRESS",
        "port": 587,
        "server": "smtp.gmail.com",
        "photo": {
            "subject": "BeeMail - Photo 🐝 📫 📸",
            "body": """
Here is your BeeMail! 🙌 
    Current IP address: {ip_address}

<hr>
<p style="color: orange;">Brought to you by</p>
<a href="https://technicallybeekeeping.com" style="text-decoration: none; color: #333;">Technically Beekeeping, LLC</a>
<p style="color: orange;">Happy Beekeeping! 🌼🍯 Enjoy the journey! 🐝</p>

"""
        },
        "video": {
            "subject": "BeeMail - Video 🐝 📫 🎥",
            "body": """
Here is your BeeMail! 🙌 
    Current IP address: {ip_address}

<hr>
<a href="https://technicallybeekeeping.com" style="color: orange;">Brought to you by</a>
<a href="https://technicallybeekeeping.com" style="text-decoration: none; color: #333;">Technically Beekeeping, LLC</a>
"""
        },

        "ip-changed": {
            "subject": "BeeMail - IP Changed 👀🚨",
            "body": """
The IP Address has changed. If you're using VNC, SSH, SCP, etc,
you'll want to change to this IP address:
    Current IP address: {ip_address}

<hr>
<a href="https://technicallybeekeeping.com" style="color: orange;">Brought to you by</a>
<a href="https://technicallybeekeeping.com" style="text-decoration: none; color: #333;">Technically Beekeeping, LLC</a>
"""
        }
    }
}

# Create the logs directory if it doesn't exist
logs_directory = '../logs'
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)


# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler with timed rotation (daily)
file_handler = TimedRotatingFileHandler(os.path.join(
    logs_directory, 'app.log'),
    when='midnight',
    interval=1,
    backupCount=30)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(file_handler)


# # Create a handler to log to the command line
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.setLevel(logging.INFO)  # Set the logging level for the console handler
# console_handler.setFormatter(logging.Formatter(
#     '%(asctime)s - %(levelname)s - %(message)s'))
# logging.getLogger().addHandler(console_handler)
