from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from guizero import App, Picture, Text



console = Console()
print = console.print
input = console.input
THEME = "zenburn"
APP = App(title="Lists", width=950, height=590)
picture = Picture(APP, image="practice/resources/graphics/lists.png")
message = Text(APP, text="Close Window to go to the first example.")
APP.display()


def md(*args, **kwargs):
    return Markdown(*args, code_theme=THEME, inline_code_theme=THEME, inline_code_lexer="python3", **kwargs)


def printwait(*args, **kwargs):
    print(*args, **kwargs)
    input()


console.clear()
##########################################
list_colors = ["green", "red", "orange", "blue"]

printwait(md("""
# Indexing 1/3

ℹ️  Lists are zero-indexed. That means...
```python3       
list_colors = ["green", "red", "orange", "blue"]
                  0       1       2        3 
                      is equivalent to
                 -4      -3      -2       -1 
```
ℹ️  Reverse indexing is also allowed...
                              
❓  What would be the result of each?
               
```python3
print(list_colors[0])
print(list_colors[-4])
```
             
"""))

printwait(md(f"""
These are both valid and give us the same result.

```python3
Result list_colors[0] : {list_colors[0]}
Result list_colors[-4] : {list_colors[-4]}
```

"""))

console.clear()
##########################################
printwait(md(f"""
# Indexing 2/3

```python3
list_colors = ["green", "red", "orange", "blue"]
```

ℹ️  You can use any mixture of positive and negative indexing
to get the same result.

Printing `list_colors[1:3]` gives us...

"""))
print(list_colors[1:3])
print()
printwait(md(f"""
which is the same as printing `list_colors[1:-1]`...

"""))
print(list_colors[1:-1])
print()
printwait(md(f"""
or this `list_colors[-3:-1]`...

"""))
print(list_colors[-3:-1])
print()
printwait(md(f"""
or this `list_colors[-3:3]`...

"""))
print(list_colors[-3:3])
input()

console.clear()
##########################################
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]

printwait(md(f"""
# Indexing 3/3

```python3
names = ["Sarah", "Tom", "Harry", "Susan", "Becky"]
```

ℹ️  Strings within a list are also indexed.

❓  What will this print?  

```python3
print(names[4][3])
```
"""))

printwait(md(f"""
```python3
{names[4][3]}
```

"""))

console.clear()
##########################################

data = [["tom", 20], ["frank", 18], ["jessica", 21], ["george", 43]]

printwait(md(f"""
# List of lists
             
```python3
data = [["tom", 20], ["frank", 18], ["jessica", 21], ["george", 43]]'
```
             
ℹ️  You can also have lists within a list.

❓  What do you think this will print?

```python3          
print(data[0])
```

"""))

printwait(md(f"""
```python3
{data[0]}
```

"""))

printwait(md(f"""
❓  What do you think this will print?

```python3          
print(data[0][0], data[0][1])
```
"""))

printwait(md(f"""
```python3
{data[0][0], data[0][1]}
```

"""))          

printwait(md(f"""
What do you think this will print?

```python3          
print(data[0][0][2])
```

""")) 

printwait(md(f"""
```python3
{data[0][0][2]}
```

"""))              

console.clear()
##########################################

data = [["tom", 20], ["frank", 18], ["jessica", 21], ["george", 43]]
user = ["jim", 25]
data.append(user)

printwait(md(f"""
# Adding to a List
             
```python3
data = [["tom", 20], ["frank", 18], ["jessica", 21], ["george", 43]]
```

ℹ️  To add to a list you could do this.

```python3
user = ["jim", 25]
data.append(user)
```

data variable after the addition.

```python3
{f"data = {data}"}
```

""")) 

console.clear()
##########################################

vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')

printwait(md(f"""
# Inserting to a List
             
```python3
vowel = ['a', 'e', 'i', 'u']
```

ℹ️  You can insert to a specific list index.
             
'o' is inserted at index 3 (4th position).

```python3
vowel.insert(3, 'o')
```

vowel variable after the insertion.

```python3
{f"vowel = {vowel}"}
```

"""))

console.clear()
##########################################

del data[2]

printwait(md(f"""
# Deleting from a List
             
```python3
data = [['tom', 20], ['frank', 18], ['jessica', 21], ['george', 43], ['jim', 25]]
```

ℹ️  To remove from a list.

```python3
del data[2]
```

data variable after the removal.

```python3
{f"data = {data}"}
```

That was the last example hit Enter to exit.

"""))

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