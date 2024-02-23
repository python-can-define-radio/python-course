from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.console import Console
from rich.markdown import Markdown
from guizero import App, Picture, Text
import tkinter as tk
from lec_03a_if_else import IMAGE_DATA



console = Console()
print = console.print
input = console.input
THEME = "zenburn"
APP = App(title="IF-Else Decision", width=850, height=500)

image = tk.PhotoImage(data=IMAGE_DATA)
picture = Picture(APP, image=image)
message = Text(APP, text="Close Window to go to the first example.")
APP.display()
layout = Layout()
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower"),
)
layout["upper"].ratio = 2


def md(*args, **kwargs):
    return Markdown(*args, code_theme=THEME, inline_code_theme=THEME, inline_code_lexer="python3", **kwargs)


def printwait(*args, **kwargs):
    print(*args, **kwargs)
    input()


console.clear()
################statevariable#datatype################

layout["upper"].update(Panel(md("""
```python3
num = input("What is your favorite number? ")
if 4:
    print("Four is my favorite number also.")
```
"""), title="[blue]Whats wrong with this Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel(md("There are actually two issues here.  \n\nThe first is that we are not converting the input variable `num` to a number, either `integer` or `float`.  \nThe second is that `if 4:` is equivalent to saying `if 4 != 0`.  \nThat would always print because 4 is never equal to 0.  \nThe correct usage would be to state your variable and use a valid comparison operator."), title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["upper"].update(Panel(md("""
```python3
num = input("What is your favorite number? ")
if 4:
    print("Four is my favorite number also.")
```
Possible correct usage.
```python3
num = int(input("What is your favorite number? "))
if num == 4:
    print("Four is my favorite number also.")
```
"""), title="[blue]Whats wrong with this Python code[/]"))

with Live(layout):
    input()

console.clear()
################ == or in ################

layout["upper"].update(Panel(md("""
```python3
opinion = input("What type of food do you like? ")
if opinion == ["pizza", "tacos", "hamburgers"]:
    print("I think most people would agree.")
else:
    print("Thats a new one.")
```
"""), title="[blue]Whats wrong with this Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel(md("The issue here is:\n\nThe input variable opinion has a data type of `string` not `list` which can never be equal without conversion.  Even if you typed out the list exactly you would have to convert the input string to a list or convert the comparison argument to a string in order to match.\n\nInstead we should use the keyword `in` to check if the string that we type matches an item in the list."), title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["upper"].update(Panel(md("""
```python3
opinion = input("What type of food do you like? ")
if opinion == ["pizza", "tacos", "hamburgers"]:
    print("I think most people would agree.")
else:
    print("Thats a new one.")
```
```python3
opinion = input("What type of food do you like? ")
if opinion in ["pizza", "tacos", "hamburgers"]:
    print("I think most people would agree.")
else:
    print("Thats a new one.")
```
"""), title="[blue]Whats wrong with this Python code[/]"))

with Live(layout):
    input()

console.clear()
################ ################