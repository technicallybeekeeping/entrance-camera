from src.Installer import Installer

if __name__ == "__main__":
    installer = Installer()

    installer.check_and_change_directory()

    enabled = installer.get_valid_boolean_from_user(
            "Do you want to enable email support? " +
            "'yes' or 'no': ")

    sender = "MODIFY-SENDER-EMAIL-ADDRESS"
    app_password = "MODIFY-APP-PASSWORD"
    recipient = "MODIFY-RECIPIENT-EMAIL-ADDRESS"

    if (enabled == 1):
        sender = installer.get_valid_email("Please enter your email address " +
                                           "(sender email address): ")
        app_password = installer.get_valid_string_from_user(
            "Please enter your 16 character app password from Google: ",
            16,
            16)
        recipient = installer.get_valid_email(
            "Please enter the email address receive email " +
            "(recipient email address): ")

    replacements = {
        r"\"enabled\": .*,": "\"enabled\": " + str(enabled) + ",",
        r"\"sender\": (.*)": "\"sender\": \"" + sender + "\",",
        r"\"app-password\": (.*)": "\"app-password\": \"" + app_password + "\",",
        r"\"recipient\": (.*)": "\"recipient\": \"" + recipient + "\","
    }
    installer.replace_strings(replacements)

    installer.install_package("schedule")
    installer.install_package("Flask")

    entry = "@reboot cd /home/techbee/Desktop/entrance-camera/src/; " + \
            "sudo -E /usr/bin/python TechBeeCam.py"
    installer.add_crontab_entry(entry)
    entry = "@reboot cd /home/techbee/Desktop/entrance-camera/web/; " + \
            "sudo -E /usr/bin/python start_web_app.py"
    installer.add_crontab_entry(entry)
