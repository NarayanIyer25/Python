from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
distance = [STARTING_MOVE_DISTANCE,MOVE_INCREMENT]


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.car_speeds = MOVE_INCREMENT

    def create_turtle(self):
        value = random.randint(1,4)
        if value == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.goto(250,0)
            new_car.color(random.choice(COLORS))
            Y = random.randint(-250,250)
            new_car.goto(300,Y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speeds)


    def car_speed(self):
        self.car_speeds += 10
