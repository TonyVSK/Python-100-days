from turtle import Turtle, Screen
from time import sleep


MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]

class Snake:
    # 1. Create a snake body
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in range(0, 3):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.speed('fastest')
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.goto(STARTING_POSITIONS[i])
            self.segments.append(new_segment)

    # 2. Move the snake
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):  # no nosso caso, de 2 a 0, diminuir 1, ai ele pega a posição 2, 1 e 0
            new_x = self.segments[i-1].xcor()        # novo x do segmento 2 será a coordenada x do segmento 1; novo x do segmento1 será do seg 0; novo x  do 0 seria  a do segmento negativo,
            new_y = self.segments[i-1].ycor()        # mas como n tem, ele vai para o move forward na linha 46, depois o while volta. Y segue a mesma lógica
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    # 3. Control the snake
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
