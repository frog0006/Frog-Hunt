import turtle
import random
import time


#Define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def speedup():
    global speed
    speed = speed + 0.5

def slowdown():
    global speed
    speed = speed - 0.5

#Freeze player control
def freeze():
    global speed
    speed = 0

#Screen setup
width = 600
height = 500
S = turtle.Screen()
S.setup(width, height)
S.bgcolor('green')
S.title("Frog Hunt")

#Register frog image
turtle.register_shape('images/frog_img.gif')

#Create the frog turtle
frog = turtle.Turtle()
frog.shape('images/frog_img.gif')
frog.up()
frog.speed(0)
frog.setposition(100,100)
#Draw Boundary
T = turtle.Turtle()
T.speed(0)
T.up()
T.setposition(-200,-200)
T.down()
T.pensize(3)
for side in range (4):
    T.forward(400)
    T.left(90)
T.hideturtle()

#Player setup
player = turtle.Turtle()
player.color('darkblue')
player.shape('triangle')
player.shapesize(stretch_wid=1, stretch_len = 1.5)
player.up()

#Set speed
speed = 1

#Set Player movement controls
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(speedup, "Up")
turtle.onkey(slowdown, "Down")
turtle.onkey(freeze, "f")

#score
score = 0

#Draw score board
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('black')
score_pen.up()
score_pen.setposition(-200,210)
score_pen.write(f'Frog Eggs: {score}')
score_pen.hideturtle()


time0 = time.time()
while True:
    player.forward(speed)
   #Set boundary
    if player.xcor() > 200 or player.xcor() <-200:
        player.setheading(180-player.heading())
    if player.ycor() > 200 or player.ycor() <-200:
        player.setheading(360-player.heading())

    if time.time() - time0 > 3:
        x = random.randint(-180,180)
        y = random.randint(-180,180)
        frog.setposition(x,y)
        time0 = time.time()
   #collision
    if abs(player.xcor()-frog.xcor()) < 20 and abs(player.ycor()-frog.ycor()) < 25:
        x = random.randint(-180,180)
        y = random.randint(-180,180)
        frog.setposition(x, y)
        time0 = time.time()

        score = score + 1
        score_pen.clear()
        score_pen.write(f'Frog Eggs: {score}')