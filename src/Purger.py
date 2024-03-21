#!/usr/bin/env python
"""
Purger class
"""
# importing required modules 
import os
import datetime


class Purger:

    def __init__(self, path, ends_with, max_days):
        self.path = path
        self.ends_with = ends_with
        self.max_days = max_days

    # function to perform delete operation based on condition
    def purge_photos(self):
        for (root, dirs, files) in os.walk(self.path, topdown=True):
            for f in files:
                if not f.endswith(self.ends_with):
                    continue

                file_path = os.path.join(root, f)
                timestamp_of_file_modified = os.path.getmtime(file_path)
                modification_date = datetime.datetime.fromtimestamp(timestamp_of_file_modified)
                delta = (datetime.datetime.now() - modification_date)
                if delta.days > self.max_days:
                    print(f"    Delete : {f}, days old {delta.days}, max_days {self.max_days}")
                    os.remove(file_path)
                else:
                    print(f"!!! Do NOT Delete : {f}, days old {delta.days}, max_days {self.max_days}")


if __name__ == "__main__":
    # Run as a script
    x = Purger("./photos", ".jpg", 1)
    x.purge_photos()
