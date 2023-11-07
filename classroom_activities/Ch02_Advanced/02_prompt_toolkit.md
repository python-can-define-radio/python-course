# The prompt_toolkit module  

The goal of the current lesson is to familiarize new students with the "prompt_toolkit" module of python.  
For more information and tutorials go to the [prompt_toolkit docs](https://python-prompt-toolkit.readthedocs.io/en/master/pages/getting_started.html#getting-started).

### Notes: 
- You may need to install prompt_toolkit to begin.
  - `pip install prompt_toolkit` (from the terminal) 

### Exercises

<i>Exercise #1:</i>  
First, run this.
```python3
## 1

from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.styles import Style


style=Style.from_dict({
    'dialog':             'bg:#88ff88',
    'dialog frame.label': 'bg:#ffffff #000000',
    'dialog.body':        'bg:#000000 #00ff00',
    'dialog shadow':      'bg:#00aa00',
    })

name = input_dialog(
    title='Username',
    text='Please type your name:', style=style).run()
```

- When you run this it will make your terminal window act similar to a graphic user interface (GUI) and `style` the window with colors using their hex code.  
- Notice the `input_dialog` function this is one of many built-in functions for the prompt_toolkit module that provides you a title, a line of text, an input textbox, and ok and cancel buttons.
- Find more types of input [here](https://python-prompt-toolkit.readthedocs.io/en/master/pages/dialogs.html).

```python3
## 2
## Copy and modify the previous exercise.
## Change the colors of each area in the dictionary to create your own color scheme.
## Change the title and question to ask the user for something other than their name.


## 3
## Use the example below and make changes to add a second dialog box to your previous code to tell the user
## the purpose of your program.
## Hint: place it above the `input_dialog` if you want it to run first and don't forget to update your import.

message_dialog(
    title=f"Calculator!!",
    text=f"This is a basic calculator that adds, subtracts, multiplies, and divides.",
    style=style).run()


```
