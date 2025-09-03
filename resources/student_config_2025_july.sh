rm ~/*.py
rm ~/Desktop/*.py
rm ~/Desktop/*/*.py
rm ~/Desktop/*/*/*.py

rm -r ~/__pycache__
rm -r ~/Desktop/__pycache__
rm -r ~/Desktop/*/__pycache__
rm -r ~/Desktop/*/*/__pycache__

dconf reset -f /org/gnome/shell/extensions/dash-to-dock/


echo "TODO: add some stuff to favorites, etc"
