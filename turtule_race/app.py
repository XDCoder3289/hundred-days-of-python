from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? 'red', 'blue', 'green', 'aqua', "
                                                      "'black', 'violet': ")
print(bet)
race_is_on = False

colors = ['red', 'blue', 'green', 'aqua', 'black', 'violet']
all_turtles = []

i = -100
z = 0
for turtle_range in range(0, 6):
    sal = Turtle()
    sal.color(colors[z])
    sal.penup()
    sal.shape("turtle")
    sal.goto(x=-230, y=i)
    i += 40
    z += 1
    all_turtles.append(sal)


if bet:
    race_is_on = True

t = 0
line = 0
while race_is_on:
    rando = random.randint(0, 20)
    contestant = all_turtles[t]
    contestant.forward(rando)
    t += 1
    if t > 5:
        t = 0
    if contestant.xcor() > 230:
        if bet == str(contestant.color()[0]):
            print(f"{contestant.color()[0]} has won so you win!")
        else:
            print(f"{contestant.color()[0]} has won so you lost")
        race_is_on = False




screen.exitonclick()
