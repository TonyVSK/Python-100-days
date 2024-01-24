from turtle import Screen, Turtle

# 1. Create screen
# 2. Create the turtle and the position
# 3. Make turtle move up or down
# 4. Create random squares moving
# 5. Create collision between squares and turtle
# 6. Create level system and make it changes everytime turtle get to the end
# 7. Create end game if turtle colides with squares


screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.title('My pong game')





timmy = Turtle()
timmy.hideturtle()
timmy.shape('turtle')
timmy.penup()
timmy.speed('fastest')
timmy.left(90)
timmy.goto(0, -280)
timmy.showturtle()

screen.exitonclick()