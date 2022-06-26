from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

        self.penup()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.setposition(x_pos, y_pos)

    def go_up(self):
        if self.y_pos > 230:
            pass
        else:
            self.y_pos += 20
            self.goto(self.x_pos, self.y_pos)

    def go_down(self):
        if self.y_pos < -230:
            pass
        else:
            self.y_pos -= 20
            self.goto(self.x_pos, self.y_pos)

