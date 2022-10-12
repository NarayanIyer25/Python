import turtle as t
import random
t.colormode(255)
color = [(225, 230, 235), (224, 235, 231), (58, 105, 145), (235, 227, 209), (131, 89, 61), (222, 201, 114), (218, 152, 76), (192, 144, 170), (148, 178, 200), (238, 225, 234), (139, 79, 102), (214, 94, 61), (67, 108, 90), (187, 81, 112), (132, 180, 136), (48, 154, 190), (65, 154, 92), (134, 135, 75), (183, 191, 201), (15, 54, 88), (30, 64, 107), (64, 51, 41), (215, 176, 192), (113, 40, 49), (168, 206, 188), (138, 34, 29), (230, 173, 164), (115, 123, 146), (152, 208, 219), (41, 60, 55), (75, 63, 49), (48, 73, 68), (75, 31, 41), (4, 110, 115)]

timmy = t.Turtle()
timmy.penup()
xsize = -200
ysize = -200
print(timmy.setposition(xsize , ysize))
for i in range(10):
    for i in range(10):
        timmy.dot(20,random.choice(color))
        timmy.forward(50) 
    ysize+=30
    timmy.goto(xsize,ysize)
screen = t.Screen()
screen.exitonclick()
