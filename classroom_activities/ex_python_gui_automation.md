The following Python program will automatically input keypresses. I don't recommend running it directly, rather, you can modify the example to your own needs.

Remember to install pyautogui beforehand by running `pip install pyautogui` in a Terminal.

```python3
import pyautogui
import time



def forwardAndMoveSelectedEmailInOutlookWebApp(addressToSendTo, folderToMoveTo):
    ## 'Forward' 
    pyautogui.hotkey('ctrl', 'shift', 'f')
    time.sleep(4)

    ## 'To' is active. Type address.
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


print("NOTE: SORT OLDEST FIRST! HAVE THE FIRST EMAIL SELECTED!")
delay = 10
print(f"Giving you {delay} seconds to open the window before starting...")
## Give time to open the window
time.sleep(delay)

for count in range(3):
    forwardAndMoveSelectedEmail("jdoe@example.com", "folderToMoveTo")
```
