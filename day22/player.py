from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.go_tostart()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True

    def go_tostart(self):
        self.goto(STARTING_POSITION)



