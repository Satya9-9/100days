from main import *

import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color




timmy_turtle.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy_turtle.color(random_color())
        timmy_turtle.circle(100)
        # timmy_turtle.right(i)
        timmy_turtle.setheading(timmy_turtle.heading()+size_of_gap)

draw_spirograph(36)

screen = Screen()             # Opens the drawing window
screen.exitonclick()          # Waits for user to click to close the window
