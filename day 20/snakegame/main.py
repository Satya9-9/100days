import time
from turtle import *
from snake import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a snake body
# x = 0
# for i in range(3):
#     chiku = Turtle(shape="square")
#     chiku.penup()
#     chiku.color("white")
#     chiku.goto(x=x, y=0)
#     x-=20

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# move the segment
game_is_on = True

# screen.update()
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.move()

screen.exitonclick()
