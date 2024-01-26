import time
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax

console = Console()
print = console.print
input = console.input
THEME = "zenburn"


def md(*args, **kwargs):
    return Markdown(*args, code_theme=THEME, inline_code_theme=THEME, inline_code_lexer="python3", **kwargs)


def printwait(*args, **kwargs):
    print(*args, **kwargs)
    input()


console.clear()
##########################################
printwait(md("""
# For loop 

```python3
names = ["Lisa", "Todd", "Mike", "Jennifer"]
for name in names:
    print(f"Hello {name}. Welcome to the Python course.")
```
             
"""))             

names = ["Lisa", "Todd", "Mike", "Jennifer"]
for name in names:
    print(f"Hello {name}. Welcome to the Python course.")
input()

console.clear()
##########################################

printwait(md("""
Basic for loop that delays printing
             
```python3
import time
             
name = "Winchester"
for letter in name:
    print(letter, end="", flush=True)
    time.sleep(.25)
```

"""))

name = "Winchester"
for letter in name:
    print(letter, end="")
    time.sleep(.25)
print()
print()
input()
                         
console.clear()
##########################################
printwait(md("""
# For loop counting temperatures

```python3
temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40, 32]
above = 0
below = 0
for temp in temps_in_F:
    if temp > 32:
        above += 1
    elif temp <= 32:
        below += 1
print(f"There are {above} measurements above freezing and {below} measurements below freezing.")
```            

"""))   

temps_in_F = [47, 100, 16, 82, 30, 68, 90, 25, 40, 32]
above = 0
below = 0
for temp in temps_in_F:
    if temp > 32:
        above += 1
    elif temp <= 32:
        below += 1
print(f"There are {above} measurements above freezing and {below} measurements below freezing.")
input()
             
console.clear()
##########################################
printwait(md("""
# For loop with count and if else decisions
             
```python3
myitems = ["computer", "desk", "chair", "table", "bookcase", "window"]
count = 0
for item in myitems:
    if item.startswith("win"):
        print(f"I hope you have a nice view from that {item}.")
        print("----------")
    elif item.startswith("book"):
        print(f"Wow nice {item} do you like to read?\nThey are commonly found in offices.")
        print("----------")
        count += 1
    else:
        print(f"A {item} is an example of something you would find in an office.")
        print("----------")
        count += 1
print(f"You have {count} pieces of furniture in your office.\n")
```            

"""))  

myitems = ["computer", "desk", "chair", "table", "bookcase", "window"]
count = 0
for item in myitems:
    if item.startswith("win"):
        print(f"I hope you have a nice view from that {item}.")
        print("----------")
    elif item.startswith("book"):
        print(f"Wow nice {item} do you like to read?\nThey are commonly found in offices.")
        print("----------")
        count += 1
    else:
        print(f"A {item} is an example of something you would find in an office.")
        print("----------")
        count += 1
print(f"You have {count} pieces of furniture in your office.\n")
input()

console.clear()
##########################################
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
 

def done(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Python", font='ogre'),
            screen.height // 2 - 10),
        Cycle(
            screen,
            FigletText("Rocks !", font='ogre'),
            screen.height // 2 - 4),
        Cycle(
            screen,
            FigletText("Any questions ?", font='ogre'),
            screen.height // 2 + 2),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(done)