import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

mish = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


i = 0
mish.pensize(3)
mish.speed(0)
while i < 50:
    a = 0
    while a < 71:
        mish.penup()
        mish.forward(5)
        mish.dot(5, random_color())
        mish.forward(5)
        a += 1
    # mish.forward(710)
    mish.left(90)
    mish.forward(20)
    mish.left(90)
    mish.color(random_color())
    b = 0
    while b < 71:
        mish.penup()
        mish.forward(5)
        mish.dot(5, random_color())
        mish.forward(5)
        b += 1
    # mish.forward(710)
    mish.right(90)
    mish.forward(20)
    mish.right(90)
    i += 1

screen.exitonclick()
