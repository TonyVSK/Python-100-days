from turtle import Turtle, Screen
from random import randint




# 1. Screen settings and ask  an input from user about what turtle will win the race
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

# 2. Create our turtles
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
y = -100

for i in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230, y)
    tim.speed('slow')
    y += 40
    all_turtles.append(tim)


if user_bet:
    is_race_on = True

winner_color = 0

while is_race_on:
    for i in range(0, 6):    
        rand_distance = randint(0, 10)
        all_turtles[i].forward(rand_distance)
        if all_turtles[i].xcor()>230:
            winner_color = all_turtles[i].pencolor()
            break
    if winner_color != 0:
        break
print(winner_color)
if winner_color==user_bet:
    results = screen.textinput(title='Good! c:', prompt='Congrats! you won')
else:
    results = screen.textinput(title='oh :c!', prompt=f'Sorry... you lost, {winner_color} won')
screen.exitonclick()