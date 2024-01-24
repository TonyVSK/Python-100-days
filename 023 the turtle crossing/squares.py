from turtle import Turtle
from random import randint


COLORS = ['red', 'green', 'blue', 'yellow', 'gray', 'purple', 'pink']


class Squares(Turtle):
    def __init__(self):

        self.new_segment = Turtle()
        self.new_segment.hideturtle()
        self.new_segment.shape('square')
        self.new_segment.shapesize(stretch_wid=1, stretch_len=3)
        self.new_segment.speed('fastest')
        self.new_segment.penup()
        self.segmentscolors = COLORS[randint(0, 6)]
        self.new_segment.color(self.segmentscolors)
        self.yposition = randint(-300, 300)
        self.xposition = 300
        self.new_segment.goto(self.xposition, self.yposition)
        self.new_segment.showturtle()

    
    def moveTurtle(self):
        self.new_segment.speed(5)
        self.new_segment.forward(-20)


    def get_position(self):
        return self.new_segment.pos()
    

    def get_xcord(self):
        return self.new_segment.xcor()