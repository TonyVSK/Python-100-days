

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) # Isso cria um retângulo (raquete)
        self.penup()
        self.goto(x_position, y_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
