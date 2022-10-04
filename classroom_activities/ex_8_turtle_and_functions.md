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
```

Exercises:

```python3
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
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
```

As described in the [chapter in Arcade Academy about functions](https://learn.arcade.academy/en/latest/chapters/08_functions/functions.html):

> "Defining a function doesn’t cause the computer to _do_ anything. It is like giving a recipe to the computer. Give someone a recipe for banana bread and they know how to make it. They haven’t actually made it yet, they just know how. You have to _tell_ them to make banana bread. That is, after we **define** the function we must **call** the function before the code in it runs. To call a function, type the function name and follow it by parenthesis. Do not use **def**, that is only used when we define what the function does, not when we tell the computer to run it."

So, let's call (run) the function that we defined.

```python3
## 5 continued
## This is the same definition as before.
def drawTriangle():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    # Don't put the mainloop here.

## It's important to NOT indent the following lines.
turtle.pensize(15)
turtle.speed(1)
turtle.pencolor("red")
drawTriangle()    # This command calls (runs) drawTriangle.
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
## Try this.
## It uses the drawTriangle function that we defined before.
## You can either copy/paste the drawTriangle definition,
## or simply leave that portion uncommented in the previous example.
turtle.speed(1)
drawTriangle()
turtle.left(20)
drawTriangle()
turtle.left(20)
drawTriangle()


## 5c
## Copy and modify the previous example.
## In this version, draw a fourth triangle, using orange as the color.
## You should only need to add three lines of code:
##   turn left 20 degrees
##   set the pen color to orange
##   draw the triangle
## Make sure to add those two lines **before** the mainloop.


## 5d
## Copy and modify the previous example.
## In this version, we still keep the orange triangle, but just before drawing 
## the orange triangle, we're going to change the pen size using 
##     turtle.pensize(10)


## 5e
## Copy and modify the previous example.
## In this version, just before drawing each triangle, pick a different pencolor.


## 5f
## Copy and modify the previous example.
## In this version, before each of the four triangles, set the pensize.
## Set the pensize to 40 before the first triangle,
## 30 before the second triangle,
## 20 before the third,
## 10 before the fourth.
```

Let's try drawing two separate triangles.

```python3
## 6
## Try this.
drawTriangle()
turtle.forward(300)
drawTriangle()
```

You'll see that the two triangles are attached by a connecting line. Let's fix it:

```python3
## 6b
## Copy and modify the previous example.
## In this version, do this:
##  draw a triangle
##  stop drawing (pick up the pen)
##  move forward 300 units
##  start drawing (put down the pen)
##  draw a triangle
```

Idea: What if we put the pendown and penup commands inside of the triangle drawing function?

```python3
## 7
## Try this. How does it differ from our original drawTriangle function?
def drawTrianglePen():
    turtle.pendown()
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.penup()

drawTrianglePen()
turtle.forward(300)
drawTrianglePen()


# 7b
# Using drawTrianglePen, draw three separate triangles.
# For extra fun, make them different colors.


# 7c
# Make a drawSquare function. Using that function, draw five separate squares.
# (This should only require about 10 to 25 lines of code. If you have more than
# that, look back at how drawTrianglePen helped to avoid repeated code.)


# 8
# Try this.
def drawC():
    turtle.setheading(180)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(70)
    
drawC()
turtle.penup()
turtle.forward(200)
turtle.pendown()
drawC()


# 8b
# Copy and modify the previous example so that it draws two Z's
# instead of two C's.
```

Our drawTriangle function works well, but what if we wanted to be able to draw different size triangles?

We could define `drawBigTriangle` and `drawSmallTriangle`, but that would be a lot of redundant code.

The better way is to use **arguments**, also called **parameters**. (_Those two terms are not perfectly synonymous, but they are often used interchangeably._)

Example:

```python3
def drawTriangleLength(thelength):
    turtle.forward(thelength)
    turtle.left(120)
    turtle.forward(thelength)
    turtle.left(120)
    turtle.forward(thelength)
    turtle.left(120)

turtle.pensize(10)
turtle.pencolor("red")
drawTriangleLength(50)
turtle.pencolor("green")
drawTriangleLength(100)
```

In that example, `thelength` is a **parameter**.

Exercises:

```python3
# 11
# Copy and modify the previous example.
# After the red and green triangles, draw a blue triangle with a side length of 150.
# This should only require adding two lines of code.


# 11b
# Copy your earlier drawSquare function.
# Name the new version drawSquareLength.
# Change it so that you can specify the length, just like in drawTriangleLength.
# Then,
# Once you've defined drawSquareLength, 
# try this. It should draw three squares of different sizes.
# NOTE: You'll get an error if you haven't yet defined drawSquareLength.
drawSquareLength(50)
drawSquareLength(100)
drawSquareLength(150)
```

Now, let's incorporate `input` to let the user pick the size of the shape.

```python3
# 14
# Try this.
linelength = 100
turtle.forward(linelength)


# 14b
# Modify the previous example to ask the user what length of line to draw.


# 15
# Try this. You'll need the drawTriangleLength function from earlier.
triLength = int(input("How big do you want the triangle to be?"))
drawTriangleLength(triLength)


# 15b
# Ask the user for three lengths.
# Draw a red   triangle with the first  user-specified length.
# Draw a green triangle with the second user-specified length.
# Draw a blue  triangle with the third  user-specified length.


# 16
# Try this. You'll need your drawSquareLength function from earlier.
mylength = int(input("How big should the square be?"))
drawSquareLength(mylength)


# 16b
# Repeat the three-triangles exercise, but with squares.
# (ask for three lengths; draw red, green, blue)
```

Functions can have multiple parameters:

```python3
def drawTriangle3(thelength, thecolor):
    turtle.pencolor(thecolor)
    turtle.forward(thelength)
    turtle.left(120)
    turtle.forward(thelength)
    turtle.left(120)
    turtle.forward(thelength)
    turtle.left(120)

drawTriangle3(100, "red")
drawTriangle3(50, "purple")
drawTriangle3(200, "cyan")


# 17
# Make a drawTriangle4 function.
# It should be identical to drawTriangle3,
# but should have the penup and pendown commands that we used earlier
# so that each triangle is separate.
# Test it with this code:
drawTriangle4(100, "red")
turtle.forward(200)
drawTriangle4(50, "purple")
turtle.forward(200)
drawTriangle4(200, "cyan")
```


```python3
# 19
# Try this. Press the up and left keys on your keyboard.

def mvfwd():
    turtle.forward(100)

def turnleft():
    turtle.left(90)


turtle.onkeypress(mvfwd, "Up")
turtle.onkeypress(turnleft, "Left")
turtle.listen()

turtle.mainloop()


# 19b
# Make it so if you press "Up" on your keyboard, the turtle will draw a square.
```

Before continuing to the following exercises, do a few of the `if`, `for`, and `while` exercises.

```python3
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


## Cool examples:
## https://gist.github.com/jkings454/b619cb0dc12901e8359393cad1b81c28
```
