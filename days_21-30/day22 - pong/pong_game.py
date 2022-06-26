import time
from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

l_pad = Paddle(-350, 0)
r_pad = Paddle(350, 0)

screen.listen()
screen.onkey(l_pad.go_up, "w")
screen.onkey(l_pad.go_down, "s")
screen.onkey(r_pad.go_up, "Up")
screen.onkey(r_pad.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)



screen.exitonclick()
