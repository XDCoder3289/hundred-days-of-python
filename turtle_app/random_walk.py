from turtle import Turtle, Screen
import random


mish = Turtle()
rando = random.randint(0, 10)

i = 0
while i < 10:
    mish.forward(rando.rando())
    mish.left(rando.rando())
    mish.right(rando.rando())
    mish.backward(rando.rando())
    i += 1

screen = Screen()
screen.exitonclick()
