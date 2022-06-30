from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setposition(-280, 260)
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over", align="center",  font=FONT)
