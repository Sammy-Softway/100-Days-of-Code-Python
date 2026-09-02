from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.setheading(180)
            random_y = random.randint(-200, 200)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT