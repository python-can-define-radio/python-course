# Preliminaries

## Day One Breakdown
These instructions assume you are working on a Linux operating system (OS).

- Create student login accounts if necessary.

- Introductions.

- [Daily Schedule of Events](https://github.com/python-can-define-radio/python-course/blob/main/resources/toc-python.md)

- Open VSCode, then close it.

- <details><summary>Link your computer to the student samba. (Expand for details)</summary>
  
  1) Open the file browser.  
  
  2) Click on `+ Other Locations` in the bottom left corner.
  
  3) At the bottom where it says `Enter server address`, type smb://`the url` (provided by the instructor) and hit Enter.
  
  4) Double-click on `studentsamba`.
  
  5) Select the `Registered User` radio button.
  
  6) Enter username and password (provided by the instructor).
  
  7) Select the `Forget password immediately` radio button.
  
  8) Click Connect.
  
  9) Close file browser. you are now linked to the studentsamba.

  10) Repeat as necessary if the `studentsamba` loses connection. 
</details>

- <details><summary>Follow these directions to run the student setup script. (Expand for details)</summary>
  
  1) Right-click on this [student_config_script.sh](https://raw.githubusercontent.com/python-can-define-radio/python-course/main/resources/student_config_script.sh)  and select `Save Link As`.
  
  2) For the save location, click on `Desktop` on the left, and then click `Save`.
  
  3) Minimize the browser window so that you can see the Desktop.
  
  4) Right-click on your Desktop and select `Open in Terminal`.
     
  5) Type `bash student_config_script.sh` and hit Enter.
     
  6) Let the instructor know if you see any error messages.
     
  7) <details><summary>Expand here for Manual instructions if the script does not work.</summary>

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
</details>  

- Create a folder for yourself with your name (and no spaces) on the Desktop.
  
- Reopen VSCode to the folder that you created.
  
- Create a Python file to trigger the installation of the Python extension.

- Demonstrate the keyboard commands below.
  
### Common VS Code keyboard shortcuts:

- `Ctrl /`: toggle comment / uncomment  (while lines are selected)
- `Home`: Cursor to beginning of line
- `End`: Cursor to end of line
- `Shift arrowkey`: Highlight forward/backward/up/down
- `Ctrl arrowkey`: Move cursor by words
- `Ctrl D`: Select multiple instances (powerful but advanced feature)
- `Ctrl Y`: Redo
- `Alt Z`: Toggles wordwrap
- `Ctrl Shift Space`: Toggles Parameter hints
  - If shortcut does not work navigate to File>Preferences>Settings
  - Type in parameter hints and uncheck ☑️`Editor › Parameter Hints: Enabled`
- Common to other text editors
  - `Ctrl S`: Saves current file
  - `Ctrl A`: Select all
  - `Ctrl X`: Cut
  - `Ctrl C`: Copy
  - `Ctrl V`: Paste
  - `Ctrl Z`: Undo
  - `Backspace`: Erase to the left
  - `Delete`:<details><summary>Erase to the right (Expand)</summary>
  
    Notes about `Delete`:
    - In the "Terminal" program, the cursor is a box.  The `Delete` key deletes the character inside the cursor box and pulls text from the RIGHT.
    - For many other programs, the cursor is a line that sits between two characters.  In this case, the {Delete} key deletes the character on the RIGHT side of the cursor and pulls text from the right.
  </details>

### VS Code Icons

- 📁 The file browser icon (`nuff said)
- 🔍 Use the magnifying glass on the left hand side of VS Code to search within multiple files.
- 🎛️ The source control icon allows you to keep your files up to date with a remote repository.
- 🐛 The run and debug icon is used for troubleshooting.
- 🪟 The extensions icon is used to install additional extensions to improve your VS Code experience.

### Misc

- <details><summary>We will be using Github for many of our Python and SDR lessons. (Expand for details)</summary>

  1) If you want, you may [create a free GitHub account](https://github.com).
  
  2) This will give you a repository in which you can save your work.
  
  3) For more information on Github Accounts:https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account
</details>
