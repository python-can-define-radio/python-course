"""Based on the code from turtle_mines."""


import turtle
import random



def colorAdjust(dist, sensor):
    # type: (float, turtle.Turtle) -> None
    oneover = int(40000 * 1 / dist)
    colorsetting = min(oneover, 255)
    sensor.fillcolor(colorsetting, 0, 0)


def handleMove():
    for sensor in sensors:
        dist = player.distance(sensor)
        colorAdjust(dist, sensor)


def mvup():
    x, y = player.pos()
    player.sety(y + 10)
    handleMove()

def mvdown():
    x, y = player.pos()
    player.sety(y - 10)
    handleMove()

def mvleft():
    x, y = player.pos()
    player.setx(x - 10)
    handleMove()

def mvright():
    x, y = player.pos()
    player.setx(x + 10)
    handleMove()


player = turtle.Turtle()
player.penup()

player.shape("square")

turtle.onkeypress(mvup, "Up")
turtle.onkeypress(mvdown, "Down")
turtle.onkeypress(mvleft, "Left")
turtle.onkeypress(mvright, "Right")

turtle.colormode(255)

sensors = []
for x in range(10):
    _sensor = turtle.Turtle()
    _sensor.penup()
    _sensor.shape("circle")
    _sensor.goto(random.randint(-400, 400), random.randint(-400, 400))
    sensors.append(_sensor)


turtle.listen()

turtle.mainloop()
