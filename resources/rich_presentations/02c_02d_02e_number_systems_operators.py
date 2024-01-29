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
item_number = 27.283
another_num = 17
x = 13/5
y = 13//5
z = 13%5
a = 2 ** 5

printwait(md(f"""
# Format Specifiers

ℹ️  The ***formatted string*** is how we would use a variable in a print statement.             

```python3
item_number = 27.283
print(f"My item number is {{item_number}}")
```           

"""))

printwait(md(f"""
```python3
My item num is {item_number}.
```

"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  But we can also add format specifiers after the variable which allow us to do things. 
                   
❓  What do you think this will print?

```python3
item_number = 27.283
print(f"My item number is {{item_number:10}}")
```

"""))

printwait(md(f"""
```python3
My item num is {item_number:10}.
```
Notice that it was padded with spaces to the left.

"""))         

console.clear()
##########################################
printwait(md(f"""
ℹ️  Justification and centering.
             
```python3
item_number = 27.283
print(f"My item number is {{item_number:>10}}.") # right justified
print(f"My item number is {{item_number:<10}}.") # left justified
print(f"My item number is {{item_number:^10}}.") # centered

"""))

printwait(md(f"""
```python3
My item number is {item_number:>10}.            
My item number is {item_number:<10}.  
My item number is {item_number:^10}.           
```         

"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  We can also round any float to a specific number of digits.

```python3
item_number = 27.283
print(f"My item number is {{item_number:.2f}}, rounded to two decimal places.")
```

"""))

printwait(md(f"""
```python3
My item num is {item_number:.2f}, rounded to two decimal places.
```

"""))

console.clear()
##########################################
printwait(md(f"""
ℹ️  This one is centered, rounded, and has extra space.
             
```python3
item_number = 27.283
print(f"My item number is {{item_number:^12.2f}}.")
```            

"""))

printwait(md(f"""
```python3
My item number is {item_number:^12.2f}.
```

"""))

console.clear()
##########################################
printwait(md(f"""
# Number Systems
             
ℹ️  These functions will convert to other number systems and display with the prefix.

```python3
print(bin(17))
print(oct(17))
print(hex(17)) 
```

"""))    

printwait(md(f"""
```python3
{bin(17)}
{oct(17)}
{hex(17)}
```

"""))

console.clear()
##########################################
printwait(md(f"""
             
ℹ️  Or we can use a format specifier to convert inside of a ***formatted string***.

```python3
another_num = 17
print(f"The number {{another_num}}, expressed in binary, is {{another_num:b}}.")
print(f"The number {{another_num}}, expressed in octal, is {{another_num:o}}.")
print(f"The number {{another_num}}, expressed in hexadecimal, is {{another_num:x}}.")
```

Incidentally, the format code "d" means decimal, which is the default and does not need to be specified.

"""))

printwait(md(f"""            
```python3
The number {another_num}, expressed in binary is {another_num:b}.
The number {another_num}, expressed in octal is {another_num:o}.
The number {another_num}, expressed in hexadecimal is {another_num:x}.
```

"""))

console.clear()
##########################################
printwait(md(f"""
# Floor division (//), Exponentiation (**), and Modulus operators (%)

```python3
x = 13/5            
{x}, is the result of 13/5.
```

"""))

printwait(md(f"""
ℹ️   Floor division (//) drops the remainder.

```python3
x = 13//5            
{y}, is the result of 13//5.
```

"""))

printwait(md(f"""
ℹ️   Modulus (%) only gives you the remainder.

```python3
x = 13%5            
{z}, is the result of 13%5.
```

The remainder 3 represents 3/5 or 0.6 which is the part that floor division leaves off.

"""))

printwait(md(f"""
ℹ️  Exponentiation (**) is x to the power of n or xⁿ. Where x is any number multiplied by itself n times.

```python3
x = 2**5            
{a}, is the result of 2**5.
```

This example gives us 2 to the power of 5 or 2\*2\*2\*2\*2.

"""))

console.clear()
##########################################
printwait(md(f"""
# What not to do!

ℹ️  Format specifiers for other number systems don't work for floats:

This will give an error, because item_number is a float:
```python3           
item_number = 27.283 
print({{item_number:b}})
```

```python3
Traceback (most recent call last):
  ...
ValueError: Unknown format code 'b' for object of type 'float'
```

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