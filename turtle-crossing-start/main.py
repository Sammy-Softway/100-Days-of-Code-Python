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

screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move()

    #Detect player successfully crossed the road
    if player.ycor() > 290:
        player.start_position()
        scoreboard.increase_level()
        car_manager.increase_speed()

    #Detect collision between player and car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()