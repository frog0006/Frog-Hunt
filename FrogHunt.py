import turtle
import random
import time
import pygame

# Initialize pygame mixer for audios
pygame.mixer.init()

# Loop play background sounds
nature_sfx = pygame.mixer.Sound('audios/nature_sfx.mp3')
water_sfx = pygame.mixer.Sound('audios/water_sfx.mp3')
nature_sfx.play(loops=-1)
water_sfx.play(loops=-1)

# Crunch sound effect whenever player collides with frog
crunch_sfx = pygame.mixer.Sound('audios/crunch_sfx.mp3')

# Play croak sound effect for every 3 frog eggs the player gets
croak_sfx = pygame.mixer.Sound('audios/croak_sfx.mp3')

# Define functions
def turnleft():
    global turning_left
    turning_left = True

def stop_turnleft():
    global turning_left
    turning_left = False

def turnright():
    global turning_right
    turning_right = True

def stop_turnright():
    global turning_right
    turning_right = False

def speedup():
    global speed
    speed = speed + 0.5

def slowdown():
    global speed
    if speed > 0.5:
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
S.register_shape('images/flower.gif')
S.register_shape('images/frogegg_img.gif')

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

# Add rocks to each corner
def add_rocks():
    positions = [(-width / 2 + 80, -height / 2 + 80), # Bottom left corner rock
                 (width / 2 - 80, -height / 2 + 80),  # Bottom right corner rock
                 (-width / 2 + 80, height / 2 - 80), # Top left corner rock
                 (width / 2 - 80, height / 2 - 80)]  # Top right corner rock
    
    for pos in positions:
        rock = turtle.Turtle()
        rock.shape('images/rocks.gif')
        rock.up()
        rock.speed(0)
        rock.setposition(pos)

add_rocks()

# Add flowers to each side of the boundary
def add_flowers():
    positions = [(0, boundary_height / 2),      # Top side
                 (0, -boundary_height / 2),     # Bottom side
                 (-boundary_width / 2, 0),      # Left side
                 (boundary_width / 2, 0)]       # Right side
    
    for pos in positions:
        flower = turtle.Turtle()
        flower.shape('images/flower.gif')
        flower.up()
        flower.speed(0)
        flower.setposition(pos)

add_flowers()

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

# Player setup
player = turtle.Turtle()
player.color('lightblue')
player.shape('triangle')
player.shapesize(stretch_wid=1, stretch_len=1.8)
player.up()

def draw_eyes(t):
    eye_size = 3
    eye_offset_x = 10
    eye_offset_y = 8

    # Draw the left eye
    t.goto(player.xcor() + eye_offset_x, player.ycor() + eye_offset_y)
    t.dot(eye_size, "black")

    # Draw the right eye
    t.goto(player.xcor() + eye_offset_x, player.ycor() - eye_offset_y)
    t.dot(eye_size, "black")

# Set speed
speed = 1

# Initialize turning states
turning_left = False
turning_right = False

# Set Player movement controls
turtle.listen()
turtle.onkeypress(turnleft, "Left")
turtle.onkeyrelease(stop_turnleft, "Left")
turtle.onkeypress(turnright, "Right")
turtle.onkeyrelease(stop_turnright, "Right")
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
score_pen.setposition(0, boundary_height / 2 + 10)
score_pen.write(f'Frog Eggs: {score}', align="center", font=("Comic Sans MS", 12))
score_pen.hideturtle()
frogegg = turtle.Turtle()
frogegg.shape('images/frogegg_img.gif')
frogegg.up()
frogegg.speed(0)
frogegg.setposition(70, boundary_height / 2 + 20)

time0 = time.time()
while True:
    player.forward(speed)
    
    # Handle turning
    if turning_left:
        player.left(5)
    if turning_right:
        player.right(5)

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

        # Play crunch sound effect
        crunch_sfx.play()

        score = score + 1
        score_pen.clear()
        score_pen.write(f'Frog Eggs: {score}', align="center", font=("Comic Sans MS", 12))
        
        # Play croak sound effect for every 3 frog eggs
        if score % 3 == 0:
            croak_sfx.play()