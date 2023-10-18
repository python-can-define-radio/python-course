# The prompt_toolkit module  

The goal of the current lesson is to familiarize new students with the "prompt_toolkit" module of python.

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