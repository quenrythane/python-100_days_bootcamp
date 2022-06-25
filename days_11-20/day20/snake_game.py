import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
level = int(screen.textinput("Choose a level", "Choose a level 1- 10"))

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(1/(level*2))  # multiply level because just level speed was too slow :)


    snake.move()
    """ why this doesnt work?
    if list(snake.head.position()) == list(food.position()):
        food.refresh()
        print(food.position())
    """

    # food collision detection
    if snake.head.distance(food) < 10:
        food.refresh()  # need add avoid appear on snake
        scoreboard.increase_score(level)

    # wall collision detection
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False






screen.exitonclick()
