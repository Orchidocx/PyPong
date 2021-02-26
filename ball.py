from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.start_speeds = [-3, -4, -5, 3, 4, 5]
        self.x_mov_dir = 5
        self.y_mov_dir = choice(self.start_speeds)

    def move(self):
        new_x = self.xcor() + self.x_mov_dir
        new_y = self.ycor() + self.y_mov_dir
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_mov_dir *= -1

    def bounce_y(self):
        self.y_mov_dir *= -1

    def increase_speed(self):
        self.x_mov_dir *= choice([1.01, 1.02, 1.03])
        self.y_mov_dir *= choice([1.01, 1.02])

    def reset(self, pos_neg):
        self.goto(0, 0)
        self.x_mov_dir = 5 * pos_neg
        self.y_mov_dir = choice(self.start_speeds)
