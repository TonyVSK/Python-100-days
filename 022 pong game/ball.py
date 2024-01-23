from turtle import Turtle
from random import randint



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('blue')
        self.speed('slowest')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.move()

    
    def move(self):
        newValue = randint(1, 2)
        if newValue == 1:
            self.speed('fastest')
            self.setheading(randint(-45, 45))
            self.speed('slowest')
        else:
            self.speed('fastest')
            self.setheading(randint(135, 225))
            self.speed('slowest')
        while True:
                self.forward(20)