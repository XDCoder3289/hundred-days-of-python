import math

def paint():
    height = int(input("What is the height of the wall: "))
    width = int(input("What is the width of the wall: "))
    coverage = 5
    num_of_cans = (height * width) / 5
    print(num_of_cans)
    print(math.ceil(num_of_cans))

paint()