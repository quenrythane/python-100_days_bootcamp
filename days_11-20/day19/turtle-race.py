from random import randint
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

screen = Screen()
screen.setup(600, 400)
# screen.exitonclick()
race = True

user_bet = screen.textinput("Make your bet", "Which turtle win?").lower()

for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-250, -125 + 50*i)
    turtles.append(t)

while race:
    for turtle in turtles:
        turtle.forward(randint(1, 10))

        if turtle.position()[0] > 250:
            race = False
            winner = turtle.fillcolor()

print(f"The winner is {winner}! You {'win' if winner == user_bet else 'lose'}!")





