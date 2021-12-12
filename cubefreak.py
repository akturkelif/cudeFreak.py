import random
import turtle as t
import os

# Score varibales

player_a_score = 0
player_b_score = 0

win = t.Screen()    # creating a window
win.title("Ping-Pong Game") # Giving name to the game.
win.bgcolor('black')    # providing color to the HomeScreen
win.setup(width=800,height=600) # Size of the game panel 
win.tracer(0)   # which speed up's the game.

gameBoard[3][3]

def createSquare(range_x):
    index_x=0
    index_y=0
    color = ('red', 'yellow', 'green')
    for index_y in range(range_x):
        for index_x in range(range_x):
            random_color2 = random.choice(color)
            gameBoard[index_y][index_x] = random_color2
            paddle_slave2 = t.Turtle()
            paddle_slave2.speed(0)
            paddle_slave2.shape('square')
            paddle_slave2.color(random_color2)
            paddle_slave2.shapesize(stretch_wid=5,stretch_len=5)
            paddle_slave2.penup()
            paddle_slave2.goto(index_x*(-100), index_y*100)

i=0
j=0
for i in range (3)
    for j in range(3)
        print(gameBoard[i][j])
# Creating a right paddle for the game

paddle_master = t.Turtle()
paddle_master.speed(0)
paddle_master.shape('square')
paddle_master.shapesize(stretch_wid=5,stretch_len=5)
paddle_master.color('red')
paddle_master.penup()
paddle_master.goto(350,0)

# Creating a pong ball for the game

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5   # Setting up the pixels for the ball movement.
ball_dy = 1.5

# Creating a pen for updating the Score

pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Monaco',24,"normal"))


def paddle_master_up():
    y = paddle_master.ycor()
    y = y + 15
    paddle_master.sety(y)

# Moving right paddle down

def paddle_master_down():
    y = paddle_master.ycor()
    y = y - 15
    paddle_master.sety(y)

def paddle_master_r():
    x = paddle_master.xcor()
    x = x + 15
    paddle_master.setx(x)

# Moving right paddle down

def paddle_master_l():
    x = paddle_master.xcor()
    x = x - 15
    paddle_master.setx(x)
    
# Keyboard binding

win.listen()
win.onkeypress(paddle_master_up,"Up")
win.onkeypress(paddle_master_down,"Down")
win.onkeypress(paddle_master_r,"m")
win.onkeypress(paddle_master_l,"n")

createSquare(3)

# Main Game Loop

while True:
    win.update() # This methods is mandatory to run any game

    # Handling the collisions with paddles.
    
    if(paddle_master.ycor() >=0) and  (paddle_master.xcor() <=0 ):
        #print("XXXXXXXXXXXXXXX")
        paddle_master.ycor()

