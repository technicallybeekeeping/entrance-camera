pip install schedule
pip install Flask

crontab -l | { cat; echo "@reboot cd /home/techbee/Desktop/entrance-camera/src/; sudo -E /usr/bin/python TechBeeCam.py"; } | crontab -
crontab -l | { cat; echo "@reboot cd /home/techbee/Desktop/entrance-camera/; sudo -E /usr/bin/python run_app_server.py"; } | crontab -

/usr/bin/thonny /home/techbee/Desktop/entrance-camera/src/config.py

