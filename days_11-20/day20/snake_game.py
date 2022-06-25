import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(605, 605)
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
    time.sleep(1/(level*3))  # multiply level because just level speed was too slow :)


    snake.move()
    """ why this doesnt work?
    if list(snake.head.position()) == list(food.position()):
        food.refresh()
        print(food.position())
    """

    # food collision detection
    if snake.head.distance(food) < 10:
        food.refresh()  # need add avoid appear on snake
        snake.extend()
        scoreboard.increase_score(level)

    # wall collision detection
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # tail collision detection
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()






screen.exitonclick()
