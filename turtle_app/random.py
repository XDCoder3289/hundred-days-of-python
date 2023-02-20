from turtle import Turtle, Screen
import random


class Random:
    def rando(self):
        randos = random.randint(100, 1000)
        return randos


mish = Turtle()
rand = Random()

i = 0
while i < 10:
    mish.forward(rand.rando())
    mish.left(rand.rando())
    mish.right(rand.rando())
    mish.backward(rand.rando())
    i += 1

screen = Screen()
screen.exitonclick()
