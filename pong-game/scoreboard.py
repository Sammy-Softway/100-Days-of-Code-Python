from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")
FONT2 = ("Courier", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_player = "Left Player"
        self.r_player = "Right Player"
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def l_win(self):
        self.goto(0,0)
        self.write(f"{self.l_player} win\n Score: {self.l_score}", align=ALIGNMENT, font=FONT2)

    def r_win(self):
        self.goto(0,0)
        self.write(f"{self.r_player} win\n Score: {self.r_score}", align=ALIGNMENT, font=FONT2)