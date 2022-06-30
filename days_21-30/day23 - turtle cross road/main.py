import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # detect player win
    if player.position()[1] > player.finish:
        player.go_to_start()
        scoreboard.level_up()
        cars.increase_speed()

    # detect turtle collision
    for car in cars.all_cars:
        if player.distance(car) < 21:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
