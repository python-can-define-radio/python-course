import turtle
from turtle import Turtle as Tur
from random import randint
import math

turtle.setup(1800, 1000)
turtle.bgcolor('skyblue')
wn = turtle.Screen()
wn.tracer(0)
tur = turtle.Turtle()

def drawBattlements(tur,x,y):
    my_goto(tur,x,y)
    drawWall(tur,x,y,3,3)

def drawCrenellations(tur,x,y,cols,fillcolor,pencolor):
    my_goto(tur,x,y)
    xoffset = (100/7)*2 
    for _ in range(cols+2):
        x += xoffset+14
        draw_rectangle(tur,x-93,y+75,23,30,fillcolor,pencolor,3)

def drawRoof(tur,x,y,w,h,color):
    my_goto(tur,x,y)
    tur.color("black")
    tur.fillcolor(color)
    tur.begin_fill()
    tur.goto(x,y)
    tur.goto(x+w//2,y+h)
    tur.goto(x+w,y)
    tur.goto(x,y)
    tur.end_fill()

def drawFlag(tur,x,y,w,h,color):
    my_goto(tur,x,y)
    tur.goto(x,y+h)
    tur.fillcolor(color)
    tur.begin_fill()
    tur.goto(x+w,y+h-10)
    tur.goto(x,y+h-20)
    tur.goto(x,y+h)
    tur.end_fill()

def drawWall(tur,x,y,rows,cols,crenellations=False):
    for row in range(rows):
        y_offset = y - (row * 25)
        if row % 2 == 0:
            for col in range(cols):
                x_offset = x + (col * 50)
                tur.pencolor("black")
                draw_rectangle(tur,x_offset,y_offset,50,25,"dimgray","black",4)
        else:
            for col in range(cols + 1):
                x_offset = x + (col * 50)
                if col == 0:
                    draw_rectangle(tur,x_offset,y_offset,25,25,"dimgray","black",4)
                elif col == cols:
                    draw_rectangle(tur,x_offset-25,y_offset,25,25,"dimgray","black",4)
                else:
                    draw_rectangle(tur,x_offset-25,y_offset,50,25,"dimgray","black",4)
    if crenellations == True:
        drawCrenellations(tur,-405,-150,20,"#2B2D2F","black")

def drawTower(tur,x,y,rows,cols,battlements=False):
    if battlements==True:
      drawWall(tur,x-25,y+25,rows,cols)
      drawBattlements(tur,x-50,y+50)
      drawCrenellations(tur,x,y,cols,"#2B2D2F","black")
    else:
      drawWall(tur,x-25,y+25,rows,cols)
      drawRoof(tur,x-50,y+50,(cols*50)+50,80,"#2B2D2F") 

def drawDoor(tur,x,y,w,h,color):
    my_goto(tur,(x-w//2),y)
    tur.fillcolor(color)
    tur.begin_fill()
    tur.goto(x-w//2,y+h-w//2)
    tur.goto(x+w//2,y+h-w//2)
    tur.goto(x+w//2,y)
    tur.goto(x-w//2,y)
    my_goto(tur,x,y+h-w)
    tur.end_fill()
    tur.begin_fill()  
    tur.circle(w//2)
    tur.end_fill()
    tur.goto(x,y+h)
    tur.goto(x,y)

def drawWindows(tur,color):
    x = 0
    y = 0
    for _ in range(2):
        for _ in range(4):
            draw_rectangle(tur,x+191.25,y+125,15,25,color,color)
            y -= 100
        x -= 350
        y = 0
    x = 0
    y = 0
    for _ in range(2):
        for _ in range(2):
            draw_rectangle(tur,x+492.5,y-75,15,25,color,color)
            y -= 100
        x -= 950
        y = 0

def drawOpenDoor(tur,x,y,w,h,color):
    my_goto(tur,(x-w//2),y)
    tur.begin_fill()
    tur.fillcolor(color)
    tur.goto(x-w,y)
    tur.goto(x-w,y+h)
    tur.circle(-w//2,90)
    tur.goto(x-w//2,y)
    tur.end_fill()
    tur.pu()
    tur.goto(x+w//2,y)
    tur.pd()
    tur.begin_fill()
    tur.goto(x+w//2,y+h-w//2)
    tur.seth(90)
    tur.circle(-w//2,90)
    tur.goto(x+w,y)
    tur.goto(x+w//2,y)
    tur.end_fill()

def drawPath(tur,x,y,color):
    my_goto(tur,x,y)
    tur.pensize(.5)
    tur.fillcolor(color)
    tur.begin_fill()
    tur.circle(-250, 90)
    tur.seth(0)
    tur.fd(90)
    tur.lt(90)
    tur.circle(255, 90)
    tur.end_fill()
    tur.pensize(2)

def drawGrass(tur,x,y,color):
    my_goto(tur,x,y)
    tur.fillcolor(color)
    tur.begin_fill()
    for peak in range(-1,18):
        tur.goto(-600+92.5*peak,randint(40,80))
    my_goto(tur,tur.xcor(),-500)
    my_goto(tur,-1000,-500)
    my_goto(tur,-1000,80)
    tur.end_fill()

def drawMountain(tur,side,x,y,capx,capy,caplength,color):
    my_goto(tur,x,y)
    draw_triangle(tur,x,y,side,color)
    drawSnowcap(tur,capx,capy,caplength)

def drawSnowcap(tur,x,y,fd,color="white"):
    my_goto(tur,x,y)
    tur.color(color)
    tur.begin_fill()
    tur.lt(60)
    tur.fd(fd)
    tur.rt(120)
    tur.fd(fd)
    tur.rt(randint(130,160))
    tur.fd(randint(20,40))
    tur.lt(randint(30,50))
    tur.fd(randint(20,40))
    tur.rt(randint(20,40))
    tur.fd(randint(0,20))
    tur.end_fill()

def drawFlower(tur,x,y,petal_col,flower_centre_col,stem_col):
    my_goto(tur,x,y)
    tur.color(stem_col)
    tur.rt(90)
    tur.fd(height / 30)
    tur.fd(-height / 30)
    my_goto(tur,x,y)
    tur.color(petal_col)
    for _ in range(6):
        tur.fd(12)
        tur.dot(10)
        tur.fd(-12)
        tur.lt(360 / 6)
    tur.color(flower_centre_col)
    tur.dot(20)

def drawTree(tur,x,y,color):
    my_goto(tur,x,y)
    draw_rectangle(tur,x,y,15,90,"saddlebrown","saddlebrown")
    tur.fd(8)
    tur.lt(90)
    tur.fd(100)
    tur.color(color)
    tur.begin_fill()
    for _ in range(10):
        tur.fd(30)
        tur.dot(50)
        tur.fd(-30)
        tur.lt(360 / 10)
    tur.end_fill()
    tur.rt(90)

def drawSun(tur,x,y,size=60,color="#FFDF22"):
    my_goto(tur,x,y)
    draw_circle(tur,x,y,size,color)

def drawCloud(tur,fd,first,second,third,fourth,fifth,color="white"):
    tur.fillcolor(color)
    tur.pencolor(color)
    tur.begin_fill()
    tur.circle(first)
    tur.fd(fd)
    tur.end_fill()
    tur.begin_fill()
    tur.circle(second)    
    tur.rt(90)
    tur.end_fill()
    tur.begin_fill()
    tur.circle(third)
    tur.rt(90)
    tur.end_fill()
    tur.begin_fill()
    tur.circle(fourth)
    tur.rt(90)
    tur.end_fill()
    tur.begin_fill()
    tur.circle(fifth)
    tur.rt(90)
    tur.end_fill()
    
def drawGuard(tur,x,y,eyecolor,skincolor,weapons=True,crown=False):
    # Draw the helmet/head/face
    my_goto(tur,x,y)
    draw_circle(tur,x,y,16,skincolor)
    my_goto(tur,x-6,y+21)
    tur.dot(8,"white") # lt eye
    tur.dot(5,eyecolor)  # lt eye
    my_goto(tur,x+6,y+21)
    tur.dot(8,"white") # rt eye
    tur.dot(5,eyecolor)  # rt eye
    my_goto(tur,x-8,y+11)
    tur.rt(90)
    tur.fillcolor("pink")
    tur.pencolor("pink")
    tur.begin_fill()
    tur.circle(8,180)  # Smile
    tur.end_fill()
    # Draw the body
    draw_rectangle(tur,x-20,y-53,40,50,"brown","brown") # body
    draw_rectangle(tur,x-30,y-10,10,50,skincolor,skincolor) # left arm
    draw_rectangle(tur,x+20,y-45,10,45,skincolor,skincolor) # right arm
    draw_rectangle(tur,x-15,y-90,10,40,"#765341","#765341") # left leg
    draw_rectangle(tur,x+5,y-90,10,40,"#765341","#765341") # right leg
    my_goto(tur,x-3,y+12) # nose
    tur.color("grey")
    tur.fd(3)
    tur.circle(3,160)
    tur.fd(3)
    if weapons == True:
        drawCOA(tur,-267,-30,35, 17.5)
        drawWeapons(tur,x,y)
    if crown == True:
        drawCrown(tur,x,y,1)
        drawCOA(tur,7,-215,35, 17.5)
    
def drawWeapons(tur,x,y):
    draw_circle(tur,x+20,y-40,22,"crimson")
    draw_circle(tur,x+20,y-35,17,"snow")
    draw_circle(tur,x+20,y-30,12,"crimson")
    draw_circle(tur,x+20,y-25,7,"blue")
    draw_star(tur,x+20,y-18,6,"snow")
    drawSword(tur,x,y)

def drawSword(tur,x,y):
    draw_rectangle(tur,x-27,y+30,5,20,"black","black")
    draw_rectangle(tur,x-35,y+45,20,5,"black","black")
    draw_rectangle(tur,x-30,y+50,10,30,"grey","grey")
    draw_triangle(tur,x-31,y+81,11,"grey")
    my_goto(tur,x-25,y+90)
    tur.color("#D3D3D3")
    tur.pensize(.3)
    tur.rt(90)
    tur.fd(40)

def drawScepter(tur,x,y,s):
    my_goto(tur,x,y)
    draw_rectangle(tur,x,y,10*s,100*s,"goldenrod","goldenrod",rot=-30)   
    draw_circle(tur,x+44*s,y+71*s,15*s,"royalblue") 
    draw_circle(tur,x+64*s,y+56*s,15*s,"royalblue") 
    draw_circle(tur,x+65*s,y+80*s,15*s,"crimson")
    drawCrown(tur,x+5*s,y+90*s,s,-30)

def drawCrown(tur,x,y,s,rot=0):
    draw_rectangle(tur,x-15*s,y+25*s,30*s,3*s,"goldenrod","goldenrod",rot=rot)
    draw_triangle(tur,x-15*s,y+29*s,5*s,"goldenrod",rot=rot)
    draw_triangle(tur,x-7*s,y+29*s,5*s,"goldenrod",rot=rot)
    draw_triangle(tur,x+1*s,y+29*s,5*s,"goldenrod",rot=rot)
    draw_triangle(tur,x+9*s,y+29*s,5*s,"goldenrod",rot=rot)

def drawCOA(tur,x,y,w,h):
    """Starts at top left of shield; coordinate is -w/2, h"""
    my_goto(tur,x,y)
    tur.begin_fill()
    tur.fillcolor("gray")
    tur.fd(w)  
    tur.rt(90)
    tur.fd(h) 
    tur.circle(-w/2, 180)  
    tur.fd(h)  
    tur.end_fill()
    drawCross(x,y,w,h)
    
def drawCross(x,y,w,h):
    cw = w/10
    draw_rectangle(tur,-cw/2+x+w/2,-h*0.6+y-h,cw,h*1.3,"red","red")
    draw_rectangle(tur,-w/4+x+w/2,h*.15+y-h,w*.5,cw,"red","red") 

def my_goto(tur: Tur,x,y,seth=0):
    tur.pu()
    tur.goto(x,y)
    tur.pd()
    tur.seth(seth)
    tur.pencolor("black")
    tur.pensize(2)

def draw_star(tur,x,y,r,color):
    my_goto(tur,x,y)
    tur.begin_fill()
    tur.color(color)
    tur.seth(162)
    tur.fd(r)
    tur.seth(0)
    tur.fillcolor(color)
    for _ in range(5):
        tur.fd(math.cos(math.radians(18)) * 2 * r)  # 2cos18°*r
        tur.rt(144)
    tur.end_fill()

def draw_triangle(tur,x,y,side,color,rot=0):
    my_goto(tur,x,y,rot)
    tur.begin_fill()
    tur.color(color)
    for _ in range(3):
        tur.fd(side)
        tur.lt(120)
    tur.end_fill()

def draw_circle(tur,x,y,radius,color):
    my_goto(tur,x,y)
    tur.begin_fill()
    tur.color(color)
    tur.circle(radius)
    tur.end_fill()

def draw_rectangle(tur,x,y,w,h,fillcolor,pencolor,pensize=1,rot=0):
    draw_pargram(tur,x,y,w,h,fillcolor,pencolor,pensize,90,rot)

def draw_pargram(tur,x,y,w,h,fillcolor,pencolor,pensize,angle,rot=0):
    my_goto(tur,x,y,rot)
    tur.begin_fill()
    tur.fillcolor(fillcolor)
    tur.pencolor(pencolor)
    tur.pensize(pensize)
    for _ in range(2):
        tur.fd(w)
        tur.lt(angle)
        tur.fd(h)
        tur.lt(180-angle)
    tur.end_fill()

width = 1200
height = 800  
sun_orbit_radius = 2800
sun_orbit_center_x = 100
sun_orbit_center_y = -2380
sun_pos = 0
sun_speed_while_visible = .5
sun_speed_while_hidden = 1 
first1 = randint(40,60)
second1 = randint(30,50)
third1 = randint(30,90)
fourth1 = randint(10,40)
fifth1 = randint(-50,50)
first2 = randint(-25,25)
second2 = randint(10,30)
third2 = randint(10,30)
fourth2 = randint(10,40)
fifth2 = randint(-20,20)
cloud = turtle.Turtle()
my_goto(cloud,-900,300)
cloud.ht()
cloud2 = turtle.Turtle()
my_goto(cloud2,-900,240)
cloud2.ht()
cloud3 = turtle.Turtle()
my_goto(cloud3,-900,400)
cloud3.ht()
sun = turtle.Turtle()
sun.ht()
door = turtle.Turtle()
door.ht()
opendoor = turtle.Turtle()
opendoor.ht()
window = turtle.Turtle()
window.ht()

drawGrass(tur,-1000,80,"limegreen")
drawMountain(tur,400,-475,-25,-325,235,100,"dimgray")
drawMountain(tur,400,100,-25,250,235,100,"dimgray")
drawMountain(tur,500,-200,-25,-25,279,150,"gray")
drawGuard(tur,-250,-25,"blue","#C89D7C")
drawWall(tur,-400,-100,9,17,True)
drawTower(tur,475,0,14,2,True)
drawTower(tur,-475,0,14,2,True)
drawTower(tur,-175,50,16,2)
drawTower(tur,175,50,16,2)
drawFlag(tur,200,180,30,40,"#FFF000")
drawFlag(tur,-150,180,30,40,"#FFF000")
drawPath(tur,-50,-300,"dimgrey")
drawDoor(tur,25,-300,100,175,"black")
drawGuard(tur,25,-210,"blue","#C89D7C",False,True)
draw_pargram(tur,200,-355,300,75,"#2b180c","#2b180c",1,45)
z = 525
for i in range(6): 
    drawFlower(tur,z,-285,"yellow","brown","green");z -=50
z = 500
for i in range(6): 
    drawFlower(tur,z,-305,"pink","brown","green");z -=50
z = 475
for i in range(6): 
    drawFlower(tur,z,-325,"skyblue","brown","green");z -=50
draw_pargram(tur,-550,-355,300,75,"#2b180c","#2b180c",1,45)
z = -225
for i in range(6): 
    drawFlower(tur,z,-285,"yellow","brown","green");z -=50
z = -500
for i in range(6): 
    drawFlower(tur,z,-305,"pink","brown","green");z +=50
z = -525
for i in range(6): 
    drawFlower(tur,z,-325,"skyblue","brown","green");z +=50
drawTree(tur,-750,-100,"forestgreen")
drawTree(tur,-625,-100,"forestgreen")
drawTree(tur,-600,-125,"forestgreen")
drawTree(tur,-700,-175,"forestgreen")
drawTree(tur,-805,-200,"forestgreen")
drawTree(tur,-600,-250,"forestgreen")
drawTree(tur,-800,-250,"forestgreen")
drawTree(tur,-725,-305,"forestgreen")
drawTree(tur,-675,-350,"forestgreen")
drawTree(tur,-800,-400,"forestgreen")
drawScepter(tur,-5,-175,.3)
tur._update()
tur.ht()

while True : 
    cloud.clear() 
    cloud2.clear() 
    cloud3.clear()
    sun.clear()
    window.clear()
    sun_x = sun_orbit_center_x + sun_orbit_radius * math.cos(math.radians(sun_pos))
    sun_y = sun_orbit_center_y + sun_orbit_radius * math.sin(math.radians(sun_pos))
    drawSun(sun, sun_x, sun_y)
    drawCloud(cloud3,.04,75,45,70,20,60)
    drawCloud(cloud,.08,50,40,60,20,50)
    drawCloud(cloud2,.15,25,15,30,20,20)
    if cloud.pos() >= (1000,200): 
        my_goto(cloud,-1000,200)     
    if cloud2.pos() >= (1000,140):
        my_goto(cloud2,-1000,140)
    if (-890,303) <= sun.pos() <= (1000,303):
        sun_pos += sun_speed_while_visible
        door.clear()
        drawOpenDoor(opendoor,25,-300,100,175,"saddlebrown")
        drawWindows(window,"black")
    else:
        sun_pos += sun_speed_while_hidden
        opendoor.clear()
        drawDoor(door,25,-300,100,175,"saddlebrown")
        drawWindows(window,"#FFFCBB")
    if sun_pos >= 180:
        sun_pos = 0
    wn.update()	 
