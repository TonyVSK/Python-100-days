from turtle import Turtle, Screen
from random import randint



timmy = Turtle()
timmy.shape('turtle')

# Drawning a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)


# Drawing a Dashed Line
# for i in range(0, 10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# Drawing different shapes
# colors = ['red', 'green', 'blue', 'yellow', 'brown', 'pink']
# for i in range(3, 9):
#     for j in range(0, i):
#         timmy.color(colors[i-3])
#         graus = 360/i
#         timmy.forward(100)
#         timmy.left(graus)

# Generate a random walk
# colors = ['red', 'green', 'blue', 'yellow', 'brown', 'pink']
# timmy.pensize(10)
# timmy.speed('fastest')


# while True:
#     timmy.color(colors[randint(0, 5)])
#     computer = randint(1, 4)
#     if computer == 1:
#         timmy.right(0)
#     elif computer == 2:
#         timmy.right(90)
#     elif computer == 3:
#         timmy.right(180)
#     else:
#         timmy.right(270)
#     timmy.forward(30)

# Make a Spirograph
# colors = ['red', 'green', 'blue', 'yellow', 'brown', 'pink']
# timmy.speed('fastest')

# for i in range(0, 100):
#     timmy.color(colors[randint(0, 5)])
#     timmy.circle(100)
#     timmy.left(360/100)

# screen = Screen()
# screen.exitonclick()




timmy.speed('fastest')
timmy.hideturtle()
colors = ['red', 'green', 'blue', 'yellow', 'brown', 'pink']
timmy.penup()
x = -300
y = -300
timmy.goto(x, y)
timmy.pendown()
for i in range(0, 10):
    for j in range (0, 10):
        timmy.color(colors[randint(0, 5)])
        timmy.dot(30)
        timmy.penup()
        timmy.forward(40)
        timmy.pendown()
    timmy.penup()
    y+= 40
    timmy.goto(x, y)
    timmy.pendown()

screen = Screen()
screen.exitonclick()