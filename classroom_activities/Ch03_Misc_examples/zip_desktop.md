This is a GNU/Linux script to zip your Desktop folder and serve it using the terminal.

1. Look up your ip address using `ip a` in a terminal window. Write it down or remember it.
2. Run the script below (running one-line-at-a-time is a good idea for self-education)

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

3. Go to the other classroom and access your ip address from above using port :8000 to download your material.
4. Go back to the original classroom, stop the server, and log off.
