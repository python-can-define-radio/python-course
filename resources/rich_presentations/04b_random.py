import random
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from guizero import App, Picture, Text



console = Console()
print = console.print
input = console.input
THEME = "zenburn"
APP = App(title="Randomness", width=1280, height=800)
picture = Picture(APP, image="practice/resources/graphics/randomness.png")
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
# random.choice 
             
ℹ️  Choosing a random string from a list. 

```python3 
import random  #For all following examples we will assume the random module has been imported
                          
fromlist = ["mike", "joe", "frank", "samantha", "tom"]  
randomname = random.choice(fromlist)  
print(randomname) 
```

"""))

printwait(md("""
ℹ️  Capitalizes just the first letter.

```python3              
capitalized = randomname[0].upper() + randomname[1:]
print(capitalized)
```

"""))             

printwait(md("""
This does the same thing.

```python3              
capitalfirstletter = randomname[:1].upper()
restofname  = randomname[1:].lower()
print(f"{capitalfirstletter}{restofname} is a great student.") 
```
                                 
"""))

fromlist = ["mike", "joe", "frank", "samantha", "tom"]  
randomname = random.choice(fromlist) 
print(randomname)
capitalized = randomname[0].upper() + randomname[1:] 
print(capitalized)
capitalfirstletter = randomname[:1].upper()
restofname  = randomname[1:].lower()  
print(f"{capitalfirstletter}{restofname} is a great student.") 
input()

printwait(md("""
ℹ️  Now that we have learned the hard way... Theres a built in function for that.  

```python3                          
x = randomname.capitalize()
print(x)  
```

"""))

x = randomname.capitalize()
print(f"{x}\n")  
input()

console.clear()
##########################################
printwait(md("""
# random.random
                          
ℹ️  Prints a random float between 0 and 1.

```python3  
print(f"{random.random()}")
````

"""))

printwait(md(f"""
             
```python3
{f"{random.random()}"}
```   
                     
"""))

printwait(md("""
Limits it to 2 decimal places. 

```python3              
print(f"{random.random():.2f}")
````

"""))

printwait(md(f"""
             
```python3
{f"{random.random():.2f}"}
```   
                     
"""))

printwait(md("""
Produces any number from 0-100 (whole_numbers only).

```python3               
print(f"{random.random()*100:.0f}")  
```
             
"""))            

printwait(md(f"""
             
```python3
{f"{random.random()*100:.0f}"}
```   

"""))

console.clear()
##########################################
printwait(md("""
# random.uniform 
                        
ℹ️  Produces random float with start stop endpoints.

```python3  
print(random.uniform(0.0, 5.0))  
```
             
"""))  

printwait(md(f"""
             
```python3
{f"{random.uniform(0.0, 5.0)}"}
```   
                     
"""))

console.clear()
##########################################
printwait(md("""
# random.randint   
                      
ℹ️  Produces a random integer between 5 and 8.

```python3  
print(random.randint(5, 8))  
```
             
"""))             

printwait(md(f"""
             
```python3
{f"{random.randint(5, 8)}"}
```   
                     
"""))

console.clear()
##########################################
printwait(md("""
# random.randrange
             
ℹ️  Produces a random integer between -5 and 11 but does not include the endpoint.     
          
```python3             
print(random.randrange(-5, 11, 2))  
```
             
"""))             

printwait(md(f"""
As shown here it would give only odd numbers from -5 to 9 because of the step value (2).            
```python3
{f"{random.randrange(-5, 10+1, 2)}"}
```   

"""))

console.clear()
##########################################
printwait(md("""
# random.getrandbits   
                       
❓  What do you think this code would do?

```python3               
ipadd = random.getrandbits(8)
print(ipadd)
```
             
"""))            

ipadd = random.getrandbits(8)
print(ipadd)
input()


printwait(md("""
Will produce a random integer from 0-255 useful for creating random IP addresses.
             
"""))

printwait(md("""
Do this four times and you have an IP address.   

```python3 
print(f"{random.getrandbits(8)}.{random.getrandbits(8)}.{random.getrandbits(8)}.{random.getrandbits(8)}")  
```            

"""))
 
print(f"{random.getrandbits(8)}.{random.getrandbits(8)}.{random.getrandbits(8)}.{random.getrandbits(8)}\n") 

printwait(md("""        
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