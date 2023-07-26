#!/bin/bash -e

echo "- Setting screen blank timeout, lock timeout, and bash terminal timeout"
gsettings set org.gnome.desktop.session idle-delay 900
gsettings set org.gnome.desktop.screensaver lock-delay 1800
echo "

## Make TMOUT variable arbitrarily large to avoid terminal auto-closing
export TMOUT=30000" >> ~/.bashrc


echo "- Disabling middle click to avoid accidental pasting"
# this works for a single session only (non-persistent).
xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"

# the next part will disable middle-click on login (persistently).
## create a script that runs the command that we saw above
scriptFile=Desktop/disable_middle_click.sh
echo 'xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"' > ~/$scriptFile
## Mark the script as executable
chmod 770 ~/$scriptFile
## Make autostart directory
mkdir -p ~/.config/autostart
## Create a .desktop file which Ubuntu/GNOME auto-loads on login
echo "[Desktop Entry]
Type=Application
Name=run_disable_middle_click_script
X-GNOME-Autostart-enabled=true
Exec=$HOME/$scriptFile
" > ~/.config/autostart/disable_middle_click.desktop
