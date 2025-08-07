# Preliminaries

## Day One Breakdown

### Prerequisites

- Login to CVTE thin client
- Create Ubuntu VM
- Login to Ubuntu VM
- Change student passwords

_Note: At any point, if you have extra time, work on this [FreeCodeCamp tutorial](https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-string-manipulation-by-building-a-cipher/step-1) or go and explore these [resources](https://github.com/python-can-define-radio/python-course/tree/main/resources)_.

[Daily Schedule of Events](https://github.com/python-can-define-radio/python-course/blob/main/resources/toc-python.md)
  
<details><summary>Introductions. (Expand for details)</summary>
  
      - Name?
      
      - Where you're from?
        
      - Any IT experience?
        
      - Anything interesting about yourself you would like to share?
        
      - What you expect from this course?
        
        
</details>

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

<!--- <details><summary>Link your computer to the student samba. (Expand for details)</summary>
  
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
</details>  --->

<details><summary>Demonstrate the keyboard shortcuts. (Expand for details)</summary>
  
### Common VS Code and Thonny keyboard shortcuts:

- `Ctrl /` (VS Code), `Ctrl 3` (Thonny): toggle comment / uncomment  (while lines are selected)
- `Home`: Cursor to beginning of line
    - `Ctrl Home`: Cursor to the beginning of the file
- `End`: Cursor to end of line
    - `Ctrl End`: Cursor to the end of the file
- `Shift arrowkey`: Highlight forward/backward/up/down
- `Ctrl arrowkey`: Move cursor by words
- `Ctrl + Shift + arrowkey`: Hightlight a word at a time
- `Ctrl D` (VS Code only): Select multiple instances (powerful but advanced feature)
- `Ctrl Y`: Redo
- `Alt ↑`: Moves the line the cursor is on up one line
- `Alt ↓`: Moves the line the cursor is on down one line
- `Alt Z` (VS Code only): Toggles wordwrap
- `Ctrl Shift Space` (VS Code only): Toggles Parameter hints
  - If shortcut does not work navigate to File>Preferences>Settings
  - Type in parameter hints and uncheck ☑️`Editor › Parameter Hints: Enabled`
- `F5`: Runs code. Default in Thonny, needs config in VS Code (see below)

- <details><summary>Common to other text editors (Expand for details)</summary>

  ### Common
    
    - `Ctrl S`: Saves current file  
    - `Ctrl A`: Select all  
    - `Ctrl X`: Cut  
    - `Ctrl C`: Copy  
    - `Ctrl V`: Paste  
    - `Ctrl Z`: Undo  
    - `Backspace`: Erase to the left  
    - `Delete`: Erase from the right  
    
- <details><summary>Creating your own VSCode keyboard shortcut to run Python (Expand for details)</summary>

  ### Instructions
  
    - There are two methods for opening the keyboard shortcut menu
      - Ctrl + K + S
      - Ctrl + Shift + P then after the > type `Open Keyboard Shortcuts`
    - Type `Python: Run Python File` in the search field
    - Click the + next to Python: run python file
    - Enter the desired keyboard shortcut
      - ⚠️ Caution: you should verify that the keyboard shortcut you want to use is not already in use

</details>
</details>
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

<details><summary>Ways to save your work (Expand for details)</summary>

### Mailo

[Mailo](https://www.mailo.com/) is an email and cloud storage provider. You can create an account without a pre-existing email / phone, and then either send your files in an email, or upload them to Mailo's cloud drive. 

### Proton mail

[Proton](https://proton.me/mail/) is an email provider. You can create an account without a pre-existing email / phone, and then send your files in an email.
### Github 
    
We use Github to host many of our Python and SDR lessons. You can create a [Github account](https://github.com) to store your files if you wish. For more information on Github Accounts, see [here](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account).

</details>

<details><summary>Using the Debugger (Expand for details)</summary>  

### Instructions    
    
The debugger is useful for watching your code as it runs. Thonny's debugger is particularly useful, as it evaluates individual steps within a line of code.

To debug in Thonny, press `Ctrl` + `F5`.

To debug in VS Code, place a breakpoint (a red dot; ask an instructor to demonstrate) on a the line of code on which you'd like to begin debugging (the first line if you aren't sure), and then press `F5`.

For more information on debugging in Thonny, see the [Thonny homepage](https://thonny.org/), or ask an instructor.

For a short video on debugging with Thonny go [here](https://www.youtube.com/watch?v=QQAqQp06nXo).

</details>
