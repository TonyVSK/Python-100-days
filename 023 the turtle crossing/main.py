# 1. Create screen
# 2. Create the turtle and the position
# 3. Make turtle move up or down
# 4. Create random squares 
# 5. Make squares moving
# 6. Create collision between squares and turtle
# 7. Create level system and make it changes everytime turtle reaches the end
# 8. Create end game if turtle colides with squares

from time import sleep
from turtle import Screen
from timmy import Timmy
from squares import Squares
from level import Level

# 1. Create screen
screen = Screen()
screen.bgcolor('white')
screen.setup(width=500, height=600)
screen.title('My Turtle Crossing Game')

# 2. Create the turtle and the position
timmy = Timmy()

# 3. Make turtle move up or down
screen.listen()
screen.onkey(timmy.up, 'Up')
screen.onkey(timmy.down, 'Down')

# 7. Create level system and make it changes everytime turtle reaches the end
level = Level()

# 4 and 5. Create random squares moving
squares = []
lvl = 1
game_is_on = True
while game_is_on == True:
    square = Squares(lvl)
    square.moveTurtle()
    while len(squares)<10:
        squares.append(square)
    for square in squares:
        square.moveTurtle()
        if square.get_xcord()<-200:
            squares.remove(square)
            square.hiding()
        # 6. Create collision between squares and turtle
        if timmy.distance(square.get_position())<35:
            print("Colisão detectada!")
            sleep(1)
        # 7. Create level system and make it changes everytime turtle reaches the end
        if timmy.ycor() >= 280:
            level.increaseLevel()
            timmy.goto(0, -280)
            lvl+=1