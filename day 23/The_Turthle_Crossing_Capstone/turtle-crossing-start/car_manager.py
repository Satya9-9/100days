from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        dice = random.randint(1, 6)
        if dice == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(290, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)

    def level_up(self):
        self.car_speed *= MOVE_INCREMENT














