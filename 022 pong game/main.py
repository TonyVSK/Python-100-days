# this game can be created in 8 steps:
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from random import randint
from time import sleep

# 1. Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My pong game')

line = Turtle()
line.hideturtle()
line.penup()
line.speed('fastest')
line.left(90)
line.color('white')
line.goto(0, -300)
for i in range(0, 16):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)
# screen.tracer(0)
# screen.update()

# 2. Create and move a paddle
paddle1 = Paddle(-260, 0)
screen.listen() # it will able to screen understand buttons being pressed with up, down, left and right
screen.onkey(paddle1.up, 'w')
screen.onkey(paddle1.down, 's')



# 3. Create another paddle
paddle2 = Paddle(260, 0)
screen.onkey(paddle2.up, 'Up')
screen.onkey(paddle2.down, 'Down')


# 4. Create the ball and make it move
ball = Ball()
direction = randint(1, 2) # 1 = right, 2 = left
ball.direction(direction)
game_is_on = True

# 8. Keep score
scoreboard1 = Scoreboard(1)
scoreboard2 = Scoreboard(2)

while game_is_on == True:
    ball.move()
# 5. Detect collision with walls
    if ball.ycor() > 260 or ball.ycor() < -260:  # considerando uma pequena margem para o teto/chão
        new_angle = 360 - ball.heading()
        ball.speed('fastest')
        ball.setheading(new_angle)
        ball.speed('slowest')
        ball.forward(10)

# 6. Detect collision with paddles
    if paddle1.distance(ball)<40 or paddle2.distance(ball)<40:
        if direction == 1:
            direction = 2
            ball.direction(direction)
        else:
            direction = 1
            ball.direction(direction)

# 7. Detect when paddle misses
    if ball.xcor()>270:
        sleep(1)
        ball.speed('fastest')
        ball.goto(0, 0)
        ball.speed('slowest')
        # 8. change score
        scoreboard1.newScore()
    if ball.xcor()<-270:
        sleep(1)
        ball.speed('fastest')
        ball.goto(0, 0)
        ball.speed('slowest')
        # 8. change score
        scoreboard2.newScore()






screen.exitonclick()