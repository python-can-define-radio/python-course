"""A few misc turtle examples."""

import turtle
import time
import random


turtle.shape("turtle")
time.sleep(1)


def squaredraw():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

colorChoices = ["chartreuse", "cadetblue", "maroon", "beige"]

def smile():
    turtle.pencolor("purple")
    turtle.fillcolor("pink")
    turtle.pensize(10)
    
    # Outline of face
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.setheading(90)
    
    # Move to and draw left eye
    turtle.penup()
    turtle.forward(130)
    turtle.setheading(180)
    turtle.forward(30)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    
    # Move to and draw right eye
    turtle.setheading(0)
    turtle.forward(60)
    turtle.pendown()
    turtle.forward(20)
    turtle.back(20)
    turtle.setheading(45)
    turtle.forward(20)
    turtle.back(20)
    turtle.penup()

    # Mouth
    turtle.setheading(180)
    turtle.forward(30)
    turtle.setheading(270)
    turtle.forward(60)
    turtle.setheading(180)
    turtle.forward(50)
    turtle.setheading(270)
    turtle.pendown()
    turtle.circle(55, 180)



    
    


smile()

while 1 > 0:
    turtle.penup()
    xpos = random.randint(-100, 300)
    ypos = random.randint(200, 400)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.pencolor(random.choice(colorChoices))
    turtle.circle(50)
    squaredraw()
