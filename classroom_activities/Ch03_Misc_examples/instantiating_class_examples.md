Goal: demonstrate how Python objects work, and review what Python classes are

```python3

from turtle import Turtle, mainloop

## create two instances of Turtle
cooltur = Turtle()
awesometle = Turtle()
cooltur.pencolor("blue")
cooltur.pensize(4)
cooltur.goto(10, 50)
awesometle.pencolor("red")
awesometle.goto(50, 2)

mainloop()

########################################
## creates an alias of choice, called c
from random import choice as c

## creates an alias of print, called p
p = print

## prints a randomly chosen name
p(c(["bob", "joe"]))

##############################################
from paragradio.v2024_12 import SpecAnSim

# name of a class followed by parentheses:
# instantiating the class (creating an instance)
fries = SpecAnSim()
fries.start()

# name of a class alone:
# creates an alias (now SSA is usable as if it was SpecAnSim)
SSA = SpecAnSim

# this creates another, separate instance of SpecAnSim
burger = SpecAnSim()
burger.start()

# a third
stuff = SSA()
stuff.start()

```
