from turtle import Turtle
class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('turtle')
        self.penup()
        self.speed('fastest')
        self.left(90)
        self.goto(0, -280)
        self.showturtle()


    def up(self):
        if self.ycor()<280:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor()>-280:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)