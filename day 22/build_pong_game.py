import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from socreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
speed = 0

#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("white")
# tim.hideturtle()
# tim.penup()
# tim.goto(0, -380)
# tim.setheading(90)
# tim.pensize(3)
#
# for i in range(40):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
screen.tracer(0)

r_paddle = Paddle((250, 0))
l_paddle = Paddle((-250, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
ball.speed("slowest")
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detecting collision with the ball

    if ball.ycor() > 250 or ball.ycor() < -250:
        # it needs to bounce
        ball.bounce_y()

    # detecting collision of ball with the paddle
    if ball.distance(r_paddle) < 40:
        print("Game Over")
        ball.bounce_x()


    # if left paddle missses the ball
    if ball.xcor() < -250:
        # then we will reset the position
        # ball.goto(0, 0)
        # ball.bounce_x()
        ball.reset_ball()
        scoreboard.l_point()


    #if right paddle misses the ball
    if ball.xcor() > 250:
        # ball.goto(0, 0)
        # ball.bounce_x()
        ball.reset_ball()
        scoreboard.r_point()


    if ball.distance(l_paddle) < 40:
        print("Game Over for 2")
        ball.bounce_x()


screen.exitonclick()
