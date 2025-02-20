import turtle
import random
import time
import pygame
import math

#Initialize pygame mixer for audios
pygame.mixer.init()

#Loop play background sounds
nature_sfx = pygame.mixer.Sound('audios/nature_sfx.mp3')
water_sfx = pygame.mixer.Sound('audios/water_sfx.mp3')
nature_sfx.play(loops=-1)
water_sfx.play(loops=-1)

#Crunch sound effect whenever player collides with frog
crunch_sfx = pygame.mixer.Sound('audios/crunch_sfx.mp3')

#Play croak sound effect for every 3 frog eggs the player gets
croak_sfx = pygame.mixer.Sound('audios/croak_sfx.mp3')

#Load boing sound effects into a list
boing_sfx_list = [
    pygame.mixer.Sound('audios/boing1_sfx.mp3'),
    pygame.mixer.Sound('audios/boing2_sfx.mp3'),
    pygame.mixer.Sound('audios/boing3_sfx.mp3'),
    pygame.mixer.Sound('audios/boing4_sfx.mp3'),
    pygame.mixer.Sound('audios/boing5_sfx.mp3'),
    pygame.mixer.Sound('audios/boing6_sfx.mp3'),
    pygame.mixer.Sound('audios/boing7_sfx.mp3')
]

#Define functions
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

def freeze():
    global speed
    speed = 0

def change_background(bg_image):
    S.bgpic(bg_image)
    global frog_relocation_interval
    if bg_image == 'images/pond.gif':
        frog_relocation_interval = 4  #Slow relocation
        player.color('lightgreen')  #Change player color to light green
    elif bg_image == 'images/pond2.gif':
        frog_relocation_interval = 2.5  #Medium relocation
        player.color('lightblue')  #Change player color to light blue (current color)
    elif bg_image == 'images/pond3.gif':
        frog_relocation_interval = 1.5  #Fast relocation
        player.color('lightcoral')  #Change player color to light red
    global time0
    time0 = time.time()

def switch_to_pond1():
    change_background('images/pond.gif')
    display_mode_message('(Easy Mode)')

def switch_to_pond2():
    change_background('images/pond2.gif')
    display_mode_message('(Normal Mode)')

def switch_to_pond3():
    change_background('images/pond3.gif')
    display_mode_message('(Hard Mode)')

#Screen setup
width = 700
height = 500
S = turtle.Screen()
S.setup(width, height)
S.bgcolor('white')
S.title("Frog Hunt")
S.tracer(0)  #Turn off automatic screen updates for smoother animation

#Register and set background images
S.register_shape('images/pond.gif')
S.register_shape('images/pond2.gif')
S.register_shape('images/pond3.gif')
S.register_shape('images/rocks.gif')
S.register_shape('images/flower.gif')
S.register_shape('images/frogegg_img.gif')

#Register and create frog image and turtle
turtle.register_shape('images/frog_img.gif')
frog = turtle.Turtle()
frog.shape('images/frog_img.gif')
frog.up()
frog.speed(0)
frog.setposition(100, 100)

#Draw Boundary
boundary_width = 600
boundary_height = 400
boundary_color = 'green'

#Add rocks to each corner
def add_rocks():
    positions = [(-width / 2 + 80, -height / 2 + 80), #Bottom left corner rock
                 (width / 2 - 80, -height / 2 + 80),  #Bottom right corner rock
                 (-width / 2 + 80, height / 2 - 80), #Top left corner rock
                 (width / 2 - 80, height / 2 - 80)]  #Top right corner rock
    
    for pos in positions:
        rock = turtle.Turtle()
        rock.shape('images/rocks.gif')
        rock.up()
        rock.speed(0)
        rock.setposition(pos)

add_rocks()

#Add flowers to each side of the boundary
def add_flowers():
    positions = [(0, boundary_height / 2),      #Top side
                 (0, -boundary_height / 2),     #Bottom side
                 (-boundary_width / 2, 0),      #Left side
                 (boundary_width / 2, 0)]       #Right side
    
    for pos in positions:
        flower = turtle.Turtle()
        flower.shape('images/flower.gif')
        flower.up()
        flower.speed(0)
        flower.setposition(pos)

add_flowers()

#Function to draw the boundary lines and green rectangles outside the boundary
def draw_boundary():
    T = turtle.Turtle()
    T.speed(0)
    T.up()
    T.hideturtle()

    #Draw boundary lines
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

    #Draw filled rectangles to hide overlapping parts of pond
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

#Player setup
player = turtle.Turtle()
player.color('lightblue')  #Default color
player.shape('triangle')
player.shapesize(stretch_wid=1, stretch_len=1.8)
player.up()

#Initialize frog relocation interval with a default value
frog_relocation_interval = 1.5  #Default medium pace

#Initialize speed
speed = 1

#Initialize turning states
turning_left = False
turning_right = False

#Initialize global time variable
global time0
time0 = time.time()

#Set Player movement controls
turtle.listen()
turtle.onkeypress(turnleft, "Left")
turtle.onkeyrelease(stop_turnleft, "Left")
turtle.onkeypress(turnright, "Right")
turtle.onkeyrelease(stop_turnright, "Right")
turtle.onkey(speedup, "Up")
turtle.onkey(slowdown, "Down")
turtle.onkey(freeze, "f")

#Score
score = 0

#Draw score board
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

#Draw message pen for displaying messages
message_pen = turtle.Turtle()
message_pen.speed(0)
message_pen.color('lightblue')
message_pen.up()
message_pen.hideturtle()

#Timer pen for displaying challenge minigame timer
timer_pen = turtle.Turtle()
timer_pen.speed(0)
timer_pen.color('black')
timer_pen.up()
timer_pen.hideturtle()

#Initialize difficulty states
normal_unlocked = False
hard_unlocked = False
challenge_mode = False
challenge_start_time = 0

#Helper function to move player
def move_player():
    angle = player.heading()
    radian_angle = math.radians(angle)
    dx = speed * math.cos(radian_angle)
    dy = speed * math.sin(radian_angle)
    player.setx(player.xcor() + dx)
    player.sety(player.ycor() + dy)

#Function to display a message at the top left corner of the screen for a given duration
def display_message(message, duration=3):
    message_pen.clear()
    message_pen.setposition(-width / 2 + 10, height / 2 - 30)  #Top left corner
    message_pen.write(message, align="left", font=("Comic Sans MS", 16, "bold"))
    S.ontimer(message_pen.clear, duration * 1000)

#Function to display mode message at the top left corner of the screen indefinitely
def display_mode_message(message):
    message_pen.clear()
    message_pen.setposition(-width / 2 + 10, height / 2 - 30)  #Top left corner
    message_pen.write(message, align="left", font=("Comic Sans MS", 16, "bold"))

#Function to enable all difficulty keys
def enable_all_difficulty_keys():
    turtle.onkey(switch_to_pond1, "1")
    turtle.onkey(switch_to_pond2, "2")
    turtle.onkey(switch_to_pond3, "3")

#Function to enable normal difficulty key
def enable_normal_difficulty_key():
    turtle.onkey(switch_to_pond1, "1")
    turtle.onkey(switch_to_pond2, "2")

#Function to disable difficulty keys
def disable_difficulty_keys():
    turtle.onkey(None, "1")
    turtle.onkey(None, "2")
    turtle.onkey(None, "3")

#Function to start the challenge minigame
def start_challenge():
    global challenge_mode
    global challenge_start_time
    global score

    score = 0
    score_pen.clear()
    score_pen.write(f'Frog Eggs: {score}', align="center", font=("Comic Sans MS", 12))
    
    challenge_mode = True
    challenge_start_time = time.time()
    disable_difficulty_keys()
    change_background('images/pond.gif')  #Start with easy difficulty
    display_message("Challenge Started!", 3)
    S.ontimer(lambda: display_mode_message("(Easy Mode)"), 3000)

#Function to update and display the challenge timer
def update_timer():
    if challenge_mode:
        elapsed_time = int(time.time() - challenge_start_time)
        timer_pen.clear()
        timer_pen.setposition(width / 2 - 100, height / 2 - 30)  #Top right corner
        timer_pen.write(f'Time: {elapsed_time}s', align="right", font=("Comic Sans MS", 16, "bold"))

#Main game loop
def game_loop():
    global time0  #Declare time0 as global to modify it within the function
    global score
    global normal_unlocked
    global hard_unlocked
    global challenge_mode

    move_player()
    
    #Handle turning
    if turning_left:
        player.left(5)
    if turning_right:
        player.right(5)
    
    #Set boundary
    if player.xcor() > boundary_width / 2:
        player.setx(boundary_width / 2)
        player.setheading(180 - player.heading())
        random.choice(boing_sfx_list).play()  #Play a random boing sound effect

    if player.xcor() < -boundary_width / 2:
        player.setx(-boundary_width / 2)
        player.setheading(180 - player.heading())
        random.choice(boing_sfx_list).play()  #Play a random boing sound effect

    if player.ycor() > boundary_height / 2:
        player.sety(boundary_height / 2)
        player.setheading(360 - player.heading())
        random.choice(boing_sfx_list).play()  #Play a random boing sound effect

    if player.ycor() < -boundary_height / 2:
        player.sety(-boundary_height / 2)
        player.setheading(360 - player.heading())
        random.choice(boing_sfx_list).play()  #Play a random boing sound effect

    if time.time() - time0 > frog_relocation_interval:
        x = random.randint(int(-boundary_width / 2) + 20, int(boundary_width / 2) - 20)
        y = random.randint(int(-boundary_height / 2) + 20, int(boundary_height / 2) - 20)
        frog.setposition(x, y)
        time0 = time.time()

    #Collision
    if abs(player.xcor() - frog.xcor()) < 20 and abs(player.ycor() - frog.ycor()) < 25:
        x = random.randint(int(-boundary_width / 2) + 20, int(boundary_width / 2) - 20)
        y = random.randint(int(-boundary_height / 2) + 20, int(boundary_height / 2) - 20)
        frog.setposition(x, y)
        crunch_sfx.play()
        score += 1
        score_pen.clear()
        score_pen.write(f'Frog Eggs: {score}', align="center", font=("Comic Sans MS", 12))
        
        #Reset timer after catching the frog
        time0 = time.time()
        
        #Play croak sound effect for every 3 frog eggs the player gets
        if score % 3 == 0:
            croak_sfx.play()

        if challenge_mode:
            if score == 20:
                switch_to_pond2()
                display_mode_message("(Normal Mode)")
            elif score == 40:
                switch_to_pond3()
                display_mode_message("(Hard Mode)")

        #Switch difficulties based on the score if not in challenge mode
        if not challenge_mode:
            if score == 20:
                switch_to_pond2()
                enable_normal_difficulty_key()
                display_message("Normal Difficulty Unlocked!", 3)  #Display message for 3 seconds
                normal_unlocked = True

            #Enable all difficulty keys when the score reaches 40
            if score == 40:
                switch_to_pond3()
                enable_all_difficulty_keys()
                display_message("Hard Difficulty Unlocked!", 3)  #Display message for 3 seconds
                hard_unlocked = True

    if challenge_mode:
        update_timer()
        if score >= 50:
            challenge_mode = False
            total_time = int(time.time() - challenge_start_time)
            display_mode_message(f"Challenge Complete! Time: {total_time}s")
            if normal_unlocked:
                enable_normal_difficulty_key()
            if hard_unlocked:
                enable_all_difficulty_keys()

    S.update()
    S.ontimer(game_loop, 20)  #Call game_loop every 20 ms for smooth updates

#Disable difficulty keys initially
disable_difficulty_keys()

#Set up key binding for starting challenge minigame
turtle.onkey(start_challenge, "4")

#Initialize and start the game loop
change_background('images/pond.gif')  #Set initial background
game_loop()
turtle.done()