import random
import turtle
from turtle import *

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput(title="make your bet", prompt="which turtle will win"
                                                          " the race? Enter a color: ")


rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
# chiku = Turtle(shape="turtle")


# turtles = [chiku, pinku, raju, hera, babu, sonu, tillu]
all_turtles = []
y = -150;

for i in range(7):
    chiku = Turtle(shape="turtle")
    chiku.penup()
    chiku.goto(x=-235, y=y)
    chiku.color(rainbow_colors[i])
    y += 50

    all_turtles.append(chiku)


random_number = random.randint(1, 100)

# chiku.goto(-235, 0)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:# creating the finish line
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle wins!")
                is_race_on = False

            else:
                print(f"you've lost! The {winning_color} turtle wins.")
                is_race_on = False


        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)


screen.exitonclick()
