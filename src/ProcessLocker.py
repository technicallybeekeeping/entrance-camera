import fcntl
import os
import logging


class ProcessLocker:
    def __init__(self):
        self.lockfile = '/tmp/Application.lock'

    def acquire_lock(self):
        try:
            self.lock_fd = open(self.lockfile, 'w')
            fcntl.lockf(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.lock_fd.write(str(os.getpid()))
            self.lock_fd.flush()
            return True
        except IOError as ex:
            logging.error("Cannot acquire lock.", ex)
            return False

    def release_lock(self):
        if hasattr(self, 'lock_fd'):
            self.lock_fd.close()
            os.remove(self.lockfile)
