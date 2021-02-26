from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

R_PADDLE_X = 350
L_PADDLE_X = -350

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")
screen.tracer(0)

# Setup paddle
r_paddle = Paddle(R_PADDLE_X, 0)
l_paddle = Paddle(L_PADDLE_X, 0)

# Setup ball
ball = Ball()

# Setup scoreboard
scoreboard = Scoreboard(180)

# listen to keystrokes
screen.listen()
# right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.025)
    screen.update()
    ball.move()

    # Detect collision with Y-walls
    if ball.ycor() > HEIGHT/2 or ball.ycor() < -HEIGHT/2:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > R_PADDLE_X - 20 or ball.distance(l_paddle) < 50 and ball.xcor() < L_PADDLE_X + 20:
        ball.bounce_x()

    # Detects if ball passes paddle (misses ball)
    if ball.xcor() > WIDTH/2 or ball.xcor() < -WIDTH/2:
        scoreboard.l_point() if ball.xcor() > 0 else scoreboard.r_point()
        ball.reset()


screen.exitonclick()
