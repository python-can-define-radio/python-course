<details><summary><i>Naming history (click to expand)</i></summary>
<pre>
2024 Feb 05: ex_2g_fun_features.md -- Accomodate moving of "ex_2f_modules_intro.md
2023 Jun 06: ex_2f_fun_fesatures.md -- Move & rename to organize the course.
</pre>
</details>

# Fun Features

This is an optional exercise that demonstrates some fun features.

### Delay printing

Source: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line

```python
import time

def delay_print(s):
    for c in s:
        print(c, end="", flush=True)
        time.sleep(0.25)

delay_print("hello world")
```

In fact, you can make everything delay printed if you'd like.

<details><summary>Expand this to see how:</summary>

```python3
import time

real_print = print
real_input = input
 
def print(s):
    for c in s:
        real_print(c, end="", flush=True)
        time.sleep(0.02)
    real_print("\n")
 
def input(s):
    for c in s:
        real_print(c, end="", flush=True)
        time.sleep(0.02)
    return real_input()

print("Notice that the normal print function has now been overridden.")
x = input("You can use input too.")
```
</details>

### Color output

#### Colors using `termcolor`

First, **in a terminal window**, run this:

```
pip3 install termcolor
```

Then, **in Python**, run this:

```python3
from termcolor import cprint

cprint("Hello, World!", "green", "on_white")
```

### Delay Printing combined with Color output

Note that the terminal in VS Code restricts the available colors to enforce readability. For example, `cprint("Hello, World!", "yellow", "on_light_red")` will display as a grey-black text color instead of yellow.

```python3
import time
from termcolor import colored

def delay_print(s):
    for c in s:
        print(colored(c, "blue", "on_red"), end="", flush=True)
        time.sleep(0.25)

delay_print("hello world")

```
For more examples, see the termcolor github page: https://github.com/termcolor/termcolor

#### Colors using `rich`

Another, more advanced library for formatting terminal output is `rich`. After running `pip install rich`, try this example (which was copied from https://rich.readthedocs.io/en/stable/tables.html):

<details><summary>Example of `rich` module (click to expand):</summary>

```python3

from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table) 
```
    
</details>
    
For more examples, see the [rich docs](https://rich.readthedocs.io).

### Dialog boxes in the terminal

After running `pip3 install prompt_toolkit`, try this:

```python3
from prompt_toolkit.shortcuts import input_dialog

text = input_dialog(
    title='Input dialog example',
    text='Please type your name:').run()

print(f"You said {text}.")
```

### Input validation

This one also uses prompt_toolkit.

```python3
from prompt_toolkit.validation import Validator
from prompt_toolkit import prompt
 
 
def options_validator(choices):
 
    def validate(text):    
        return text in choices
 
    validator = Validator.from_callable(
        validate,
        error_message=f"You may say: {choices}")
 
    return validator
 
 
 
def input_with_options(_prompt: str, options: list):
    print(_prompt + "\n")
    return prompt('> ', validator=options_validator(options))
 
 
resp = input_with_options("Yes or no?", options=["y", "n"])
print(f"You said {resp}")
animal = input_with_options("Cats or dogs?", options=["cats", "dogs"])
print(f"Ok, {animal}")
```

More info in the [prompt-toolkit docs](https://python-prompt-toolkit.readthedocs.io).

### Sounds

First, in a terminal, run this:

```
pip3 install playsound
```

Then, in Python, run this:

```
from playsound import playsound

playsound("You_must_pick_a_filename.mp3")
```
More info on audio processing in the [soundFile lesson](https://github.com/python-can-define-radio/python-course/blob/main/classroom_activities/Ch03_Misc_examples/soundFile.md)
