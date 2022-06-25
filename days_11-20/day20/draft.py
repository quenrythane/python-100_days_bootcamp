from random import randint
from turtle import Turtle

x, y = randint(-280, 280), randint(-280, 280)
y = 201
print(x)
print(y)

t = Turtle()
t.speed("fastest")
t.goto(x, y)
print(t.position())
cord = list(abs(x) for x in t.position())
print(cord)
print(cord > [200, 200])





