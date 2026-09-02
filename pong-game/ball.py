from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def wall_collision(self):
        self.dy *= -1

    def paddle_collision(self):
        self.dx *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_collision()