#!/usr/bin/env python
""" Script to remove files beyond a specific amount of time.
___ ____ ____ _  _ _  _ _ ____ ____ _    _   _   _   ___  ____ ____ _  _ ____ ____ ___  _ _  _ ____
 |  |___ |    |__| |\ | | |    |__| |    |    \_/    |__] |___ |___ |_/  |___ |___ |__] | |\ | | __
 |  |___ |___ |  | | \| | |___ |  | |___ |___  |     |__] |___ |___ | \_ |___ |___ |    | | \| |__]
                                                                                                      
This file is part of the Entrance Camera Basic distribution 
(https://github.com/technicallybeekeeping/entrance-camera-basic).

Copyright (c) 2024 Technically Beekeeping, LLC
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

Want to learn more?!? 
See https://www.youtube.com/@TechnicallyBeekeeping or https://technicallybeekeeping.com
"""
# importing required modules 
import os 
import datetime 


# Path to look for photos
PATH = "./photos"
INCLUDE_ENDS_WITH = ".jpg"
MAX_DAYS = 3

# function to perform delete operation based on condition 
def purge_old_photos(path, endswith, max_days): 
    # loop to check all files one by one 
    # os.walk returns 3 things: current path, files in the current path, and folders in the current path 
    for (root,dirs,files) in os.walk(path, topdown=True): 
        for f in files: 
            if not f.endswith(endswith):
                continue
            # temp variable to store path of the file 
            file_path = os.path.join(root,f) 
            # get the timestamp, when the file was modified 
            timestamp_of_file_modified = os.path.getmtime(file_path) 
            # convert timestamp to datetime 
            modification_date = datetime.datetime.fromtimestamp(timestamp_of_file_modified) 
            # find the number of days when the file was modified 
#            number_of_days = (datetime.datetime.now() - modification_date).days 
#            if number_of_days > max_days: 
            mins = (datetime.datetime.now() - modification_date).minutes
            if mins > max_days:
                # remove file 
                os.remove(file_path) 
                print(f" Delete : {f}") 

# call function 
purge_old_photos(PATH, INCLUDE_ENDS_WITH, MAX_DAYS)
