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
## 3
## Copy and modify the previous exercise.
## Change the colors of each area in the dictionary to create your own color scheme.
## Change the title and question to ask the user for something other than their name.


## 4
## Use the example below and make changes to add a second dialog box to your previous code to
## tell the user the purpose of your program.
## Hint: place it above the `input_dialog` if you want it to run first and don't forget to
## update your import.

message_dialog(
    title=f"Calculator!!",
    text=f"This is a basic calculator that adds, subtracts, multiplies, and divides.",
    style=style).run()
```
<details><summary>Expand here for a simple calculator program using prompt_toolkit.</summary>
  
```python3
  
## Convert the basic calculator practical exercise to use functions and prompt_toolkit

from prompt_toolkit.shortcuts import button_dialog, input_dialog, message_dialog, yes_no_dialog
from prompt_toolkit.styles import Style


style=Style.from_dict({
    'dialog':             'bg:#2c66d3',
    'dialog frame.label': 'bg:#ffffff #000000',
    'dialog.body':        'bg:#000000 #00ff00',
    'dialog shadow':      'bg:#89827e',
    })

name = input_dialog(
    title='Username',
    text='Please type your name:', style=style).run()
message_dialog(
    title=f"{name}'s calculator!!",
    text=f"Greetings, {name}\nThis is a basic calculator that adds, subtracts, multiplies, and divides.", style=style).run()
dontstop = True

while dontstop == True:  
    firstnum = float(input_dialog(
        title=f"{name}'s input",
        text='Please type a number:', style=style).run())
    secondnum = float(input_dialog(
        title=f"{name}'s  second input",
        text='Please type another number:', style=style).run())
    operation = button_dialog(
        title='Operation',
        text=f'Choose an operation {name}?',
        buttons=[
            ('Add', 'sum'),
            ('Subtract', 'difference'),
            ('Multiply', 'product'),
            ('Divide', 'quotient')
        ], style=style
    ).run()
    if operation == 'sum':
        result = firstnum + secondnum
    elif operation == 'difference':
        result = firstnum - secondnum
    elif operation == 'product':
        result = firstnum * secondnum
    elif operation == 'quotient':
        result = firstnum / secondnum
    message_dialog(
            title=f"{name}'s Result",
            text=f"The {operation} is {result}", style=style).run()
    result = yes_no_dialog(
        title='Confirmation',
        text=f'Would you like to perform another calculation {name}?', style=style).run()
    if result == False:
        message_dialog(
            title='Exiting',
            text=f'Thank you for playing {name}, Goodbye', style=style).run()
        dontstop = False

  
```
</details>

### Input validation

Try this:

```python3
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt


class FunctionyValidator(Validator):
    def __init__(self, valfunc):
        self.valfunc = valfunc
        
    def validate(self, document):
        text = document.text
        valresult = self.valfunc(text)
        if valresult != "":
            raise ValidationError(message=valresult)

def between_2_and_5(x: str) -> str:
    try:
        numx = int(x)
    except:
        return "That's not a num."
    
    if 2 <= numx <= 5:
        return ""
    else:
        return "Must be between 2 and 5."

number = int(prompt('Give a number: ', validator=FunctionyValidator(between_2_and_5)))
print(f'You said: {number}')
```
