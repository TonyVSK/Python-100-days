# this game can be created in 8 steps:
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

from turtle import Turtle, Screen
from paddle import Paddle

# 1. Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My pong game')
# screen.tracer(0)
# screen.update()

# 2. Create and move a paddle
paddle1 = Paddle(-260, 0)
# 3. Control the snake
screen.listen() # it will able to screen understand buttons being pressed with up, down, left and right
screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle1.down, 'Down')
# # with w, a, s, d buttons
# screen.onkey(snake.up, 'w')
# screen.onkey(snake.down, 's')
# screen.onkey(snake.left,'a')
# screen.onkey(snake.right, 'd')


screen.exitonclick()