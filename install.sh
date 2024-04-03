pip install schedule
crontab -l | { cat; echo "@reboot sudo /usr/bin/python /home/techbee/Desktop/entrance-camera/src/TechBeeCam.py"; } | crontab -