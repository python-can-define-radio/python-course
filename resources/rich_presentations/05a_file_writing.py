from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown


def md(*args, **kwargs):
    return Markdown(*args, code_theme=THEME, inline_code_theme=THEME, inline_code_lexer="python3", **kwargs)


def printwait(*args, **kwargs):
    print(*args, **kwargs)
    input()

console = Console()
print = console.print
input = console.input
THEME = "zenburn"
layout = Layout()

layout.split_row(
    Layout(name="left"),
    Layout(name="right"),
)
layout["left"].split_column(
    Layout(name="upper"),
    Layout(name="lower"),
)
layout["left"].ratio = 3
layout["upper"].ratio = 3

###############write###############

layout["upper"].update(Panel(md("""
```python3
f = open(f"05a_my_file.txt", "w")
f.write("Here are some words.")
f.write("More words.\\n")
f.close()
```
"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))
layout["right"].update(Panel("", title="[blue]File contents[/]"))
console.clear()

with Live(layout):
    input()

layout["right"].update(Panel("""\nHere are some words.
More words.""", title="[blue]File contents[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("\nThe [red bold italic]w[/] stands for write to the filename in question. It will create the file if it doesn't exist or overwrite any existing data in the file.\n\nCommon practice is to add a new line at the end of your last file write.", title="[blue]Commentary[/]"))

with Live(layout):
    input()

###############write-with-error###############

layout["upper"].update(Panel(md("""
```python3
f = open(f"05a_my_file.txt", "x")
f.write("Here are some words.")
f.write("More words.\\n")
f.close()
```
"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))
layout["right"].update(Panel("", title="[blue]File contents[/]"))
console.clear()

with Live(layout):
    input()

layout["right"].update(Panel("""\nHere are some words.
More words.""", title="[blue]File contents[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("\nThe [red bold italic]x[/] argument will also write to the filename in question or return a [green bold italic]FileExistsError[/] if the file already exists.", title="[blue]Commentary[/]"))

with Live(layout):
    input()

###############append###############

layout["upper"].update(Panel(md("""
```python3
f = open(f"05a_my_file.txt", "a")
f.write("Yet more words.")
f.write("and more words.")
f.close()
```
"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))
layout["right"].update(Panel("""\nHere are some words.
More words.""", title="[blue]File contents[/]"))

with Live(layout):
    input()

layout["right"].update(Panel("""\nHere are some words.
More words.Yet more words.
and more words.""", title="[blue]File contents[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("The [red bold italic]a[/] stands for append from the filename in question. It will add to the data at the end.\n\nThis is why it is common practice to add a new line at the end of your last file write. Hit [red bold italic]ENTER[/] again to see the difference the new line makes.", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("The [red bold italic]a[/] stands for append from the filename in question. It will add to the data at the end.\n\nThis is why it is common practice to add a new line at the end of your last file write.", title="[blue]Commentary[/]"))

layout["right"].update(Panel("""\nHere are some words.
More words.
Yet more words.
and more words.""", title="[blue]File contents[/]"))

with Live(layout):
    input()

###############read###############

layout["upper"].update(Panel(md("""
```python3
f = open(f"05a_my_file.txt", "r")
contents = f.read()
print(contents)
f.close()
```
"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["upper"].update(Panel(md("""
```python3
f = open(f"05a_my_file.txt", "r")
contents = f.read()
print(contents)
f.close()
```
```python3
Here are some words.
More words.
Yet more words.
and more words.
```                                
"""), title="[blue]Python code[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("The [red bold italic]r[/] stands for read from the filename in question.", title="[blue]Commentary[/]"))

with Live(layout):
    input()

###############readline###############

layout["upper"].update(Panel(md("""
```python3
f = open(f"05a_my_file.txt", "r")
firstline = f.readline()  
secondline = f.readline()  
thirdline = f.readline()  
print(firstline)  
print(secondline)  
print(thirdline)  
f.close()
```
"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["upper"].update(Panel(md("""
```python3
f = open(f"05a_my_file.txt", "r")
firstline = f.readline()  
secondline = f.readline()  
thirdline = f.readline()  
print(firstline)  
print(secondline)  
print(thirdline)  
f.close()
```
```python3
Here are some words.
More words.
Yet more words.
```                                                           
"""), title="[blue]Python code[/]"))

layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("[red bold italic]Readline[/] reads a single line at a time. It has a filepointer which [bold underline blue]bookmarks[/] the location in the event readline is called again while the file is still open.", title="[blue]Commentary[/]"))

with Live(layout):
    input()

###############readlines###############

layout["upper"].update(Panel(md("""
```python3  
f = open(f"05a_my_file.txt", "r")  
contents = f.readlines()  
print(contents)   
f.close()
```
"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["upper"].update(Panel(md("""
```python3  
f = open(f"05a_my_file.txt", "r")  
contents = f.readlines()  
print(contents)   
f.close()
```
```python3
['Here are some words.\\n', 'More words.\\n', 'Yet more words.\\n', 'and more words.\\n']
```

"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("[red bold italic]Readlines[/] puts each line of the document into a list but shows the new lines.", title="[blue]Commentary[/]"))

with Live(layout):
    input()

###############splitlines###############

layout["upper"].update(Panel(md("""
```python3  
f = open(f"05a_my_file.txt", "r")  
contents = f.read().splitlines()  
print(contents)   
f.close()
```
"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["upper"].update(Panel(md("""
```python3  
f = open(f"05a_my_file.txt", "r")  
contents = f.read().splitlines()  
print(contents)   
f.close()
```
```python3
['Here are some words.', 'More words.', 'Yet more words.', 'and more words.']
```

"""), title="[blue]Python code[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))
layout["right"].update(Panel("""\nHere are some words.
More words.
Yet more words.
and more words.""", title="[blue]File contents[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("[red bold italic]Splitlines[/] puts each line of the document into a list but does not show the new lines.", title="[blue]Commentary[/]"))

with Live(layout):
    input()

###############writebinary###############

layout["upper"].update(Panel(md("""
```python3  
f = open(f"05a_my_unique_file_binary.txt", "wb")  
mylist = [65, 66, 67, 68]  
madebytes = bytes(mylist)  
f.write(madebytes)  
f.close()
```
"""), title="[blue]Python code[/]"))
layout["right"].update(Panel("", title="[blue]File contents[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["right"].update(Panel("""\nABCD""", title="[blue]File contents[/]"))

with Live(layout):
    input()

layout["lower"].update(Panel("[red bold italic]Write binary[/] converts each decimal value to binary which can be read by a text editor as ascii characters.\n\nWe can only do this with numbers up to 255 because a byte has 8 bits. ", title="[blue]Commentary[/]"))

with Live(layout):
    input()

###############readbinary###############

layout["upper"].update(Panel(md("""
```python3  
f = open(f"05a_my_binary_file.txt", "rb")  
contents = f.read()  
convcontents = list(map(int, contents))  
print(convcontents)  
f.close()
```
"""), title="[blue]Python code[/]"))
layout["right"].update(Panel("""\nABCD""", title="[blue]File contents[/]"))
layout["lower"].update(Panel("", title="[blue]Commentary[/]"))

with Live(layout):
    input()

layout["upper"].update(Panel(md("""
```python3  
f = open(f"05a_my_binary_file.txt", "rb")  
contents = f.read()  
convcontents = list(map(int, contents))  
print(convcontents)  
f.close()
```
```python3
[65, 66, 67, 68]                                
```
"""), title="[blue]Python code[/]"))

layout["lower"].update(Panel("[red bold italic]Read binary[/] allows us to read the binary directly and convert each ascii character back to its decimal value which we then put back into a list.", title="[blue]Commentary[/]"))

with Live(layout):
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