from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(380, 0)
l_paddle = Paddle(-380, 0)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_collision()

    #Paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.paddle_collision()
        ball.move_speed *= 0.9

    #Ball goes out of play area
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_ball()

    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_ball()

    if scoreboard.r_score == 2:
        game_is_on = False
        scoreboard.r_win()

    if scoreboard.l_score == 2:
        game_is_on = False
        scoreboard.l_win()



screen.exitonclick()