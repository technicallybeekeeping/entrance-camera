import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)


config = {
    "mail": {
        "sender": "MODIFY-SENDER-EMAIL-ADDRESS",
        "app-password": "MODIFY-APP-PASSWORD",
        "recipient": "MODIFY-RECIPIENT-EMAIL-ADDRESS",
        "port": 465,
        "server": "smtp.gmail.com",
        "subject": "BeeMail",
        "body": "Here is your BeeMail!"
    }
}
