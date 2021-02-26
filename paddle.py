from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)

    def reset(self, x, y):
        self.goto(x, y)
