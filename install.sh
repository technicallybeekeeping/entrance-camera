pip install schedule

crontab -l | { cat; echo "@reboot cd /home/techbee/Desktop/entrance-camera/src/; sudo -E /usr/bin/python TechBeeCam.py"; } | crontab -

/usr/bin/thonny /home/techbee/Desktop/entrance-camera/src/config.py