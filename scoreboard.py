from turtle import Turtle
FONT = ("Arial", 24, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    """It deals with the score system of the game"""
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        # self.clear()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.read_high_score()
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)
        self.write(arg=f"high Score: {self.high_score}\t", align="right", font=FONT)

    def score_increases(self):
        self.goto(0, 260)
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write_high_score()
        self.write(arg=f"Game over, Your Score is:\n {self.score},\n the high score is \n{self.high_score}", align="center", font=FONT)

    def read_high_score(self):
        with open("highscore.txt") as file:
            self.high_score = int(file.read())

    def write_high_score(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.high_score))
