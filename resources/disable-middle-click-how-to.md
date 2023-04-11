# How to disable middle click within the Linux operating system

This is useful when your mouse pointing device has a scroll wheel that performs as a middle button.  For example, when the wheel is pressed too firmly while rolling to scroll text, a 'paste' activity may occur uncepectedly, potentially adding some and deleting other text.

In the terminal program, type and press enter:

```
xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"
```

_NOTE: Throughout this document, after each command (e.g. "xmodmap....10", above), press the {Enter} key._

This will disable the middle click until you log out.

# How to make the change persistent

We want to put that command in an executable file, and then set it to run on login.

1. In the terminal, go to the Desktop, and make a file containing the commmand:  

   ```
   cd ~/Desktop
   fileContents='xmodmap -e "pointer = 1 25 3 4 5 6 7 8 9 10"'
   echo $fileContents > disable_middle_click.sh
   ```
NOTE: In the previous commands, be sure to have no spacing in: fileContents=

2. Set the file mode for that file to exectuable:  

   `chmod +x disable_middle_click.sh`

3. Set the new file to run at log-in:
     - Press the "Show Applications" button at lower left corner of OS window.
     - Search for "Startup Applications Preferences".  
       (You can do this by simply typing "startup..." and looking through the results that appear.)
     - Click "Add"
     - Enter these:
         - Name: Disable Middle Click
         - Command: _Click Browse, and navigate to the file on the Desktop_
         - Press the "Add" button to finalize and close the small window.
         - Press "close" to end the "Startup Applications Preferences" window.

7. Log-out and log-in to verify that it works.

---------------

## If you wish to re-enable middle click:

```
xmodmap -e "pointer = 1 2 3 4 5 6 7 8 9 10"
```
