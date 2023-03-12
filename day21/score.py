from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('red')
        self.hideturtle()
        self.penup()
        self.setx(0)
        self.sety(280)
        self.write(f'Score:{self.score}', align='right', font=('Arial', 8, 'normal'))


    def increment(self):

        self.score +=1
        self.clear()
        self.write(f'Score:{self.score}', align='right', font=('Arial', 8, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='right', font=('Arial', 8, 'normal'))



