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
    speed = speed + 0.1

def slowdown():
    global speed
    speed = speed - 0.1

#Screen setup
width = 600
height = 500
S = turtle.Screen()
S.setup(width, height)
S.bgcolor('green')
S.title("Frog Hunt")

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


while True:
    player.forward(speed)