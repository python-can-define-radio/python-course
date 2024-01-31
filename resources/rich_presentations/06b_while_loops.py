import time
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from termcolor import cprint
from guizero import App, Picture, Text



console = Console()
print = console.print
input = console.input
THEME = "zenburn"
APP = App(title="While Loops", width=1310, height=735)
picture = Picture(APP, image="practice/resources/graphics/whileloops.jpg")
message = Text(APP, text="Close Window to go to the first example.")
APP.display()


def md(*args, **kwargs):
    return Markdown(*args, code_theme=THEME, inline_code_theme=THEME, inline_code_lexer="python3", **kwargs)


def printwait(*args, **kwargs):
    print(*args, **kwargs)
    input()


console.clear()
##########################################

printwait(md("""
# While loop 

❓  How could me change this so it works with any capitalization of "yes".            

```python3
keepGoing = input("Do you want me to keep going? ")
while keepGoing == "yes":
    print("Since the variable keepGoing is still 'yes', I am going to keep going.")
    keepGoing = input("Do you want me to keep going? ")
print("Ok, you typed something other than 'yes', so I stopped.")
```
             
"""))             

keepGoing = input("Do you want me to keep going? ")
while keepGoing == "yes":
    print("Since the variable keepGoing is still 'yes', I am going to keep going.")
    keepGoing = input("Do you want me to keep going? ")
print("Ok, you typed something other than 'yes', so I stopped.")
input()
                         
console.clear()
##########################################

printwait(md("""
# While loop 

ℹ️  Here's a variation that gives you 4 guesses and displays "No, try again" if the guess was wrong.            
To accomplish this, we must ask for input twice: before the loop and inside the loop.
```python3
print("Welcome to the word guesser!")
secretWord = "water"
numguesses = 0
guess = input("What is your guess? ")
while guess != secretWord:
    print("No, try again.")  
    if numguesses < 3:
        numguesses += 1
        guess = input("What is your guess? ")
    else:
        print("Sorry, you ran out of guesses.")
        break
    if guess == secretWord:
        print("You got it!")
if guess == secretWord and numguesses < 1:
    print("wow you got it the first time!")
```
             
"""))             

print("Welcome to the word guesser!")
secretWord = "water"
numguesses = 0
guess = input("What is your guess? ")
while guess != secretWord:
    print("No, try again.")  
    if numguesses < 3:
        numguesses += 1
        guess = input("What is your guess? ")
    else:
        print("Sorry, you ran out of guesses.")
        break
    if guess == secretWord:
        print("You got it!")
if guess == secretWord and numguesses < 1:
    print("wow you got it the first time!")
input()
                         
console.clear()
##########################################

printwait(md("""
# While loop 

ℹ️  Here's a variation that TODO....
```python3
from termcolor import cprint
             
keepGoing = "yes"
count = 0
while keepGoing != "-1":
    cprint("Type number of operation or -1 to exit", "red", "on_white")
    keepGoing = input("Do you want me to keep going? add(1), subtract(2), exit(-1) ")
    if keepGoing == "1":
        count +=1
        cprint(f"The count is now {count}", "green", "on_red")
    elif keepGoing == "2":
        count -= 1
        cprint(f"The count is now {count}", "red", "on_yellow")
    elif keepGoing == "":
        cprint("You did not type anything please type 1 for add, 2 for subtract, or -1 to exit", "green")
print("Ok, stopping.")  
```
             
"""))             

keepGoing = "yes"
count = 0
while keepGoing != "-1":
    cprint("Type number of operation or -1 to exit", "red", "on_white")
    keepGoing = input("Do you want me to keep going? add(1), subtract(2), exit(-1) ")
    if keepGoing == "1":
        count +=1
        cprint(f"The count is now {count}", "green", "on_red")
    elif keepGoing == "2":
        count -= 1
        cprint(f"The count is now {count}", "red", "on_yellow")
    elif keepGoing == "":
        cprint("You did not type anything please type 1 for add, 2 for subtract, or -1 to exit", "green")
print("Ok, stopping.")  
input()   

console.clear()
##########################################

printwait(md("""
# While loop 

ℹ️  Using readline in a while loop.
```python3
mypath = "practice/python_examples_for_class/"
f = open(f"{mypath}05a_my_unique_file.txt", "r")
eachline = f.readline()
while eachline:
    print(eachline)
    eachline = f.readline()
f.close()
```
             
"""))             

mypath = "practice/python_examples_for_class/"
f = open(f"{mypath}05a_my_unique_file.txt", "r")
eachline = f.readline()
while eachline:
    print(eachline)
    eachline = f.readline()
f.close()
print()
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