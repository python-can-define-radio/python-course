rm ~/*.py
rm ~/Desktop/*.py
rm ~/Desktop/*/*.py
rm ~/Desktop/*/*/*.py
rm ~/*.pyc
rm ~/Desktop/*.pyc
rm ~/Desktop/*/*.pyc
rm ~/Desktop/*/*/*.pyc
rmdir ~/__pycache__
rmdir ~/Desktop/__pycache__
rmdir ~/Desktop/*/__pycache__
rmdir ~/Desktop/*/*/__pycache__

dconf reset -f /org/gnome/shell/extensions/dash-to-dock/


echo "TODO: add some stuff to favorites, etc"
