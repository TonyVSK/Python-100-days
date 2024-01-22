# 4. Detect collision with food

from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        x_position = randint(-280, 280)
        y_position = randint(-280, 280)
        self.goto(x_position, y_position)
        self.refresh()


    def refresh(self):
        x_position = randint(-280, 280)
        y_position = randint(-280, 280)
        self.goto(x_position, y_position)