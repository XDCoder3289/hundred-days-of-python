from turtle import Turtle, Screen

mish = Turtle()


def triangle():
    i = 0
    while i < 3:
        mish.forward(100)
        mish.right(120)
        i += 1


def square():
    mish.color("green")
    i = 0
    while i < 4:
        mish.forward(100)
        mish.right(90)
        i += 1


def pentagon():
    mish.color("blue")
    i = 0
    while i < 5:
        mish.forward(100)
        mish.right(72)
        i += 1


def hexagon():
    mish.color("red")
    i = 0
    while i < 5:
        mish.forward(100)
        mish.right(60)
        i += 1


def heptagon():
    mish.color("orange")
    i = 0
    while i < 7:
        mish.forward(100)
        mish.right(360 / 7)
        i += 1


def octagon():
    mish.color("orange")
    i = 0
    while i < 8:
        mish.forward(100)
        mish.right(45)
        i += 1


def nonagon():
    mish.color("brown")
    i = 0
    while i < 9:
        mish.forward(100)
        mish.right(40)
        i += 1


def decagon():
    mish.color("black")
    i = 0
    while i < 10:
        mish.forward(100)
        mish.right(36)
        i += 1


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()


screen = Screen()
screen.exitonclick()
