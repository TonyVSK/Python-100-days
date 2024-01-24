from turtle import Turtle
class Timmy(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.shape('turtle')
        self.penup()
        self.speed('fastest')
        self.left(90)
        self.goto(0, -280)
        self.showturtle()