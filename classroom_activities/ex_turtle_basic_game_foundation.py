"""Arrow keys to move."""

import turtle


WIDTH = 500
HEIGHT = 600
turtle.setup(WIDTH + 50, HEIGHT + 50)
turtle.screensize(100, 3000, "lightblue")

playerState = {
    "health": 3
}


def touching(t1, t2):
    return t1.distance(t2) < 5


def checkCollision():
    if touching(player, block) or touching(player, block2):
        
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
            


block = turtle.Turtle()
block.shape("square")
block.color("black", "brown")
block.penup()
block.goto(-60, 20)

block2 = turtle.Turtle()
block2.shape("square")
block2.color("black", "brown")
block2.penup()
block2.goto(80, 0)

player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")

info = turtle.Turtle()
info.penup()
info.goto(0, 200)
info.write(f"Health: {playerState['health']}")

turtle.onkeypress(mvright, "Right")
turtle.onkeypress(mvleft, "Left")
turtle.onkeypress(mvup, "Up")
turtle.onkeypress(mvdown, "Down")
turtle.listen()

turtle.mainloop()


