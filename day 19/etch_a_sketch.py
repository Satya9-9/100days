from turtle import *

chiku = Turtle()
screen = Screen()

def move_forward():
    chiku.forward(100)
def backward():
    chiku.backward(100)
def counter_clockwise():
    chiku.right(10)

def clockwise():
    chiku.left(10)

def clear_screen():
    chiku.clear()
    chiku.penup()
    chiku.home()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()