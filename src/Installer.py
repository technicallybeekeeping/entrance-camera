import re
import subprocess
import logging


class Installer:
    def __init__(self):
        self.config_file = 'src/config.py'

    def get_photo_option_from_user(self):
        while True:
            print("---")
            print("Please choose one of the following options:")
            print("0. Do not take still photos of the bees")
            print("1. Photograph the bees once a day")
            print("2. Photograph the bees every hour")

            choice = input("Enter your choice (0, 1, or 2): ")

            if choice in ['0', '1', '2']:
                return int(choice)
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
            print("")

    def get_video_option_from_user(self):
        while True:
            print("---")
            print("Please choose one of the following options:")
            print("0. Do not record video of the bees")
            print("1. Record the bees once a day")
            print("2. Record the bees every hour")

            choice = input("Enter your choice (0, 1, or 2): ")

            if choice in ['0', '1', '2']:
                return int(choice)
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
            print("")

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
            logging.error("Error occurred while replacing strings:", e)

    def clear_crontab(self):
        try:
            subprocess.run(["crontab", "-r"], check=True)
            print("Crontab cleared successfully.")
        except subprocess.CalledProcessError as e:
            print("Error:", e)

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

    def get_base_command(self):
        return 'cd ~/Desktop/entrance-camera/src/; /usr/bin/python Application.py'

    def schedule_photo_crontab(self, option):
        if option == 0:
            return
        elif option == 1:
            crontab_string = '30 12 * * * ' + self.get_base_command() + \
                " " + 'TaskPhoto'
        elif option == 2:
            crontab_string = '30 * * * * ' + self.get_base_command() + \
                " " + 'TaskPhoto'
        else:
            print("Invalid option. Please choose 0, 1, or 2.")
        self.add_crontab_entry(crontab_string)

    def schedule_video_crontab(self, option):
        if option == 0:
            return
        elif option == 1:
            crontab_string = '0 12 * * * ' + self.get_base_command() + \
                " " + 'TaskVideo'
        elif option == 2:
            crontab_string = '0 * * * * ' + self.get_base_command() + \
                " " + 'TaskVideo' # >> /path/to/logfile.log 2>&1
        else:
            print("Invalid option. Please choose 0, 1, or 2.")
        self.add_crontab_entry(crontab_string)

    def install_postfix(self):
        try:
            subprocess.run(['sudo', 'apt-get', 'install', 'postfix'], check=True)
            print("Postfix installed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error installing Postfix:", e)
