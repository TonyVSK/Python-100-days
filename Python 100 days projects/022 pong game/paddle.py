

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.speed('fastest')
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) # Isso cria um retângulo (raquete)
        self.penup()
        self.goto(x_position, y_position)
        self.showturtle()

    def up(self):
        if self.ycor()<250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor()>-250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
