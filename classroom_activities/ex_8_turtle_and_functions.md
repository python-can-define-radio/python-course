# Turtle

The `turtle` module is a fun way to draw pictures and make games using Python.

It's also a great way to gain familiarity with Python concepts and syntax.

```python3
# 1
# Try this.
import turtle

turtle.forward(100)
turtle.left(90)
turtle.forward(200)

turtle.mainloop()
```

In this first example, you'll see that the "turtle" (the little triangle on the screen) moved forward, turned left, and moved forward again.

Now, let's make it turn right:

```python3
# 2
# Try this. Don't forget to import turtle.
turtle.forward(100)
turtle.right(90)
turtle.forward(200)

turtle.mainloop()
```

To avoid the window closing immediately, always put `turtle.mainloop()` at the end.

```python3
# 2b
# Try this. You'll notice that it closes immediately.
# The way to fix that is to put the mainloop part at the end.
turtle.forward(100)
```

Let's make it colorful! And let's slow it down too. Also, let's put a small delay at the beginning so that you have time see what is happening.

```python3
# 2c
# Try this.

import time
import turtle

turtle.speed(1)
time.sleep(4)    # This means 4 seconds. You can change it to higher or lower as needed.

turtle.pencolor("black")
turtle.pensize(10)
turtle.forward(20)

turtle.pencolor("red")
turtle.pensize(2)
turtle.forward(50)

turtle.pencolor("green")
turtle.pensize(20)
turtle.forward(200)
```

You can also pick up the pen, which means "stop drawing". (Conversely, `pendown` means "start drawing".)

```python3
# 2d
# Try this.
turtle.forward(50)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(30)


# 2e
# Draw three separate lines.


# 3
# Set the pen size to 20.
# Set the pen color to orange.
# Move forward 50 units.
# Turn left 45 degrees.
# Set the pen color to purple.
# Move forward 100 units.


# 3b
# Make the turtle draw a square with a different color for each side.


# 4
# Make the turtle draw a triangle with a different color for each side.
```

At this point, you may have noticed that the code for fairly simple tasks can be pretty long.

The solution? Functions.

There's a great [chapter in Arcade Academy about functions](https://learn.arcade.academy/en/latest/chapters/08_functions/functions.html). I recommend reading it. After you have read the intro and section 8.1, try this:

```python3
## 5
## This defines how to draw a triangle.
## However, it doesn't actually draw the triangle. Read below to see why.
def drawTriangle():
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    # Don't put the mainloop here.
```

As described in the [chapter in Arcade Academy about functions](https://learn.arcade.academy/en/latest/chapters/08_functions/functions.html):

> "Defining a function doesn’t cause the computer to _do_ anything. It is like giving a recipe to the computer. Give someone a recipe for banana bread and they know how to make it. They haven’t actually made it yet, they just know how. You have to _tell_ them to make banana bread. That is, after we **define** the function we must **call** the function before the code in it runs. To call a function, type the function name and follow it by parenthesis. Do not use **def**, that is only used when we define what the function does, not when we tell the computer to run it."

So, let's call the function that we defined.

```python3
## 5 continued
## This is the same definition as before.
def drawTriangle():
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    # Don't put the mainloop here.

## It's important to NOT indent the following lines.
turtle.pensize(15)
turtle.speed(1)
turtle.pencolor("red")
drawTriangle()    # This command runs drawTriangle. You could also say we are "calling" (running) drawTriangle.
turtle.pencolor("blue")
drawTriangle()
turtle.pencolor("green")
drawTriangle()
turtle.mainloop()
```

That should draw three triangles (red, blue, green). They draw stacked, so if you aren't quick, you may only see the green one.

Make sure you get that part working before moving on.

```python3
## 5b
## Copy and modify the previous example.
## In this version, have the turtle move forward a little bit after each triangle so that you can see each triangle separately.


## 5c
## Copy and modify the previous example.
## In this version, do this:
##  draw a triangle
##  stop drawing (pick up the pen)
##  move forward 400 units
##  start drawing (put down the pen)
##  draw a triangle
```


--------

```python3
## Try this. How does it differ from our original drawTriangle function?
def drawTriangle_pd():
    turtle.pendown()
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.penup()

drawTriangle_pd()
turtle.forward(300)
drawTriangle_pd()


# 6c
# Using drawTriangle_pd, draw three separate triangles of different colors.


# 6b
# Make a drawSquare function. Using that function, draw five separate squares. (This should only require about 10 to 25 lines of code. If you have more than that, look back at how drawTriangle helped to avoid repeated code.)


# 6d
# Try this.

def drawAShape():
    turtle.forward(100)
    turtle.left(140)
    turtle.forward(50)
    turtle.right(140)
    
drawAShape()
turtle.penup()
turtle.forward(10)
turtle.pendown()
drawAShape()


# 6e
# Try this.

def drawZ():
    turtle.forward(100)
    turtle.right(140)
    turtle.forward(100)
    turtle.left(140)
    turtle.forward(100)
    
drawZ()
turtle.penup()
turtle.forward(10)
turtle.pendown()
drawZ()


# 6f
# Copy and modify the previous example so that it draws two C's
# instead of two Z's.


# 7
# Try this.

def drawAShape():
    turtle.forward(100)
    turtle.left(140)
    turtle.forward(50)
    turtle.right(140)

drawAShape()
turtle.penup()
turtle.forward(10)
turtle.pendown()
drawAShape()
turtle.penup()
turtle.forward(10)
turtle.pendown()
drawAShape()


# 8
# Copy and modify the previous example so that it draws a different shape.


# 10
# Copy and modify the previous example so that it draws three separate squares.


# 11
# Define a function to draw a square.


# 13
# Try this.
linelength = 100
turtle.forward(linelength)


# 14
# Modify the previous example to ask the user what length of line to draw.


# 15
# Try this.
def drawTwoSides(thelen):
    turtle.forward(thelen)
    turtle.left(90)
    turtle.forward(thelen)

drawTwoSides(100)


# 16
# Try this.
def drawTwoSides(thelen):
    turtle.forward(thelen)
    turtle.left(90)
    turtle.forward(thelen)

lee = 100
drawTwoSides(lee)


# Some notes on terminology:
# In the previous example, `thelen` is a parameter of the function `drawTwoSides`.
# (The word "argument" is sometimes used instead of "parameter".)
# The functions that we defined before this did not have any parameters.
# You've already seen functions that use parameters, such as print() and turtle.forward().


# 17
# Modify the previous example so that `lee` comes from user input.
# For the sake of the exercise, don't change the inside of the function.
# (Ask if you don't know what that means.)


# 18
# Define a drawSquare function in the same style as drawTwoSides.
# In other words, the function should have one parameter called thelen.
# After defining the function, run drawSquare with length 100.
# Also, run drawSquare with length 200.
# Your code should look like this:

def drawSquare(thelen):
    you_write_code_here

drawSquare(100)
drawSquare(200)

# 19
# Try this. You'll need your drawSquare function from the previous question.

lee = int(input("How big should the square be?"))
drawSquare(lee)

# 20
# Modify the previous example like so:
# If the user picks a size that is negative, then let the user know that the side length must be positive.
# If the user picks a size that is too big, then let the user know that the side length is too big.
#  ("too big" is up to you to decide.)
# Otherwise, draw a square with the specified length.


# 21
# Try this:

keepGoing = "yes"
while keepGoing == "yes":
    print("Hello")
    keepGoing = input("Do you want the program to continue? Type 'yes' to continue.")

print("We're done. Go take a break to stretch.")


# 22
# Modify the previous example so that every time the user types "yes",
# the turtle moves forward 10 units and turns left 45 degrees.


# 23
# Modify the previous example so that every time the user types "yes",
# it asks the user "How far do you want the turtle to move?".
# Then move the turtle forward the amount that the user specifies.


# 24
# Modify the previous example so that every time the user types "yes",
# it asks the user "What size square would you like to draw?".
# Then draw a square (using drawSquare) with the length that the user specifies.


# 25
# Try this.
lengths = [100, 50, 20, 200]
for leng in lengths:
    print(leng)

# 26
# Modify the previous example so that after it prints the length,
# it moves the turtle forward that far.
# (In other words, the first time that the loop runs, it should move forward 100 units,
#  the second time, it should move 50 units, etc)


# 27
# Modify the previous example so that it turns 90 degrees after each forward movement.


# 28
# Try this. Press the up and left keys on your keyboard.

def mvfwd():
    turtle.forward(100)

def turnleft():
    turtle.left(90)


turtle.onkeypress(mvfwd, "Up")
turtle.onkeypress(turnleft, "Left")
turtle.listen()

turtle.mainloop()


# 29
# Make it so if you press "Up" on your keyboard, the turtle will draw a square.


## Cool examples:
## https://gist.github.com/jkings454/b619cb0dc12901e8359393cad1b81c28
```
