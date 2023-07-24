## Configuration
These instructions assume you are working on a Linux operating system (OS).

- Create a folder for yourself with your name (and no spaces) on the Desktop.
- In VSCode, open the folder that you created.
- Create a Python file to trigger the installation of the Python extension.
- Follow these directions to run a setup script:
  - Right-click on this [student_config_script.sh](https://raw.githubusercontent.com/python-can-define-radio/python-course/main/resources/student_config_script.sh)  and select `Save Link As`.  
  - For the save location, click on `Desktop` on the left, and then click `Save`.
  - Minimize the browser window so that you can see the Desktop.
  - Right-click on your Desktop and select `Open in Terminal`.
  - Type `bash student_config_script.sh` and hit Enter.
  - Let the instructor know if you see any error messages.

<details><summary>Expand here for Manual instructions if the script does not work.</summary>

### How to change terminal timeout (TMOUT variable):

- Activate a Terminal program window in Linux OS.
- Type and run: `echo -e '\n\nexport TMOUT=30000' >> ~/.bashrc` (this appends `export TMOUT=30000` to the end of the .bashrc file)
- Verify that it changed the file using this command to view the file: `cat ~/.bashrc`
- Close all terminals so it'll take effect.

### Alternate approach to change TMOUT:

Run this Python:

```python3
f = open("/home/PUT_YOUR_USERNAME_HERE/.bashrc", "a")
f.write("\n\n")
f.write("export TMOUT=300000")
f.close()
```

### How to change OS screen timeout on Ubuntu:

In Settings, click the magnifying glass in the top left of the window and search `Screen Lock` and select it.
- Adjust the "Blank Screen" option. Recommended setting: 15 minutes.
- Adjust the "Automatic Screen Lock Delay". Recommended setting: 30 minutes.

### For instructions on how to disable middle click go to:
https://github.com/python-can-define-radio/python-course/blob/main/resources/disable-middle-click-how-to.md
</details>




### On the keyboard:

- `Ctrl /`: toggle comment / uncomment  (while lines are selected)
- `Backspace`: erase to the left
- `Delete`: erase to the right
- `Home`: Cursor to beginning of line
- `End`: Cursor to end of line
- `Shift arrowkey`: Highlight forward/backward/up/down
- `Ctrl arrowkey`: move cursor by words
- `Ctrl D`: select multiple instances (_powerful but advanced feature -- instructor will demo how to use_)

Notes about `Delete`:
- In the "Terminal" program, the cursor is a box.  The `Delete` key deletes the character inside the cursor box and pulls text from the RIGHT.
- For many other programs, the cursor is a line that sits between two characters.  In this case, the {Delete} key deletes the character on the RIGHT side of the cursor and pulls text from the right.
