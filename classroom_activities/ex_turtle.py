# 1
# Try this.
import turtle

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
something = input("Press enter to exit.")



# 2
# Try this.

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
something = input("Press enter to exit.")


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

something = input("Press enter to exit")

