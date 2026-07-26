from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_foward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(fun=move_foward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()