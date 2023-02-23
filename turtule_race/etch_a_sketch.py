from turtle import Turtle, Screen

mish = Turtle()
screen = Screen()
screen.listen()


def forward():
    mish.forward(10)


def back():
    mish.backward(10)


def right():
    mish.right(25)


def left():
    mish.left(25)


screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.exitonclick()