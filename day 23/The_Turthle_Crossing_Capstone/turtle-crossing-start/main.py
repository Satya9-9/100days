import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()
level.update()

screen.listen()
screen.onkey(player.move, "Up")

car_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    car.create_car()
    car.move_car()

    # detecting the collision with the car

    for carz in car.all_cars:
        if carz.distance(player) < 20:
            game_is_on = False

    if player.ycor() == 260:
        level.increase_level()
        player.reset_position()
        # level.update()
        # car_speed *= 0.9
        car.level_up()
screen.exitonclick()
