# There is 7 steps:
# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall - GameOver
# 7. Detect collision with tail - GameOver

from turtle import Turtle, Screen
from snake import Snake
from time import sleep

# Screen definitions
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snack Game')
screen.tracer(0)


# 1. Create a snake body
segments = []
starting_positions = [(0, 0),(-20, 0),(-40, 0)]

snake = Snake()

# 2. Move the snake
    
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

    snake.move()

screen.exitonclick()