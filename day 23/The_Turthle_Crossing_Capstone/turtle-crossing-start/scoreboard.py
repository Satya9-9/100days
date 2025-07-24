from turtle import *
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

        self.score = 0

    def level(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}",align="left", font=FONT)


