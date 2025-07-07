import random
import turtle
from turtle import Turtle,Screen


timmy_turtle = Turtle()       # Creates a turtle object
timmy_turtle.shape("turtle")  # Makes it look like a turtle
turtle.colormode(255)


colors = [(241, 237, 228), (236, 238, 244), (245, 237, 242), (235, 243, 239), (185, 162, 132), (129, 92, 70),
          (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135), (28, 35, 49), (119, 79, 92), (54, 24, 33),
          (46, 25, 19), (147, 170, 154), (86, 107, 91), (161, 156, 60), (113, 31, 43), (168, 107, 98), (27, 37, 33),
          (51, 58, 92), (212, 179, 189), (110, 123, 155), (117, 37, 27), (161, 107, 118), (219, 178, 170),
          (177, 202, 186), (180, 187, 209), (106, 144, 116), (67, 75, 35)]

# timmy_turtle.fillcolor("red")
timmy_turtle.pensize(1)
timmy_turtle.speed("fastest")
# print(turtle.heading())

# start_x = -100
# start_y = -100
# timmy_turtle.penup()
# timmy_turtle.hideturtle()
# timmy_turtle.goto(start_x, start_y)
# timmy_turtle.dot(20, random.choice(colors))
#
# for j in range(10):
#
#     for i in range(10):
#         # timmy_turtle.color(random.choice(colors))
#         # timmy_turtle.circle(5)
#         timmy_turtle.dot(20, random.choice(colors)) # this is a dot
#         # timmy_turtle.penup()
#         timmy_turtle.forward(30)
#         # timmy_turtle.pendown()
#
#     # timmy_turtle.penup()
#     start_y += 40
#     timmy_turtle.goto(start_x,start_y)

timmy_turtle.penup()
timmy_turtle.hideturtle()
timmy_turtle.setheading(200)
timmy_turtle.forward(300)
timmy_turtle.setheading(0)
for i in range(1,101):
    timmy_turtle.dot(20,random.choice(colors))
    timmy_turtle.forward(30)
    if i % 10 == 0:
        # timmy_turtle.left(90)
        timmy_turtle.setheading(90)
        timmy_turtle.forward(30)
        timmy_turtle.left(90)
        timmy_turtle.forward(300)
        timmy_turtle.setheading(0)




screen = Screen()             # Opens the drawing window
screen.exitonclick()          # Waits for user to click to close the window
