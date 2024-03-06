#!/usr/bin/env python
""" 
Purger class
"""
# importing required modules 
import os
import datetime

# Path to look for photos
PATH = "./photos"
INCLUDE_ENDS_WITH = ".jpg"
MAX_DAYS = 1


class Purger:
    # function to perform delete operation based on condition
    def purge_photos(path, endswith, max_days):
        # loop to check all files one by one
        # os.walk returns 3 things: current path, files in the current path, and folders in the current path
        for (root, dirs, files) in os.walk(path, topdown=True):
            for f in files:
                if not f.endswith(endswith):
                    continue
                # temp variable to store path of the file
                file_path = os.path.join(root, f)
                # get the timestamp, when the file was modified
                timestamp_of_file_modified = os.path.getmtime(file_path)
                # convert timestamp to datetime
                modification_date = datetime.datetime.fromtimestamp(timestamp_of_file_modified)
                # find the number of days when the file was modified
                delta = (datetime.datetime.now() - modification_date)
                if delta.days > max_days:
                    # remove file
                    print(f"    Delete : {f}, days old {delta.days}, max_days {max_days}")
                    os.remove(file_path)  
                else:
                    print(f"!!! Do NOT Delete : {f}, days old {delta.days}, max_days {max_days}")


if __name__ == "__main__":
    # call function
    x = Purger()
    x.purge_photos(PATH, INCLUDE_ENDS_WITH, MAX_DAYS)
