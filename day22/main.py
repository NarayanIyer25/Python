import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, 'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    player.level_up()
    car_manager.create_turtle()
    car_manager.move()
    for car in car_manager.all_cars:
       if player.distance(car)<30:
           game_is_on = False

    if player.level_up():
        car_manager.car_speed()
        player.go_tostart()
        scoreboard.level_up()
    screen.update()
scoreboard.game_over()
screen.exitonclick()