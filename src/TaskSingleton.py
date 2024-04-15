import logging
import os
import signal
import subprocess


class TaskSingleton:
    def __init__(self, script_path):
        self.script_path = script_path
        self.lock_file = script_path + ".lock"

    def kill_previous_instance(self):
        # Check if the lock file exists
        if os.path.exists(self.lock_file):
            # Read the process ID from the lock file
            with open(self.lock_file, 'r') as file:
                pid = int(file.read().strip())

            try:
                os.kill(pid, 0)
                logging.info(
                    "Previous instance is running (PID: {})".format(pid))
                os.kill(pid, signal.SIGTERM)
                logging.info("Terminated previous instance.")
            except OSError as ex:
                logging.error("Cannot kill existing process.", ex)
                pass

    def run_script(self):
        # Write the current process ID to the lock file
        with open(self.lock_file, 'w') as file:
            file.write(str(os.getpid()))

        # Run the script
        subprocess.call(["python3", self.script_path])

        # Remove the lock file after the script finishes
        os.remove(self.lock_file)
