GUI automation is useful for a variety of tasks. For example, you may need a computer to stay awake, but you may not have access to change the time until it auto-locks.

One module for such tasks is pyautogui. You'll need to first install pyautogui beforehand by running `pip install pyautogui` in a Terminal.

Here's a basic example that simply moves the mouse 5 pixels to the right (relative to its current position):

```python3
import pyautogui

pyautogui.moveRel(5, 0)
```

A more interesting example could be a mouse-mover that keeps the computer awake:

```python3
import pyautogui
import time

while True:
    print("moving now!")
    pyautogui.moveRel(1, 0)
    pyautogui.moveRel(-1, 0)
    time.sleep(1)
```

## Another example...

The following Python program will automatically input keypresses to control the Outlook Web App. I don't recommend running it directly, rather, you can modify the example to your own needs.



```python3
""" 'py_gui_email_forwarding.py' from a MS Outlook-based e-mail account.
May 25, 2023
INSTRUCTIONS:
1. Update the variables in 'PARAMETERS to be updated...", below.
2. Sign-in to your MS Outlook-based e-mail account in a web browser at office.com or 
   using another appropriate website.
3. Run this python program.  It will ask you to ensure you want to proceed.
    a. After you press 'y' to proceed, there will be a 10 seconds delay. 
    b. Within the delay, activate the e-mail window by mouse-touching 
       the very e-mail you want to move.

Info: 
In the Main Body of Program, if the line "for count in range(quantity):" is a commented, 
only a single e-mail will be forwarded

from: https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch02_Advanced/10_python_gui_automation.md
"""

import pyautogui
import time

"""PARAMETERS to be updated by user:"""
# Change to match your intended destination e-mail acct.:
to_email = "e-mail-name@company.domain"  
# State a folder (existing or not) in the SOURCE("From") e-mail acct.: 
from_doneFolder = "MovedToOtherAcct"  # e-mails will be moved here.  E.g., "Deleted"
quantity = 1  # Enter here the number of messages you want to move.


def forwardAndMoveSelectedEmailInOutlookWebApp(addressToSendTo, folderToMoveTo):
    """This performs like a macro, runing key-board-equivalent commands for Outlook."""

    ## 'Forward' the selected e-mail (Selected by user's pointing to it with mouse.) 
    pyautogui.hotkey('ctrl', 'shift', 'f')
    time.sleep(4)

    ## 'To' field is active. Type address.
    pyautogui.write(addressToSendTo, interval=0.05)
    time.sleep(2)

    ## Press Enter to pick the address
    pyautogui.press('enter')
    time.sleep(1)

    ## Move the cursor to the body so that we can send
    pyautogui.press('tab')
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(1)

    ## 'Send' shortcut
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(4)

    ## 'Move to folder'
    pyautogui.press('v')
    time.sleep(2)

    pyautogui.write(folderToMoveTo, interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)


print("""
NOTES:
- SORT OLDEST FIRST!
- HAVE THE FIRST EMAIL SELECTED!
- Consider disabling "thread" or "conversation" view -- try both ways and see which you prefer.
""")
saidSomething = input("Continue? (y|N)...").lower()
if saidSomething != "y":
    import sys
    sys.exit()
    
delay = 10
print()
print(f"Giving you {delay} seconds to open the window before starting.")
print("If you aren't ready, Ctrl+C to exit now.")
for i in range(delay, 0, -1):
    print(i)
    time.sleep(1)

for count in range(1, quantity+1):  # Repeat for each e-mail to be moved.
    forwardAndMoveSelectedEmailInOutlookWebApp(to_email, from_doneFolder)
```
