import turtle
import time
import random

paddle1 = turtle.Turtle()
paddle1.color("purple")
time.sleep(3)

paddle1.penup()
paddle1.shape("square")
paddle1.shapesize(5, 1)  # stretch so it looks like a paddle
paddle1.goto(-300, 0)

paddle2 = turtle.Turtle()
paddle2.penup()
paddle2.shape("square")
paddle2.shapesize(5, 1)
paddle2.goto(300, 0)

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")




def p1_up():
    # Get current x, y position of the paddle
    x, y = paddle1.pos()
    # Set the y position to whatever it was plus 10
    paddle1.sety(y + 10)

def p1_down():
    x, y = paddle1.pos()
    paddle1.sety(y - 10)

def p2_up():
    x, y = paddle2.pos()
    paddle2.sety(y + 10)

def p2_down():
    x, y = paddle2.pos()
    paddle2.sety(y - 10)

def handle_bounce():
    print("IN PROGRESS")
    # if ball.distance(paddle1)

    # ball.distance(paddle2)
    # if contact
        # set new angle


turtle.onkeypress(p1_up, "w")
turtle.onkeypress(p1_down, "s")
turtle.onkeypress(p2_up, "Up")
turtle.onkeypress(p2_down, "Down")

turtle.listen()

init_direction = random.randint(0, 359)
ball.setheading(init_direction)

# loop forever
while True:
    ball.forward(1)
    handle_bounce()
