#!/bin/bash
#call this script from a desktop entry 
sudo virsh start VMname

until ssh username@ipaddress 
do
	echo "Attempting SSH connection to Virtual Machine..."
done

#Gnome desktop entry (/usr/share/applications)
#
# [Desktop Entry]
# Name=Virtual Machine Name
# Comment=VM
# Type=Application
# Exec=/bin/this_script.bash
# Icon=/path/to/icon.png
# Categories=Development
# Terminal=true
# StartupNotify=true
