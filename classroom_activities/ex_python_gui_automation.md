The following Python program will automatically input keypresses. I don't recommend running it directly, rather, you can modify the example to your own needs.

Remember to install pyautogui beforehand by running `pip install pyautogui` in a Terminal.

```python3
import pyautogui
import time



def forwardAndMoveSelectedEmailInOutlookWebApp():
    ## 'Forward' 
    pyautogui.hotkey('ctrl', 'shift', 'f')
    time.sleep(4)

    ## 'To' is active. Type address.
    pyautogui.write("jdoe@example.com", interval=0.05)
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

    pyautogui.write("autoforwarded", interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)



## Give time to open the window
time.sleep(5)

for count in range(3):
    forwardAndMoveSelectedEmailInOutlookWebApp()
```
