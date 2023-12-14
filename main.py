from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# make stuff
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
# paddle controls
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
# bounce off sides
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
# bounce off paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() > -338:
        ball.bounce_x()
# detect misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
