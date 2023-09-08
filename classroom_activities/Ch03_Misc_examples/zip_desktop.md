This is a GNU/Linux script to zip your Desktop folder and serve it.

1. Look up your ip address using `ip a`
2. Run the script below (running one-line-at-a-time is a good idea for self-education)
3. Afterwards, you can delete if you want

```sh
cd ~
zip -r Desktop.zip Desktop
cd Desktop
mkdir served_folder
cd ..
mv Desktop.zip Desktop/served_folder/
cd Desktop/served_folder
python3 -m http.server
```
