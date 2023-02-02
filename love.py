# Love calculator

name_one = input("Please enter your name: ").lower()
name_two = input("Please enter your partner's name: ").lower()

t = name_one.count("t") + name_two.count("t")
r = name_one.count("r") + name_two.count("r")
u = name_one.count("u") + name_two.count("u")
e = name_one.count("e") + name_two.count("e")

l = name_one.count("l") + name_two.count("l")
o = name_one.count("o") + name_two.count("o")
v = name_one.count("v") + name_two.count("v")
e = name_one.count("e") + name_two.count("e")

true = t + r + u + e
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}%. You guys are like mentos and coke")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}% and you guys are okay together")
else:
    print(f"Your score is {score}%")


