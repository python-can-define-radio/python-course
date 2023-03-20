"""Arrow keys to move."""

import turtle
import random



WIDTH = 500
HEIGHT = 600
turtle.setup(WIDTH + 50, HEIGHT + 50)
turtle.bgcolor("lightblue")
 
playerState = {
    "health": 3
}
  
def touching(t1, t2):
    # type: (turtle.Turtle, turtle.Turtle) -> bool
    return t1.distance(t2) < 5
 
 
def checkCollision():
    for block in blocks:
        if touching(player, block):
            info.undo()  # erase the old "health" text on the screen
            info.write(f"Health: {playerState['health']}")
 
            playerState["health"] = playerState["health"] - 1
            player.undo()  # Make the player back up
 
 
def mvright():
    x, y = player.pos()
    if x < WIDTH / 2:
        player.setx(x + 20)
    checkCollision()
 
 
def mvleft():
    x, y = player.pos()
    if x > -WIDTH / 2:
        player.setx(x - 20)
    checkCollision()
 
 
def mvup():
    x, y = player.pos()
    if y < HEIGHT / 2:
        player.sety(y + 20)
    checkCollision()
 
 
def mvdown():
    x, y = player.pos()
    if y > -WIDTH / 2:
        player.sety(y - 20)
    checkCollision()
 
 
blocks = []
for count in range(30):
    block = turtle.Turtle()
    block.shape("square")
    block.color("black", "brown")
    block.speed(0)
    block.penup()
    x = random.randrange(-160, 160+20, 20)
    y = random.randrange(-160, 160+20, 20)
    block.goto(x, y)
    blocks.append(block)
 
 
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
 
info = turtle.Turtle()
info.penup()
info.goto(0, 300)
info.write(f"Health: {playerState['health']}")
 
turtle.onkeypress(mvright, "Right")
turtle.onkeypress(mvleft, "Left")
turtle.onkeypress(mvup, "Up")
turtle.onkeypress(mvdown, "Down")
turtle.listen()
 
turtle.mainloop()
