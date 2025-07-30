from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt")as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=("Courier", 24, "normal"))

    def write_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score >= self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data :

                data.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()
