# now differemt types of shapes
from main import *

# # this is for drawing square
# for i in range(4):
#
#     timmy_turtle.forward(100)
#     timmy_turtle.left(90)
#
# # this is for drawing dashed line
# for i in range(5):
#
#     timmy_turtle.forward(10)
#     timmy_turtle.penup()
#     timmy_turtle.forward(10)
#     timmy_turtle.pendown()



def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        timmy_turtle.forward(100)
        timmy_turtle.left(angle)

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]

for i in range(3,20):
    timmy_turtle.color(random.choice(colors))
    draw_shape(i)

screen = Screen()             # Opens the drawing window
screen.exitonclick()          # Waits for user to click to close the window
