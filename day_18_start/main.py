from turtle import Turtle, Screen, colormode
import heroes
import random

print(heroes.gen())


tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

colormode(255)

# colors = ["red", "orange", "yellow", "green", "blue", "violet",
#           "purple", "forest green", "rosy brown", "pink", "brown", "dark cyan"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rand_color = (r, g, b)
    return rand_color

tim.speed("fastest")

def spiral_circles(circle_gaps):
    for _ in range(int(360 / circle_gaps)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + circle_gaps)


spiral_circles(10)


# for moves in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# n = 3

# while True:
#     if n == 10:
#         break
#     deg = 360 / n
#     n += 1
#     tim.color(random.choice(colors))
#     for _ in range(n):
#         tim.forward(100)
#         tim.right(deg)



# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for sides in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shapes(sides)



# speed = 1
# direction = [0, 90, 180, 270]
#
# for _ in range(100):
#     tim.color(random_color())
#     tim.pensize(5)
#     tim.forward(20)
#     tim.setheading(random.choice(direction))
#     tim.speed(speed)
#     speed += 0.05





screen = Screen()
screen.exitonclick()