import turtle
import time
import random
import sys


TOP = 400
BOTTOM = -400
LEFT_PADDLE = -500
LEFT_WALL = -550
RIGHT_PADDLE = 500
RIGHT_WALL = 550

wall_drawer = turtle.Turtle()
wall_drawer.hideturtle()
time.sleep(1)

# Turtles always start at (0, 0)
# So we must pick up the pen and go to the corner
wall_drawer.penup()
wall_drawer.goto(LEFT_WALL, TOP)
wall_drawer.pendown()
wall_drawer.pensize(12)

wall_drawer.goto(RIGHT_WALL, TOP)
wall_drawer.goto(RIGHT_WALL, BOTTOM)
wall_drawer.goto(LEFT_WALL, BOTTOM)
wall_drawer.goto(LEFT_WALL, TOP)


ball = turtle.Turtle()
ball.penup()
ball.shape("circle")

paddle1 = turtle.Turtle()
paddle1.color("purple")
paddle1.penup()
paddle1.shape("square")
paddle1.shapesize(5, 1)  # stretch so it looks like a paddle
paddle1.goto(LEFT_PADDLE, 0)

paddle2 = turtle.Turtle()
paddle2.penup()
paddle2.shape("square")
paddle2.shapesize(5, 1)
paddle2.goto(RIGHT_PADDLE, 0)






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


def ball_touching_wall():
    bx, by = ball.pos()
    if by >= TOP:
        time.sleep(5)
    if by <= BOTTOM:
        time.sleep(5)


def ricochet():
    print("TODO")

def handle_bounce():
    if ball_touching_wall():
        ricochet()
    print("TODO")
    # if ball.distance(paddle1)

    # ball.distance(paddle2)
    # if contact
        # set new angle


turtle.onkeypress(p1_up, "w")
turtle.onkeypress(p1_down, "s")
turtle.onkeypress(p2_up, "Up")
turtle.onkeypress(p2_down, "Down")

turtle.listen()

# init_direction = random.randint(0, 359)
init_direction = 270
ball.setheading(init_direction)

# loop forever
while True:
    ball.forward(1)
    handle_bounce()
