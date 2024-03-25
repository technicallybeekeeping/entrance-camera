import logging

config = {
    "photos": {
        "path": "../photos",
        "ends_with": "jpg",
        "max_days_alive": 1
    },
    "videos": {
        "path": "../videos",
        "ends_with": "mp4",
        "max_days_alive": 1
    },
    "mail": {
        "sender": "MODIFY-SENDER-EMAIL-ADDRESS",
        "app-password": "MODIFY-APP-PASSWORD",
        "recipient": "MODIFY-RECIPIENT-EMAIL-ADDRESS",
        "port": 465,
        "server": "smtp.gmail.com",
        "subject": "BeeMail 🐝 📫",
        "body": "Here is your BeeMail! 🙌"
    }
}

# Logging settings
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)
