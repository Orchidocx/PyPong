from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmovdir = 5
        self.ymovdir = 5

    def move(self):
        new_x = self.xcor() + self.xmovdir
        new_y = self.ycor() + self.ymovdir
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.xmovdir *= -1

    def bounce_y(self):
        self.ymovdir *= -1
