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
# Try this.

def dosomething():
    turtle.forward(100)

turtle.onkeypress(dosomething, "Up")
turtle.listen()
