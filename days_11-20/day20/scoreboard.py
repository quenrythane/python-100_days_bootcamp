from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 350)
        self.update_scoreboard()

    def increase_score(self, num):
        self.score += num
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)
