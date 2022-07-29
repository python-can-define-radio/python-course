# 1
# Try this.
import turtle
import time

turtle.forward(100)
turtle.left(90)
turtle.forward(100)

time.sleep(99999)


# 2
# Try this.

turtle.forward(100)
turtle.right(90)
turtle.forward(100)

time.sleep(99999)


# 3
# Try making the turtle draw a square.


# 4
# Try making the turtle draw a triangle.


# 5
# Try this.
turtle.forward(50)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.forward(30)


# 6
# Draw three separate lines.


# 6b
# Draw three separate squares.


# 6c
# Draw three separate triangles.


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


# 9
# Copy and modify the previous example so that it draws three separate squares.

# 10
# Try this. Press the up and left keys on your keyboard.

def mvfwd():
    turtle.forward(100)

def turnleft():
    turtle.left(90)


turtle.onkeypress(mvfwd, "Up")
turtle.onkeypress(turnleft, "Left")
turtle.listen()

time.sleep(99999)

# 11
# Define a function to draw a square.


# 12
# Make it so if you press "s" on your keyboard, the turtle will draw a square.


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

leng = 100
drawTwoSides(leng)


# Some notes on terminology:
# In the previous example, `thelen` is a parameter of the function `drawTwoSides`.
# (The word "argument" is sometimes used instead of "parameter".)
# The functions that we defined before this did not have any parameters.
# You've already seen functions that use parameters, such as print() and turtle.forward().


# 17
# Modify the previous example so that `leng` comes from user input.
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

leng = int(input("How big should the square be?"))
drawSquare(leng)

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
