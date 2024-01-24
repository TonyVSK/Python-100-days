from turtle import Turtle
from random import randint


COLORS = ['red', 'green', 'blue', 'yellow', 'gray', 'purple', 'pink']


class Squares(Turtle):
    def __init__(self, level):
        self.level = level
        self.new_segment = Turtle()
        self.new_segment.hideturtle()
        self.new_segment.shape('square')
        self.new_segment.shapesize(stretch_wid=1, stretch_len=5)
        self.new_segment.speed('fastest')
        self.new_segment.penup()
        self.segmentscolors = COLORS[randint(0, 6)]
        self.new_segment.color(self.segmentscolors)
        self.yposition = randint(-260, 300)
        self.xposition = 370
        self.new_segment.goto(self.xposition, self.yposition)
        self.new_segment.showturtle()

    
    def moveTurtle(self):
        self.new_segment.speed(3)
        self.new_segment.forward(-20*self.level)


    def get_position(self):
        return self.new_segment.pos()
    

    def get_xcord(self):
        return self.new_segment.xcor()
    
    def hiding(self):
        return self.new_segment.hideturtle()