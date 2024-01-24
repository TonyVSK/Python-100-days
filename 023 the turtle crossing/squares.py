from turtle import Turtle
from random import randint


COLORS = ['red', 'green', 'blue', 'yellow', 'gray', 'purple', 'pink']


class Squares(Turtle):
    def __init__(self):
        self.segments = []
        self.create_squares()
        self.head = self.segments[0]


    def create_squares(self):
        self.yposition = randint(-300, 300)
        self.xposition = 0
        self.segmentscolors = COLORS[randint(0, 6)]
        for i in range(0, 3):
            self.add_segment()
            self.xposition += 20



    # Extend snake
    def add_segment(self):
        new_segment = Turtle()
        new_segment.hideturtle()
        new_segment.speed('fastest')
        new_segment.penup()
        new_segment.shape('square')
        new_segment.color(self.segmentscolors)
        new_segment.goto(self.xposition, self.yposition)
        new_segment.showturtle()
        
        self.segments.append(new_segment)