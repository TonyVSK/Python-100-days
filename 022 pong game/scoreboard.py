# 5. Create a scoreboard

from turtle import Turtle




class Scoreboard(Turtle):
    def __init__(self, user):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.penup()
        
        

        if user == 1:

            self.goto(-40, 200)
            self.write('0', align='center', font=('Arial', 70, 'normal'))
        else:

            self.goto(40, 200)
            self.write('0', align='center', font=('Arial', 70, 'normal'))
        self.hideturtle()
        self.user = user
        self.newValue = 0



    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 20, 'normal'))

    def newScore(self):
        self.clear()
        self.newValue += 1
        self.write(f'{self.newValue}', align='center', font=('Arial', 70, 'normal'))