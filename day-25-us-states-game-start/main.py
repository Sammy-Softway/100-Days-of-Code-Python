from turtle import Screen, Turtle
import pandas
from pandas.core.dtypes import missing

tim = Turtle()
screen = Screen()
screen.title("U.S State Game")
bg_image = "blank_states_img.gif"
screen.addshape(bg_image)
tim.shape(bg_image)


us_states = pandas.read_csv("50_states.csv")
us_states_list = us_states.state.tolist()
xcord_list = us_states.x.tolist()
ycord_list = us_states.y.tolist()


guess_made = 0
states_guessed_correctly = []
guess_on = True

while guess_on:
    user_answer = screen.textinput(title=f"{guess_made}/50 U.S State correct",
                                   prompt="Enter another state").strip().title()
    #answer = user_answer.strip().title()

    locs = Turtle()
    locs.penup()
    locs.shape("circle")
    locs.shapesize(0.5)

    if user_answer == "Exit":
        missing_states = [state for state in us_states_list if state not in states_guessed_correctly]
        # missing_states = []
        # for state in us_states_list:
        #     if state not in states_guessed_correctly:
        #         missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        print(missing_states)
        break

    if guess_made == 50:
        guess_on = False
        print("Thank you for playing!")
    elif user_answer not in us_states_list:
        continue
    elif user_answer in us_states_list:
        guess_made += 1
        states_guessed_correctly.append(user_answer)
        location = us_states[us_states.state == user_answer]
        x_coord = location.x.item()
        y_coord = location.y.item()

        locs.goto(x_coord, y_coord)
        locs.write(arg=f"{user_answer}", align="center", font=("Courier", 14, "normal"))



screen.exitonclick()

