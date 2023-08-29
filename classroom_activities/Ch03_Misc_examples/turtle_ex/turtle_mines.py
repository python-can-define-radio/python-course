import turtle
import random


def drawStar(x, y):
    starDrawer = turtle.Turtle()
    starDrawer.hideturtle()
    starDrawer.speed(0)
    starDrawer.penup()
    starDrawer.goto(x, y)
    starDrawer.pendown()
    starDrawer.color('red', 'yellow')
    starDrawer.begin_fill()
    ## This piece is from https://docs.python.org/3/library/turtle.html
    for x in range(0, 36):
        starDrawer.forward(200)
        starDrawer.left(170)
    starDrawer.end_fill()


def checkCollision():
    dist = player.distance(landmine)
    if dist < 20:
        x, y = landmine.pos()
        drawStar(x-100, y-5)

def mvup():
    x, y = player.pos()
    player.sety(y + 10)
    checkCollision()

def mvdown():
    x, y = player.pos()
    player.sety(y - 10)
    checkCollision()

def mvleft():
    x, y = player.pos()
    player.setx(x - 10)
    checkCollision()

def mvright():
    x, y = player.pos()
    player.setx(x + 10)
    checkCollision()


player = turtle.Turtle()
player.pensize(10)

player.shape("square")

turtle.onkeypress(mvup, "Up")
turtle.onkeypress(mvdown, "Down")
turtle.onkeypress(mvleft, "Left")
turtle.onkeypress(mvright, "Right")

landmine = turtle.Turtle()
landmine.penup()
landmine.shape("circle")
landmine.goto(random.randint(-400, 400), random.randint(-400, 400))
landmine.fillcolor("red")

turtle.listen()

turtle.mainloop()
