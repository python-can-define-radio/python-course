import turtle
import time


leo = turtle.Turtle()
donny = turtle.Turtle()
raph = turtle.Turtle()
mikey = turtle.Turtle()

nar = turtle.Turtle()
nar.penup()

myturtles = [leo, donny, raph, mikey]

## For each turtle in my list of turtles,
for t in myturtles:
    ## Set the shape of one of the turtles to "turtle"
    t.shape("turtle")
    t.shapesize(10)
    t.penup()

colors = ["blue", "purple", "red", "orange"]
names = ["Leo", "Donny", "Raph", "Mikey"]
amounts = [100, 200, 300, 400]
for colorCounter in range(0, 3 + 1):
    t = myturtles[colorCounter]
    color = colors[colorCounter]
    name = names[colorCounter]
    amount = amounts[colorCounter]

    t.color(color)
    t.forward(amount)
    nar.write(name, font=("Arial", 20, "normal"))
    nar.forward(100)
    time.sleep(2)
    

turtle.mainloop()
