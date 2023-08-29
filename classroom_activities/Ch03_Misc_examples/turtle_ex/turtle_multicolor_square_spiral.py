"""Multi-color squares spirialing outward"""
import turtle
import random

turtle.speed(0)
turtle.pensize(10)
colors = ["purple", "green", "blue", "red"]
size = 100
while True:
    randomcol = random.choice(colors)
    size += 5
    turtle.pencolor(randomcol)
    turtle.forward(size)
    turtle.left(91)
    turtle.forward(size)
    turtle.left(91)
    turtle.forward(size)
    turtle.left(91)
    turtle.forward(size)
    turtle.left(91)

"""---------------------------------"""
