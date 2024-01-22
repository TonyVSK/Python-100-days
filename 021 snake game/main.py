# There is 7 steps:
# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall - GameOver
# 7. Detect collision with tail - GameOver

from turtle import Screen
from food import Food
from snake import Snake
from time import sleep
from scoreboard import Scoreboard

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
# 4. Detect collision with food
food = Food()
# 5. Create a scoreboard
scoreboard = Scoreboard(0)
# 3. Control the snake
screen.listen() # it will able to screen understand buttons being pressed with up, down, left and right
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right, 'Right')
# with w, a, s, d buttons
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left,'a')
screen.onkey(snake.right, 'd')


# 2. Move the snake    
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # 4. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
    # 5. Create a scoreboard
        scoreboard.newScore()
    

screen.exitonclick()