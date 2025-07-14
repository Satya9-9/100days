import time
from turtle import *
from snake import *
from food import Food
from scoreboard import Scoreboard

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
food= Food()
score_board = Scoreboard()


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

    # detecting collision with food
    if snake.head.distance(food)<20:
        food.refresh()
        # score_board.score += 1
        snake.extend_segment()
        score_board.write_score()

    # detecting the collision with the wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        print("Game Over")
        score_board.game_over()
        game_is_on = False

    # detecting collision with tail
    # if head collides with any segment in the tail then game over
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            game_is_on = False
        # game  over



screen.exitonclick()
