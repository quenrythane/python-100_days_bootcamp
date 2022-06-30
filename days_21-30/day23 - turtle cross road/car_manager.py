from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1, 6) == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            new_car.setheading(180)
            random_y = randint(-20, 20)*10
            new_car.setposition(300, random_y)
            new_car.speed = self.speed
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)
