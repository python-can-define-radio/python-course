# Preliminaries

## Day One Breakdown
These instructions assume you are working on a Linux operating system (OS).

<details><summary>Create student login accounts. (Expand for details)</summary>
<br/>
    
_Note: At any point, if you have extra time, work on this [FreeCodeCamp tutorial](https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-string-manipulation-by-building-a-cipher/step-1)._

  1. Insert ID card.

  2. In the browser, go to the registration page that the instructors will provide.

  3. If requested, type your PIN.

  4. Click "Create account" at the bottom of the screen. Note that it takes about 10 seconds to create (and gives no indication of loading), so press ONLY ONCE.

  5. Let the instructor know if you have any error messages. If it sucessfully created the account, then move on to the next step.

  6. It should show you a username and password. Remember or write down the username; copy the password to the clipboard.

  7. Click on the first link available, which will take you to a login page.

  8. In the new tab that opens, enter your username and password from the first tab.

  9. Set a new password. The password must be at least 20 characters.

  10. It should show a screen that has many details about your newly-created account. Click the menu in the top right that shows your name, and click log out.

  11. Close the browser.

  12. Log out of the computer. Log in with your account that you just created.

  Instructors will submit tickets as necessary using Slack.
  </details>
  
<details><summary>Introductions. (Expand for details)</summary>
  
      - Name?
      
      - Where you're from?
        
      - Any IT experience?
        
      - Anything interesting about yourself you would like to share?
        
      - What you expect from this course?
        
      - Is your account working?
        
</details>

[Daily Schedule of Events](https://github.com/python-can-define-radio/python-course/blob/main/resources/toc-python.md)

<details><summary>Initial VS Code setup. (Expand for details)</summary>

  1. Create a folder for yourself with your name (and no spaces) on the Desktop.
     
  2. Open VS Code. (Right-click and `add to favorites` if you want it on your sidebar.)
     
  3. Create a Python file to trigger the installation of the Python extension.
     
  4. Connect VS Code to that folder.  
    - file>open folder  
    - navigate to the folder you just created on the Desktop  
    - open
  5. Close VS Code.
</details>

<details><summary>Link your computer to the student samba. (Expand for details)</summary>
  
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

<details><summary>Follow these directions to run the student setup script. (Expand for details)</summary>
  
  1) Right-click on this [student_config_script.sh](https://raw.githubusercontent.com/python-can-define-radio/python-course/main/resources/student_config_script.sh)  and select `Save Link As`.
    
  2) For the save location, click on `Desktop` on the left, and then click `Save`.
  
  3) Minimize the browser window so that you can see the Desktop.
  
  4) Right-click on your Desktop and select `Open in Terminal`.
     
  5) Type `bash student_config_script.sh` and hit Enter.
     
  6) Let the instructor know if you see any error messages.
   
  7) <details><summary>This is what the script does. Expand</summary>
      
      - adds term_example_files folder to the desktop.  
      - adds python_slideshows folder to the desktop.  
      - adds sdr_slideshows folder to the desktop.  
      - adds rich_presentaions folder to the desktop.  
      - sets up some basic VSCode and computer configuration settings.
        
      </details>
8) <details><summary>Expand here for Manual instructions if the script does not work.</summary>

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

<details><summary>Demonstrate the keyboard shortcuts. (Expand for details)</summary>
  
### Common VS Code and Thonny keyboard shortcuts:

- `Ctrl /` (VS Code), `Ctrl 3` (Thonny): toggle comment / uncomment  (while lines are selected)
- `Home`: Cursor to beginning of line
    - `Ctrl Home`: Cursor to the beginning of the file
- `End`: Cursor to end of line
    - `Ctrl End`: Cursor to the end of the file
- `Shift arrowkey`: Highlight forward/backward/up/down
- `Ctrl arrowkey`: Move cursor by words
- `Ctrl D` (VS Code only): Select multiple instances (powerful but advanced feature)
- `Ctrl Y`: Redo
- `Alt ↑`: Moves the line the cursor is on up one line
- `Alt ↓`: Moves the line the cursor is on down one line
- `Alt Z` (VS Code only): Toggles wordwrap
- `Ctrl Shift Space` (VS Code only): Toggles Parameter hints
  - If shortcut does not work navigate to File>Preferences>Settings
  - Type in parameter hints and uncheck ☑️`Editor › Parameter Hints: Enabled`
- `F5`: Runs code. Default in Thonny, needs config in VS Code (see below)
- Common to other text editors
  - `Ctrl S`: Saves current file
  - `Ctrl A`: Select all
  - `Ctrl X`: Cut
  - `Ctrl C`: Copy
  - `Ctrl V`: Paste
  - `Ctrl Z`: Undo
  - `Backspace`: Erase to the left
  - `Delete`: Erase from the right
</details>

<details><summary>Icons (Expand for details)</summary>

### VS Code Icons

- 📁 The file browser icon (`nuff said)
- 🔍 Use the magnifying glass on the left hand side of VS Code to search within multiple files.
- 🎛️ The source control icon allows you to keep your files up to date with a remote repository.
- 🐛 The run and debug icon is used for troubleshooting.
- 🪟 The extensions icon is used to install additional extensions to improve your VS Code experience.

### Icons in the python-can-define-radio lessons
    
👨🏽‍🏫 = <b>Discussion/Lecture  
🧠 = PE/Exam  
🔬 = Independent Work Time/Experimentation  
✎ = User input follows</b>

</details>

<details><summary>We will be using Github for many of our Python and SDR lessons. (Expand for details)</summary>

  1) If you want, you may [create a free GitHub account](https://github.com).
  
  2) This will give you a repository in which you can save your work.
  
  3) For more information on Github Accounts:https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account
</details>
