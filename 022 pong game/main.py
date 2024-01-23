# this game can be created in 8 steps:
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball

# 1. Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My pong game')
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

screen.exitonclick()