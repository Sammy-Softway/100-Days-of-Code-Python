from turtle import Turtle
import random

POSITION = range(-280, 280)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_cord = random.choice(POSITION)
        y_cord = random.choice(POSITION)
        self.goto(x_cord, y_cord)