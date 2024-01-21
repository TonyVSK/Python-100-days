from turtle import Turtle, Screen
from time import sleep


class Snake:
    # 1. Create a snake body
    def __init__(self):
        self.segments = []
        self.starting_positions = [(0, 0),(-20, 0),(-40, 0)]
        for i in range(0, 3):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.speed('fastest')
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.goto(self.starting_positions[i])
            self.segments.append(new_segment)
    # 2. Move the snake
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):  # no nosso caso, de 2 a 0, diminuir 1, ai ele pega a posição 2, 1 e 0
            new_x = self.segments[i-1].xcor()        # novo x do segmento 2 será a coordenada x do segmento 1; novo x do segmento1 será do seg 0; novo x  do 0 seria  a do segmento negativo,
            new_y = self.segments[i-1].ycor()        # mas como n tem, ele vai para o move forward na linha 46, depois o while volta. Y segue a mesma lógica
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.segments[0].left(90)

