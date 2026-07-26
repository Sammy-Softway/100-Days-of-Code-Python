from turtle import Screen, Turtle
import random


screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")
print(f"You chose {user_bet} turtle")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [0, 60, -60, 120, -120, 180]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-380, y_coordinates[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_on = True


while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 380:
            race_on = False
            fastest_turtle = turtle.pencolor()
            if user_bet == fastest_turtle:
                print(f"You win! {fastest_turtle} turtle wins the race.")
            print(f"You lost! {fastest_turtle} turtle wins the race.")




# sam = Turtle(shape="turtle")
# sam.penup()
# sam.color(colors[1])
# sam.goto(-380, 60)
#
# mike = Turtle(shape="turtle")
# mike.penup()
# mike.color(colors[2])
# mike.goto(-380, -60)
#
# dan = Turtle(shape="turtle")
# dan.penup()
# dan.color(colors[3])
# dan.goto(-380, 120)
#
# seyi = Turtle(shape="turtle")
# seyi.penup()
# seyi.color(colors[4])
# seyi.goto(-380, -120)
#
# dolapo = Turtle(shape="turtle")
# dolapo.penup()
# dolapo.color(colors[5])
# dolapo.goto(-380, 180)






screen.exitonclick()