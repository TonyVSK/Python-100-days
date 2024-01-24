# 1. Create screen
# 2. Create the turtle and the position
# 3. Make turtle move up or down
# 4. Create random squares 
# 5. Make squares moving
# 6. Create collision between squares and turtle
# 7. Create level system and make it changes everytime turtle get to the end
# 8. Create end game if turtle colides with squares


from turtle import Screen, Turtle
from timmy import Timmy
from squares import Squares

# 1. Create screen
screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.title('My Turtle Crossing Game')

# 2. Create the turtle and the position
timmy = Timmy()

# 3. Make turtle move up or down
screen.listen()
screen.onkey(timmy.up, 'Up')
screen.onkey(timmy.down, 'Down')

# 4. Create random squares moving
squares = Squares()

screen.exitonclick()