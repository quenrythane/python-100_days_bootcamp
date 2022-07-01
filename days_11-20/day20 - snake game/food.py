from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x, y = randint(-14, 14) * 20, randint(-14, 14) * 20
        self.goto(x, y)
