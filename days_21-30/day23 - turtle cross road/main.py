import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
# TODO 2: add more randomly generated car along the y-axis which move from right edge to left and then dissapear
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    # detect player win
    if player.position()[1] > 260:
        player.setposition(0, -280)
        scoreboard.level_up()
        car.increase_speed()

    # detect turtle collision
    # TODO 4: finish this detection
    if player.position()[1] > 50:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()

