# Turtle Graphics Game
import turtle
import math
import random
import os


# Set up screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.bgpic('kbgame-bg.gif')
wn.tracer(3)

# Drawn border
mypen = turtle.Turtle()
mypen.penup()
mypen.color('grey')
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create a player
player = turtle.Turtle()
player.color('red')
player.shape('triangle')
player.penup()
player.speed(0)

# Create goals
maxGoals = 6
goals = []
for i in range(maxGoals):
    # Create goal
    goals.append(turtle.Turtle())
    goals[i].color('yellow')
    goals[i].shape('circle')
    goals[i].penup()
    goals[i].speed(0)
    goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))

# Set speed variable
speed = 1

# Set score variable
score = 0


# Define functions
def turnleft():
    player.left(30)


def turnright():
    player.right(30)


def increasespeed():
    global speed
    speed += 1


def decreasespeed():
    global speed
    if speed > 1:
        speed -= 1


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False

# Set keyboard binding
turtle.listen()
turtle.onkey(turnleft, 'Left')
turtle.onkey(turnright, 'Right')
turtle.onkey(increasespeed, 'Up')
turtle.onkey(decreasespeed, 'Down')

while True:
    # Move the player
    player.forward(speed)

    # Boundary checking for player
    if player.xcor() > 285 or player.xcor() < -285:
        player.right(180)
        os.system('afplay bounce.mp3&')
    if player.ycor() > 285 or player.ycor() < -285:
        player.right(180)
        os.system('afplay bounce.mp3&')

    # Move the goal
    for i in range(maxGoals):
        goals[i].forward(3)

        # Collision checking
        if isCollision(player, goals[i]):
            goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[i].right(random.randint(0, 360))
            os.system('afplay collision.mp3&')
            score += 1

            # Draw the score on screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-280, 310)
            score_string = 'Score: %s' % score
            mypen.write(score_string, False, font=('Arial', 14, 'normal'), align='left')

        # Boundary checking for goal
        if goals[i].xcor() > 285 or goals[i].xcor() < -285:
            goals[i].right(180)
            os.system('afplay bounce.mp3&')
        if goals[i].ycor() > 285 or goals[i].ycor() < -285:
            goals[i].right(180)
            os.system('afplay bounce.mp3&')



delay = raw_input('Press Enter to finish...')
