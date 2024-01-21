# There is 7 steps:
# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall - GameOver
# 7. Detect collision with tail - GameOver

from turtle import Turtle, Screen
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

for i in range(0, 3):
    new_segment = Turtle()
    new_segment.penup()
    new_segment.speed('fastest')
    new_segment.shape('square')
    new_segment.color('white')
    new_segment.goto(starting_positions[i])
    segments.append(new_segment)


# 2. Move the snake
    
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

    for i in range(len(segments)-1, 0, -1):  # no nosso caso, de 2 a 0, diminuir 1, ai ele pega a posição 2, 1 e 0
        new_x = segments[i-1].xcor()        # novo x do segmento 2 será a coordenada x do segmento 1; novo x do segmento1 será do seg 0; novo x  do 0 seria  a do segmento negativo,
        new_y = segments[i-1].ycor()        # mas como n tem, ele vai para o move forward na linha 46, depois o while volta. Y segue a mesma lógica
        segments[i].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()