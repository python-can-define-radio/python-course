from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from guizero import App, Picture, Text



console = Console()
print = console.print
input = console.input
THEME = "zenburn"
APP = App(title="IF-Else Decision", width=850, height=500)
picture = Picture(APP, image="practice/resources/graphics/If-Statement-in-Python.png")
message = Text(APP, text="Close Window to go to the first example.")
APP.display()


def md(*args, **kwargs):
    return Markdown(*args, code_theme=THEME, inline_code_theme=THEME, inline_code_lexer="python3", **kwargs)


def printwait(*args, **kwargs):
    print(*args, **kwargs)
    input()


console.clear()
##########################################
print(md(f"""
# IF -  ELSE
             
ℹ️  A basic if-else statement.
             
```python3
x = int(input("Type a number please? "))
if x == 5:
    print("Nice 5")
else:
    print("This will happen if we type anything other than 5.")
```
             
Let's try it! (I put it in loop here so we can do it more than once.)

"""))   

print("[blue][on yellow bold]Enter[/] to start.[/]")
input()
print("[blue][bold on yellow]-1[/] to quit.[/]")

x = int(input("Type a number please? "))
while x != -1:
    if x == 5:
        print("Nice 5\n")
    else:
        print("This will happen if we type anything other than 5.\n")
    x = int(input("Type a number please? "))
print()

printwait(md(f"""         
ℹ️  Since we told it to expect integers on the input this is what we would see if we tried letters or floats.

```python3
Traceback (most recent call last):
  ...
    x = int(input("Type a number please? "))
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'asdf'            
```                          

"""))

console.clear()
##########################################
print(md(f"""
# IF - IF - ELSE

❓  Whats happening in this code?             

```python3
x = int(input(\"""What number would you like to try?  
Enter any number.--> \"""))  
if x == 5:  
    print("I really like that number.")  
if x != 5:  
    print("Why didn't you choose 5?")  
if x >= 5:  
    print("Apparently you like numbers of 5 and above.")  
else:  
    print("Apparently you like small numbers.")  
if 6 < x < 50:  
    print("Apparently you like numbers between 6 and 50.")
```  

Let's try it!

"""))

print("[blue][on yellow bold]Enter[/] to start.[/]")
input()
print("[blue][bold on yellow]-1[/] to quit.[/]")

x = int(input("""What number would you like to try?  
Enter any number.--> """))  
while x != -1:
    if x == 5:  
        print("I really like that number.\n")  
    if x != 5:  
        print("Why didn't you choose 5?\n")  
    if x >= 5:  
        print("Apparently you like numbers of 5 and above.\n")  
    else:  
        print("Apparently you like small numbers.\n")  
    if 6 < x < 50:  
        print("Apparently you like numbers between 6 and 50.\n")
    x = int(input("""What number would you like to try?  
Enter any number.--> """)) 

console.clear()
##########################################
print(md(f"""
# IF - ELIF - ELSE

❓  How about this one?             

```python3             
x = int(input(\"""What number would you like to try?
Enter any number.--> \"""))
if x > 500:
    print("So you like large numbers.")
elif x <= 100:
    print("So you like small numbers.")
elif 100 < x < 500:
    print("Thats between 100 and 500")
else: # Will this ever happen?
    print("That is not a valid number.")
```

Let's try it!

"""))

print("[blue][on yellow bold]Enter[/] to start.[/]")
input()
print("[blue][bold on yellow]-1[/] to quit.[/]")

x = int(input("""What number would you like to try?
Enter any number.--> """))
while x != -1:
    if x > 500:
        print("So you like large numbers.\n")
    elif x <= 100:
        print("So you like small numbers.\n")
    elif 100 < x < 500:
        print("Thats between 100 and 500.\n")
    else: 
        print("That is not a valid number.\n")
    x = int(input("""What number would you like to try?  
Enter any number.--> """))

console.clear()
##########################################
print(md(f"""
# IF - ELIF - ELSE 

ℹ️  This is the same as the previous example. (Just a little shorter)

```python3               
x = int(input(\"""What number would you like to try?
Enter any number.--> \"""))
if x > 500:
    print("So you like large numbers.")
elif x < 100:
    print("So you like small numbers.")
else:
    print("Thats between 100 and 500.")
```

Let's try it!

"""))

print("[blue][on yellow bold]Enter[/] to start.[/]")
input()
print("[blue][bold on yellow]-1[/] to quit.[/]")

x = int(input("""What number would you like to try?
Enter any number.--> """))
while x != -1:
    if x > 500:
        print("So you like large numbers.\n")
    elif x < 100:
        print("So you like small numbers.\n")
    else:
        print("Thats between 100 and 500.\n")
    x = int(input("""What number would you like to try?  
Enter any number.--> """))

console.clear()
##########################################
print(md(f"""
# Nested IF

❓  Lets talk about this one? 
             
```python3               
x = int(input("Please type a number. "))
y = int(input("Please type another number. "))
if x == 5:
    if y == 7:
        print("Ok we met both conditions.")
    else:
        print("x was 5 but y was not 7.")
else:
    print("x was not 5 so it did not check for y.")
```            

Let's try it!

"""))

print("[blue][on yellow bold]Enter[/] to start.[/]")
input()
print("[blue][bold on yellow]-1[/] to quit.[/]")

def run_example_5():
    x = int(input("Please type a number. "))
    if x == -1:
        return
    y = int(input("Please type another number. "))
    while True:
        if y == -1:
            return
        if x == 5:
            if y == 7:
                print("Ok we met both conditions.")
            else:
                print("x was 5 but y was not 7.")
        else:
            print("x was not 5 so it did not check for y.")
        x = int(input("Please type a number. "))
        if x == -1:
            return
        y = int(input("Please type another number. ")) 

run_example_5()

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
    