from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.setposition(x_pos, y_pos)

    # don't know which version is better so leave both (but personally prefer second because of readability)
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20) if self.position()[1] < 230 else "do nothing"

    def go_down(self):
        if self.position()[1] < -230:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 20)
