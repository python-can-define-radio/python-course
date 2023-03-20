import turtle
import time
import sys
 

def checkCollision():
    for loc in pastLocations:
        if p1.distance(loc) < 5:
            print("Game end.")
            sys.exit()
        if p2.distance(loc) < 5:
            print("Game end.")
            sys.exit()
        

def doTickActions():
    pastLocations.append(p1.pos())
    pastLocations.append(p2.pos())
    p1.stamp()
    p2.stamp()
    p1.forward(50)
    p2.forward(50)
    checkCollision()
 
 
def handleTick():
    doTickActions()
    turtle.ontimer(handleTick, 200)


def p1_left():
    p1.left(90)

def p1_right():
    p1.right(90)

def p2_left():
    p2.left(90)

def p2_right():
    p2.right(90)


p1 = turtle.Turtle()
p1.speed(0)
p1.pencolor("blue")
p1.fillcolor("blue")
p1.penup()
p1.goto(200, 0)
p1.pendown()
p1.shapesize(2)
p1.shape("turtle")
p1.setheading(180)


p2 = turtle.Turtle()
p2.speed(0)
p2.pencolor("red")
p2.fillcolor("red")
p2.penup()
p2.goto(-200, 0)
p2.pendown()
p2.shapesize(2)
p2.shape("turtle")
p2.setheading(0)

pastLocations = []


turtle.onkeypress(p1_left, "Left")
turtle.onkeypress(p1_right, "Right")
turtle.onkeypress(p2_left, "a")
turtle.onkeypress(p2_right, "d")
turtle.listen()

print("Starting in 4 seconds...")
time.sleep(4)
handleTick()

turtle.mainloop()
