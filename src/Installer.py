from config import config
import os
import re
import subprocess
import logging


class Installer:
    def __init__(self):
        self.config_file = 'config.py'

    def get_valid_boolean_from_user(self, request):
        while True:
            user_input = input(request).strip().lower()
            if user_input in ['yes', 'no']:
                return 1 if user_input == 'yes' else 0
            else:
                print("Error: Invalid input. Please enter 'yes' or 'no'.")

    def get_valid_string_from_user(self, request, min, max):
        while True:
            user_input = input(request)
            if len(user_input) >= min and len(user_input) <= max:
                return user_input
            else:
                if (min == max):
                    print("Error: String length must be", min,
                          "characters long.")
                else:
                    print("Error: String length should be between", min,
                          "and", max, "characters.")

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def get_valid_email(self, request):
        while True:
            email = input(request).strip()
            if self.is_valid_email(email):
                return email
            else:
                print("Error: Invalid email address. " +
                      "Please enter a valid email.")

    def replace_strings(self, replacements):
        try:
            with open(self.config_file, 'r') as file:
                file_data = file.read()

            for pattern, replacement in replacements.items():
                file_data = re.sub(pattern, replacement, file_data)

            with open(self.config_file, 'w') as file:
                file.write(file_data)
            logging.info("Successfully update configuration.")
        except Exception as e:
            logging.Error("Error occurred while replacing strings:", e)

    def add_crontab_entry(self, entry):
        # Get current crontab entries
        process = subprocess.Popen(['crontab', '-l'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, _ = process.communicate()
        current_crontab = stdout.decode('utf-8')

        try:
            # Check if the entry already exists
            if entry not in current_crontab:
                # Add the new entry to the existing crontab
                new_crontab = current_crontab + entry + '\n'

                # Write the new crontab
                process = subprocess.Popen(['crontab', '-'],
                                           stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                process.communicate(input=new_crontab.encode('utf-8'))

                logging.info("Crontab entry added successfully.")
            else:
                logging.error("Crontab entry already exists.")
        except Exception as e:
            logging.error("Error occurred while modifying crontab:", e)

    def install_package(self, package):
        try:
            subprocess.check_call(["pip3", "install", package])

            logging.info(package + " package successfully installed.")
        except subprocess.CalledProcessError as e:
            logging.error("Error occurred while installing " + package, e)

    def check_and_change_directory(self):
        current_directory = os.getcwd()
        if os.path.basename(current_directory) != 'src':
            new_directory = "/Users/merpenbeck/src/techbee/entrance-camera/src"
            os.chdir(new_directory)
            logging.info(f"Changed directory to: {new_directory}")


if __name__ == "__main__":
    installer = Installer()
    # Example crontab entry to add (runs every minute)
    # entry_to_add = "* * * * * /path/to/your/command"

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
    entry = "@reboot cd /home/techbee/Desktop/entrance-camera/; " + \
            "sudo -E /usr/bin/python run_app_server.py"
    installer.add_crontab_entry(entry)
