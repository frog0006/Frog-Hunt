import turtle
import random
import time

# Define functions
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

# Freeze player control
def freeze():
    global speed
    speed = 0

# Screen setup
width = 700
height = 500
S = turtle.Screen()
S.setup(width, height)
S.bgcolor('white')
S.title("Frog Hunt")

# Register and set background images
S.register_shape('images/pond.gif')
S.bgpic('images/pond.gif')
S.register_shape('images/rocks.gif')

# Register frog image
turtle.register_shape('images/frog_img.gif')

# Create the frog turtle
frog = turtle.Turtle()
frog.shape('images/frog_img.gif')
frog.up()
frog.speed(0)
frog.setposition(100, 100)

# Draw Boundary
boundary_width = 600
boundary_height = 400
boundary_color = 'green'

# Function to draw the boundary lines and green rectangles outside the boundary
def draw_boundary():
    T = turtle.Turtle()
    T.speed(0)
    T.up()
    T.hideturtle()

    # Draw boundary lines
    T.color('black')
    T.pensize(3)
    T.setposition(-boundary_width / 2, -boundary_height / 2)
    T.down()
    for side in range(2):
        T.forward(boundary_width)
        T.left(90)
        T.forward(boundary_height)
        T.left(90)
    T.up()

    # Draw filled rectangles to hide overlapping parts of pond
    T.color(boundary_color)
    T.begin_fill()
    T.setposition(-width / 2, -height / 2)
    T.down()
    T.goto(-width / 2, height / 2)
    T.goto(-boundary_width / 2, height / 2)
    T.goto(-boundary_width / 2, -height / 2)
    T.goto(-width / 2, -height / 2)
    T.end_fill()
    T.up()

    T.begin_fill()
    T.setposition(boundary_width / 2, -height / 2)
    T.down()
    T.goto(boundary_width / 2, height / 2)
    T.goto(width / 2, height / 2)
    T.goto(width / 2, -height / 2)
    T.goto(boundary_width / 2, -height / 2)
    T.end_fill()
    T.up()

    T.begin_fill()
    T.setposition(-width / 2, boundary_height / 2)
    T.down()
    T.goto(width / 2, boundary_height / 2)
    T.goto(width / 2, height / 2)
    T.goto(-width / 2, height / 2)
    T.goto(-width / 2, boundary_height / 2)
    T.end_fill()
    T.up()

    T.begin_fill()
    T.setposition(-width / 2, -boundary_height / 2)
    T.down()
    T.goto(width / 2, -boundary_height / 2)
    T.goto(width / 2, -height / 2)
    T.goto(-width / 2, -height / 2)
    T.goto(-width / 2, -boundary_height / 2)
    T.end_fill()

draw_boundary()

# Add rocks to each corner
def add_rocks():
    positions = [(-width / 2 + 100, -height / 2 + 80), #Bottom left corner rock
                 (width / 2 - 90, -height / 2 + 80), #Bottom right corner rock
                 (-width / 2 + 100, height / 2 -80), #Top left corner rock
                 (width / 2 - 110, height / 2 - 90)] #Top right corner rock
    
    for pos in positions:
        rock = turtle.Turtle()
        rock.shape('images/rocks.gif')
        rock.up()
        rock.speed(0)
        rock.setposition(pos)

add_rocks()

# Player setup
player = turtle.Turtle()
player.color('lightblue')
player.shape('triangle')
player.shapesize(stretch_wid=1, stretch_len=1.8)
player.up()

# Set speed
speed = 1

# Set Player movement controls
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(speedup, "Up")
turtle.onkey(slowdown, "Down")
turtle.onkey(freeze, "f")

# Score
score = 0

# Draw score board
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('black')
score_pen.up()
score_pen.setposition(-boundary_width / 2, boundary_height / 2 + 10)
score_pen.write(f'Frog Eggs: {score}', font=("Comic Sans MS", 12))
score_pen.hideturtle()

time0 = time.time()
while True:
    player.forward(speed)
    # Set boundary
    if player.xcor() > boundary_width / 2 or player.xcor() < -boundary_width / 2:
        player.setheading(180 - player.heading())
    if player.ycor() > boundary_height / 2 or player.ycor() < -boundary_height / 2:
        player.setheading(360 - player.heading())

    if time.time() - time0 > 3:
        x = random.randint(int(-boundary_width / 2) + 20, int(boundary_width / 2) - 20)
        y = random.randint(int(-boundary_height / 2) + 20, int(boundary_height / 2) - 20)
        frog.setposition(x, y)
        time0 = time.time()
    # Collision
    if abs(player.xcor() - frog.xcor()) < 20 and abs(player.ycor() - frog.ycor()) < 25:
        x = random.randint(int(-boundary_width / 2) + 20, int(boundary_width / 2) - 20)
        y = random.randint(int(-boundary_height / 2) + 20, int(boundary_height / 2) - 20)
        frog.setposition(x, y)
        time0 = time.time()

        score = score + 1
        score_pen.clear()
        score_pen.write(f'Frog Eggs: {score}', font=("Comic Sans MS", 12))