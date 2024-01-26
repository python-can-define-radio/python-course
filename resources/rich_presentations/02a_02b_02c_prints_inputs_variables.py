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

# console.clear()
# ##########################################
# printwait(md("""
# # Commonly used characters
             
# | Character | Common name |
# |--|-----------|
# |()| parenthesis |
# |[]| brackets |
# |{}| braces |

# # Math operators (other than +,-,*,/)          
# | Character | Common name |
# |--|-----------|
# |//| floor division |             
# |%| modulus |
# |**| exponentiation |
                                                
# """))  

console.clear()
##########################################
printwait(md(f"""
# Prints 

ℹ️  Lets start with a basic print statement.
              
```python3
print("Here we go!")
```

"""))            

printwait(md(f"""
```python3
Here we go!
```
             
Here we see the first type of data that we can work with in python, a ***string***.

"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  We can create a multi-line string by simply using multiple print statements.
      
```python3
print("If you want")
print("separate lines, you")
print('can do it')
print('like this.')
```

```python3
If you want
separate lines, you
can do it
like this.
```

In Python, the single quote can be used instead of the double quote.           
                                      
"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  Another method for creating seperate lines would be to use an `escape` character.
             
```python3
print("If you want \\nseparate lines, you \\ncan do it \\nlike this.")
```

"""))             

printwait(md(f"""
```python3
If you want
separate lines, you
can do it
like this.
```
                                      
The `\\n` is used to create a ***new line***, python recognizes the n after the escape character to have special meaning.

"""))            

console.clear()
##########################################
printwait(md(f"""
ℹ️  A third method for creating seperate lines would be to use triple quotes which is called a multi-line string.
             
```python3
print(\"""If you want
separate lines, you
can do it
like this.\""")
```

""")) 

printwait(md(f"""
```python3
If you want
separate lines, you
can do it
like this.
```        

Using triple quotes without the print would be ignored as code.             
             
"""))   

console.clear()
##########################################
printwait(md(f"""
# Inputs
ℹ️  We use an ***input*** to gather information from the ***user***.
             
```python3
input("Please type your name? ")            
```

"""))

printwait(md(f"""
```python3
Please type your name? |
```

Notice we added a space after the punctuation to move the cursor a little bit away from the text.

"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  If we want to save the user data we have to store it in a ***variable***. 
                         
```python3
name = input("Please type your name? ") 
```
             
This would give us the same result as the previous one but whatever is typed by the user will be stored in the variable `name` so we can use it later.
             
"""))

printwait(md(f"""
ℹ️  Here we will use the variable to greet the user.             

```python3
name = input("Please type your name? ")
print(f"Hello {{name}}!") 
```

Lets try it.

"""))

name = input("Please type your name? ")
print(f"Hello {name}!\n") 

printwait(md(f"""        
This is called a ***formatted string*** and we will be using it a lot.            
             
"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  Generally variable names CAN have any mix of uppercase or lowercase letters, numbers, or an underscore (_). However it cannot start with a number.

Single letters are often used for simplicity like a,b,c or x,y,z.
```python3
x = 5
or
x = int(input("Please type a number? "))
```
These are typically used when storing numbers. 
             
Numbers introduce two more data types ***integers*** (whole numbers), and ***floats*** (non-whole numbers).

"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  Naming the variable to indicate what is stored is also common.
             
```python3
name = "Catherine"
or
name = input("Please type your name? ")
or
number = int(input("Please type a number? "))
```           

"""))

console.clear()
##########################################
printwait(md(f"""
# Variables (What not to do)
ℹ️  Do NOT use ***keywords*** or ***function*** names.

```python3
print = "Hello"
or
while = 5
```

This will cause your normal built-in print function to stop working,  
and while is a keyword reserved by python for specific conditions.  

"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  Do NOT start your variable with a number or use spaces anywhere in the variable.
             
```python3
3rdthing = "Whatever you want"
or
my number = 45.7             
```

These will cause a:  
SyntaxError: invalid decimal literal  
SyntaxError: invalid syntax.

The full python naming conventions can be found here.  
https://pythonguides.com/python-naming-conventions/ 

Last example hit Enter to exit. 
                   
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

