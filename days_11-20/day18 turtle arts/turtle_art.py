import turtle as t
from random import choice, randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(500):
    # tim.color(choice(colors))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))

input(".")
