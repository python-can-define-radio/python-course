import time
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.console import Console
from rich.markdown import Markdown
from guizero import App, Picture, Text



console = Console()
print = console.print
input = console.input
THEME = "zenburn"
APP = App(title="Dictionaries", width=1300, height=750)
picture = Picture(APP, image="/home/michael.a.hutchings98/Desktop/Hutchings/practice/resources/graphics/dictionary.jpg")
message = Text(APP, text="Close Window to go to the first example.")
APP.display()
layout = Layout()
layout.split_row(
    Layout(name="left"),
    Layout(name="right"),
)
layout["right"].split_column(
    Layout(name="top"),
    Layout(name="bottom"),
)
layout["left"].ratio = 3
layout["top"].ratio = 1


def md(*args, **kwargs):
    return Markdown(*args, code_theme=THEME, inline_code_theme=THEME, inline_code_lexer="python3", **kwargs)


def printwait(*args, **kwargs):
    print(*args, **kwargs)
    input()


console.clear()
#################Basic dictionary#################

personaldata = {
  "firstname": "Trevor",
  "lastname": "Gold",
  "age": 23,
  "location": "Boston",
  "position": "Programmer",
  "ESD": "2022Nov21"
}

layout["left"].update(md("""
# Dictionaries 

ℹ️  Dictionaries are a python data structure that consist of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

"""))

layout["top"].update(Panel(md("""
```python3
personaldata = {
  "firstname": "Trevor",
  "lastname": "Gold",
  "age": 23,
  "location": "Boston",
  "position": "Programmer",
  "ESD": "2022Nov21"
}
```
"""), title="[blue]Our Dictionary[/]"))

layout["bottom"].update(md("""

"""))


layout["left"].update(md("""
# Dictionaries 

ℹ️  Dictionaries are a python data structure that consist of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

The `key` is a name of the general category or type of data which is stored in the value (similar to a variable).  
\nThe `value` is the specific data stored.     

""")) 

with Live(layout):
    input()

console.clear()
##########Pulling data from a dictionary##########

layout["left"].update(md("""
# Retrieving Data
                         
ℹ️  There are different methods for retrieving dictionary data depending on what data you want and what you are doing with it. 

```python3
## Retrieves all keys which we are putting into a list.  
mykeys = list(personaldata.keys())
print(mykeys)

## Retrieves all values which we are putting into a list.  
myvals = list(personaldata.values())
print(myvals)

## Retrieves all items which we are putting into a list of tuples. 
mydictitems = list(personaldata.items())
print(mydictitems)
```

""")) 

layout["top"].update(Panel(md("""
```python3
personaldata = {
  "firstname": "Trevor",
  "lastname": "Gold",
  "age": 23,
  "location": "Boston",
  "position": "Programmer",
  "ESD": "2022Nov21"
}
```                      
"""), title="[blue]Our Dictionary[/]")) 

layout["bottom"].update(md("""

"""))

with Live(layout):
    input()

layout["left"].update(md("""
# Retrieving Data
                         
ℹ️  There are different methods for retrieving dictionary data depending on what data you want and what you are doing with it. 

```python3
## Retrieves all keys which we are putting into a list.  
mykeys = list(personaldata.keys())
print(mykeys)

## Retrieves all values which we are putting into a list.  
myvals = list(personaldata.values())
print(myvals)

## Retrieves all items which we are putting into a list of tuples. 
mydictitems = list(personaldata.items())
print(mydictitems)
```
Accessing dictionary data

```python3
['firstname', 'lastname', 'age', 'location', 'position', 'ESD']

['Trevor', 'Gold', 23, 'Boston', 'Programmer', '2022Nov21']

[('firstname', 'Trevor'), ('lastname', 'Gold'), ('age', 23), ('location', 'Boston'), ('position', 'Programmer'), ('ESD', '2022Nov21')]
```                         

"""))

with Live(layout):
    input()
                
# console.clear()
####Pulling single data point from a dictionary####

layout["left"].update(md("""                       
ℹ️  This demonstrates accessing a single data point from the dictionary. 

```python3
print(f'Do you know {personaldata["firstname"]} ...?')
                         
## Alternate approach:
print(f'Do you know {personaldata.get("firstname")} ...?')
```
                         
"""))

with Live(layout):
    input()

layout["left"].update(md("""
 
ℹ️  This demonstrates accessing a single data point from the dictionary. 

```python3
print(f'Do you know {personaldata["firstname"]} ...?')
                         
## Alternate approach:
print(f'Do you know {personaldata.get("firstname")} ...?')
```

```python3
Do you know Trevor ...?
Do you know Trevor ...?                         

"""))

with Live(layout):
    input()


console.clear()
##########Pulling data from a dictionary##########

jobname = {
  "Frank": "Programmer",
  "Jim": "Linguist",
  "Melissa": "IT Consultant",
  "Henry": "Linguist",
  "Jane": "Programmer",
  "George": "IT Consultant"
}

layout["left"].update(md("""
 
ℹ️  Lets look at a new dictionary. 

"""))
                         
layout["top"].update(Panel(md("""
```python3
jobname = {
  "Frank": "Programmer",
  "Jim": "Linguist",
  "Melissa": "IT Consultant",
  "Henry": "Linguist",
  "Jane": "Programmer",
  "George": "IT Consultant"
}
```                      
"""), title="[blue]Our Dictionary[/]")) 

layout["bottom"].update(md("""

"""))

with Live(layout):
    input()

layout["left"].update(md("""
 
ℹ️  Lets look at a new dictionary.

❓  What will this print? 

```python3
for name in jobname:
    print(f"{name} works as a(n) {jobname[name]}")
```                                                                                                    
"""))

with Live(layout):
    input()

layout["left"].update(md("""
 
ℹ️  Lets look at a new dictionary.

❓  What will this print? 

```python3
for name in jobname:
    print(f"{name} works as a(n) {jobname[name]}")
``` 

```python3
Frank works as a(n) Programmer
Jim works as a(n) Linguist
Melissa works as a(n) IT Consultant
Henry works as a(n) Linguist
Jane works as a(n) Programmer
George works as a(n) IT Consultant 
```
                                                                                                                                                                                                      
"""))

with Live(layout):
    input()

layout["left"].update(md("""

❓  What will this print? 

```python3
print("These people are IT Consultants:")
for name in jobname.keys():
    if jobname[name].startswith("IT"):
        print(name)
``` 

"""))

with Live(layout):
    input()

layout["left"].update(md("""

❓  What will this print? 

```python3
print("These people are IT Consultants:")
for name in jobname.keys():
    if jobname[name].startswith("IT"):
        print(name)
``` 

```python3                         
These people are IT Consultants:
Melissa
George                         
```
                         
"""))

with Live(layout):
    input()

layout["left"].update(md("""

Alternate approach: 

```python3
print("These people are Linguists:")
for name, title in jobname.items():
    if title == "Linguist":
        print(name)
``` 
                         
"""))

with Live(layout):
    input()

layout["left"].update(md("""

Alternate approach: 

```python3
print("These people are Linguists:")
for name, title in jobname.items():
    if title == "Linguist":
        print(name)
``` 
                         
```python3
These people are Linguists:
Jim
Henry                         
```   
                                                                        
"""))

with Live(layout):
    input()


############Example dictionary in use############

# import random
# user = input("rock paper or scissors? ")

# beats = {
#     "rock": "scissors",
#     "scissors": "paper",
#     "paper": "rock"
# }

# choices = ["rock", "paper", "scissors"]
 
# cpu = random.choice(choices)
# print(f"cpu has selected: {cpu}")

# if user == cpu:
#     print("Tie")
# elif beats[user] == cpu:
#     print("You win!")
# else:
#     print("You lose!")
    
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