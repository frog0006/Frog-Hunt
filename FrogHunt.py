import turtle
import random
import time
import pygame
import math

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

# Load boing sound effects into a list
boing_sfx_list = [
    pygame.mixer.Sound('audios/boing1_sfx.mp3'),
    pygame.mixer.Sound('audios/boing2_sfx.mp3'),
    pygame.mixer.Sound('audios/boing3_sfx.mp3'),
    pygame.mixer.Sound('audios/boing4_sfx.mp3'),
    pygame.mixer.Sound('audios/boing5_sfx.mp3'),
    pygame.mixer.Sound('audios/boing6_sfx.mp3'),
    pygame.mixer.Sound('audios/boing7_sfx.mp3')
]

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
    speed += 0.5

def slowdown():
    global speed
    if speed > 0.5:
        speed -= 0.5

# Freeze player control
def freeze():
    global speed
    speed = 0

# Function to change the background image
def change_background(image):
    S.bgpic(image)

# Screen setup
width = 700
height = 500
S = turtle.Screen()
S.setup(width, height)
S.bgcolor('white')
S.title("Frog Hunt")
S.tracer(0)  # Turn off automatic screen updates for smoother animation

# Register and set background images
S.register_shape('images/pond.gif')
S.register_shape('images/rocks.gif')
S.register_shape('images/flower.gif')
S.register_shape('images/frogegg_img.gif')
S.register_shape('images/pond2.gif')
S.register_shape('images/pond3.gif')

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

# Set speed
speed = 1

# Initialize turning states
turning_left = False
turning_right = False

# Initialize global time variable
global time0
time0 = time.time()

# Set Player movement controls
turtle.listen()
turtle.onkeypress(turnleft, "Left")
turtle.onkeyrelease(stop_turnleft, "Left")
turtle.onkeypress(turnright, "Right")
turtle.onkeyrelease(stop_turnright, "Right")
turtle.onkey(speedup, "Up")
turtle.onkey(slowdown, "Down")
turtle.onkey(freeze, "f")
turtle.onkey(lambda: change_background('images/pond.gif'), "1")
turtle.onkey(lambda: change_background('images/pond2.gif'), "2")
turtle.onkey(lambda: change_background('images/pond3.gif'), "3")

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

# Helper function to move player
def move_player():
    angle_rad = math.radians(player.heading())
    dx = speed * math.cos(angle_rad)
    dy = speed * math.sin(angle_rad)
    player.setx(player.xcor() + dx)
    player.sety(player.ycor() + dy)

# Main game loop
def game_loop():
    global time0  # Declare time0 as global to modify it within the function

    move_player()
    
    # Handle turning
    if turning_left:
        player.left(5)
    if turning_right:
        player.right(5)
    
    # Set boundary
    if player.xcor() > boundary_width / 2:
        player.setx(boundary_width / 2)
        player.setheading(180 - player.heading())
        random.choice(boing_sfx_list).play()  # Play a random boing sound effect

    if player.xcor() < -boundary_width / 2:
        player.setx(-boundary_width / 2)
        player.setheading(180 - player.heading())
        random.choice(boing_sfx_list).play()  # Play a random boing sound effect

    if player.ycor() > boundary_height / 2:
        player.sety(boundary_height / 2)
        player.setheading(360 - player.heading())
        random.choice(boing_sfx_list).play()  # Play a random boing sound effect

    if player.ycor() < -boundary_height / 2:
        player.sety(-boundary_height / 2)
        player.setheading(360 - player.heading())
        random.choice(boing_sfx_list).play()  # Play a random boing sound effect

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
        crunch_sfx.play()
        global score
        score += 1
        score_pen.clear()
        score_pen.write(f'Frog Eggs: {score}', align="center", font=("Comic Sans MS", 12))
        
        # Play croak sound effect for every 3 frog eggs the player gets
        if score % 3 == 0:
            croak_sfx.play()

    S.update()
    S.ontimer(game_loop, 20)  # Call game_loop every 20 ms for smooth updates

# Initialize and start the game loop
game_loop()
turtle.done()