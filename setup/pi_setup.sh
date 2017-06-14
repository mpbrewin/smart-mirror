#!/bin/bash

#########################################################
### Script to install all necessary programs and configure the raspberry pi for SmartMirror#
### Be sure to ensure all repositories are up to date
################################################

VENV="py3env"
REQ="requirements.txt"
PY3 = "/usr/bin/python3"
BOOT_CONF = "/boot/config.txt"
DISP_ROT="display_rotate=1"


### Pi config

# Rotate screen
# Add display_rotate=1 to /boot/config.txt (if not there already)
#if grep -q $DISP_ROT $BOOT_CONF
#then
#	echo "display already rotated"
#else
#	echo "display_rotate=1" >> $BOOT_CONF
#fi

# Uncommented the line that enables HDMI hotplugging:
# ```hdmi_force_hotplug=1```

#  To disable screensaver, comment the following file in the new Raspian version: /etc/xdg/lxsession/LXDE-pi/autostart
# To disable the blank screen at every startup, just update the /etc/lightdm/lightdm.conf file and add in the [SeatDefaults] section the following command:
# [SeatDefaults]
# xserver-command=X -s 0 -dpms

# @xscreensaver -no-splash
# Additionally, add the following lines:

# If getting black borders, uncomment disable_overscan=1 (make sure it's 1)

# @xset s off
# @xset -dpms
# @xset s noblank
# @chromium --kiosk --incognito http://localhost
# This completely disables all screensaving features, and makes sure chromium will start after boot an points to the localhost webserver in full screen mode.



### Packages and tools

# Install chromium browser
sudo apt-get install chromium-browser

# Install pip
sudo apt-get install python3-pip

# Install virtual env
sudo apt-get install python-virtualenv
# Use python3
virtualenv -p $PY3 $VENV
. $VENV/bin/activate
# Install all requirements as specified by $REQ
sudo pip install -r $REQ

deactivate