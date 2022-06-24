import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
level = 10

while game_is_on:
    screen.update()
    time.sleep(1/level)

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    snake.move()







screen.exitonclick()
