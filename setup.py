from src.Installer import Installer

if __name__ == "__main__":
    print("Starting Setup ...")

    installer = Installer()

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
            "Please enter your 19 character app password from Google: ",
            19,
            19)
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

    installer.clear_crontab()

    option = installer.get_photo_option_from_user()
    installer.schedule_photo_crontab(option)

    option = installer.get_video_option_from_user()
    installer.schedule_video_crontab(option)

    # reboot daily at 11:45 pm every day
    entry = '40 23 * * * ' + installer.get_base_command() + ' TaskReboot'
    installer.add_crontab_entry(entry)

    # Purge process nightly
    entry = '45 0 * * * ' + installer.get_base_command() + ' TaskPurge'
    installer.add_crontab_entry(entry)

    # Check for IP changes every 10 minutes on the 8s
    # entry = '8-58/10 * * * * ' + installer.get_base_command() + ' TaskCheckIP'
    # installer.add_crontab_entry(entry)

    # Schedule web app server
    entry = "@reboot cd ~/Desktop/entrance-camera/web/; " + \
            "sudo -E /usr/bin/python start_web_app.py"
    installer.add_crontab_entry(entry)

    installer.install_package("schedule")
    installer.install_package("Flask")
    installer.install_postfix()
