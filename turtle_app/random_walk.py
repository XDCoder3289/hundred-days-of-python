from turtle import Turtle, Screen
import random

mish = Turtle()
mish.pensize(10)
mish.speed(6)

color = ["blue", "green", "pink", "seagreen"]

c = 0
i = 0

while i < 50:
    if c > 3:
        c = 0
    mish.color(color[c])
    rando1 = random.randint(10, 50)
    rando2 = random.randint(50, 100)
    rando3 = random.randint(10, 100)
    rando4 = random.randint(50, 100)
    mish.forward(rando1)
    mish.right(90)
    mish.forward(rando1)
    mish.backward(rando3)
    mish.left(90)
    i += 1
    c += 1

screen = Screen()
screen.exitonclick()
