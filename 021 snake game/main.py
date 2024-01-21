# There is 7 steps:
# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall - GameOver
# 7. Detect collision with tail - GameOver

from turtle import Turtle, Screen

# Screen definitions
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snack Game')


# 1. Create a snake body
snake = []
x = 0
y= 0

for i in range(0, 3):
    new_segment = Turtle()
    new_segment.penup()
    new_segment.speed('fastest')
    new_segment.shape('square')
    new_segment.color('white')
    new_segment.goto(x, y)
    snake.append(new_segment)
    x -=20


# 2. Move the snake
    
    

screen.exitonclick()