from turtle import Turtle , Screen
import random
colors = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'orange']
direction = [0,90,180,270]
timmy = Turtle()
timmy.pensize(10)

for i in range(100):
    direct = random.choice(direction)
    color = random.choice(colors)
    timmy.color(color)
    timmy.left(direct)
    timmy.forward(20)
    

screen = Screen()
screen.exitonclick()
