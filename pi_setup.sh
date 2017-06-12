#!/bin/bash

################################################
### Script to install all necessary programs and tools for the raspberry pi 
### Be sure to ensure all repositories are up to date
################################################

VENV="py3env"
REQ="requirements.txt"

### Pi config

# Rotate screen - instructions taken from http://michaelteeuw.nl/post/83188136918/magic-mirror-part-v-installing-the-raspberry-pi
# The ‘BIOS’ settings of the Raspberry Pi are stored in the /boot partition of the system. This partition contains a config.txt file with all the settings. To rotate the monitor, add the following line to this file:
# ```display_rotate=1```
# For a more reliable connection to the monitor, I’ve uncommented the line that enables HDMI hotplugging:
# ```hdmi_force_hotplug=1```

#  To disable screensaver, edit the following file in the new Raspian version: /etc/xdg/lxsession/LXDE-pi/autostart

 # @xscreensaver -no-splash
# Additionally, add the following lines:

# @xset s off
# @xset -dpms
# @xset s noblank
# @chromium --kiosk --incognito http://localhost
# This completely disables all screensaving features, and makes sure chromium will start after boot an points to the localhost webserver in full screen mode.



### Packages and tools

# Install chromium browser
#sudo apt-get install chromium x11-xserver-utils unclutter

# Install virtual env
sudo apt-get install python-virtualenv
# Use python3
virtualenv -p /usr/bin/python3 $VENV
. $VENV/bin/activate
# Install all requirements as specified by $REQ
sudo pip install $REQ

deactivate