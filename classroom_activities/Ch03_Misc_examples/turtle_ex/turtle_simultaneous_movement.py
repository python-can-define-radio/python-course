# inspired by https://pythonturtle.academy/tutorial-fireflies/

import turtle
import time

bob = turtle.Turtle()
joe = turtle.Turtle()

## This turns off the animation. After this line, it will only update the 
## drawings when you run `turtle.update()`
## This allows for simultaneous movement of multiple turtles.
turtle.tracer(0, 0)

for i in range(500):
    bob.forward(5)
    bob.left(2)
    joe.forward(5)
    joe.right(2)
    turtle.update()
    time.sleep(0.01)


turtle.mainloop()
