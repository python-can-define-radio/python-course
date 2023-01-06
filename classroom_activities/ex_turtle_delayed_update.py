# inspired by https://pythonturtle.academy/tutorial-fireflies/

import turtle

bob = turtle.Turtle()
joe = turtle.Turtle()

## This turns off the animation. After this line, it will only update the 
## drawings when you run `turtle.update()`
turtle.tracer(0, 0)

for i in range(100):
    bob.forward(5)
    bob.left(2)
    joe.forward(5)
    joe.right(2)
    turtle.update()


turtle.mainloop()



