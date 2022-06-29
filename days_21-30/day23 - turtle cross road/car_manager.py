from turtle import Turtle
from random import choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.setheading(180)
        self.speed = STARTING_MOVE_DISTANCE

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def move(self):
        self.forward(self.speed)
