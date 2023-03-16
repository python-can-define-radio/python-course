## Configuration

- Create a folder for yourself with your name (and no spaces) on the Desktop.
- In VSCode, open the folder that you created, and create a Python file to trigger the installation of the Python extension.
- Turn off Python auto import completions in VSCode. Ask the instructor how.
- Change the `TMOUT` variable in `.bashrc`. Details below.
- Disable middle-click if desired. Details in the `resources` directory.

## Things to know:

### How to change TMOUT:

- `echo -e '\n\nexport TMOUT=30000' >> ~/.bashrc` (this appends `export TMOUT=30000` at the end of the .bashrc file)
- Close all terminals so it'll take effect.

### Alternate approach to change TMOUT:

Run this Python:

```python3
f = open("/home/PUT_YOUR_USERNAME_HERE/.bashrc", "a")
f.write("\n\n")
f.write("export TMOUT=300000")
f.close()
```

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
