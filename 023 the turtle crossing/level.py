from turtle import Turtle
from time import sleep

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.speed('fastest')
        self.penup()
        self.goto(180, 240)
        self.levelNow = 0
        self.increaseLevel()

    
    def increaseLevel(self):
        self.levelNow += 1
        self.clear()
        self.write(f'level: {self.levelNow}', align='center', font=('Arial', 20, 'normal'))
        sleep(1)
