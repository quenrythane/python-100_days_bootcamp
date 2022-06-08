# docs https://pypi.org/project/colorgram.py/
import colorgram
import random
from turtle import *


def get_color_list():
    rgb_colors = []
    colors = colorgram.extract('ash-pikachu.jpg', 10)
    for color in colors:
        rgb = color.rgb.r, color.rgb.g, color.rgb.b
        rgb_colors.append(rgb)

    return rgb_colors


color_list = get_color_list()
colormode(255)
tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
