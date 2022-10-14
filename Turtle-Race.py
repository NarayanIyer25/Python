from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=400,height=400)
choice = screen.textinput("Race",prompt="Choose the colour yo want")
color = ['red','blue','green','yellow','purple','orange']
yloc = [-40,-20,0,20,40,60 ]
tummies=[]

timmy = Turtle()
timmy.shape('turtle')
timmy.penup()
timmy.goto(-170,-40)
timmy.color(choice)
color.remove(choice)
tummies.append(timmy)
position = -40
for i in range(5):
    timmy = Turtle()
    timmy.shape('turtle')
    timmy.penup()
    position+=20
    timmy.goto(-170,position )
    colour = random.choice(color)
    if colour != choice:
        timmy.color(colour)
        color.remove(colour)
    tummies.append(timmy)
game_on = True
while game_on:
    x=180
    for turtle in tummies:
        value = random.randint(0,10)
        turtle.forward(value)
        if turtle.xcor()>=180:
            game_on = False
            if choice == turtle.pencolor():
                print("You Win")
            else:
                print(f"{turtle.pencolor()} win")

screen.exitonclick()
