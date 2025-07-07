# now a random walk
from main import *


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


timmy_turtle.pensize(10)
direction = [0,90,180,270]
colors = [
    "light gray",
    "slate gray",
    "powder blue",
    "light steel blue",
    "rosy brown",
    "light coral",
    "thistle",
    "lavender",
    "beige",
    "misty rose",
    "peach puff",
    "lemon chiffon",
    "light goldenrod yellow",
    "honeydew",
    "linen",
    "azure",
    "gainsboro",
    "blanched almond",
    "antique white",
    "old lace"
]
timmy_turtle.speed("fastest")

for i in range(200):
    timmy_turtle.color(random_color())

    integer = random.randint(0,100)
    random_direction = random.choice(direction)
    timmy_turtle.forward(30)
    timmy_turtle.setheading(random_direction)


screen = Screen()             # Opens the drawing window
screen.exitonclick()          # Waits for user to click to close the window
