from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-220, 260)
        self.active_level()

    def active_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.active_level()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER!\nSmashed by a car 😔 on level {self.level}", align="center", font=FONT)