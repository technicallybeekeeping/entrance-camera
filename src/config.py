import logging
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
        "duration_secs": 300
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
"""
        },
        "video": {
            "subject": "BeeMail - Video 🐝 📫 🎥",
            "body": """
Here is your BeeMail! 🙌 
    Current IP address: {ip_address}
"""
        },

        "ip-changed": {
            "subject": "BeeMail - IP Changed 👀🚨",
            "body": """
The IP Address has changed. If you're using VNC, SSH, SCP, etc,
you'll want to change to this IP address:
    Current IP address: {ip_address}
"""
        }
    }
}

# Create the logs directory if it doesn't exist
logs_directory = '../logs'
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

# Configure logging
logging.basicConfig(level=logging.INFO,  # Set the logging level
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=os.path.join(logs_directory, 'app.log'),
                    filemode='a')  # Set the file mode to append

# Logging settings
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)
