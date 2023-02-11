from gamedata import data
from art import asciii
import random

print(asciii)

def compare():
    rando_1 = random.randint(0, 49)
    rando_2 = random.randint(0, 49)

    if rando_2 == rando_1:
        rando_2 = random.randint(0, 49)
    
    account_1 = data[rando_1]['name']
    follower_1 = data[rando_1]['follower_count']
    account_2 = data[rando_2]['name']
    follower_2 = data[rando_2]['follower_count']
    
    compare = {
        "A": follower_1,
        "Name One": account_1,
        "B": follower_2,
        "Name Two": account_2,
    }

    return compare

# Take input and see if the input had higher or lower

def play():
    i = 0
    win = True
    while win:
        comparison = compare()
        print(f"{comparison['Name One']} or {comparison['Name Two']}")
        guess = input("Guess who has higher followers (A) (B): ").upper()
        if guess == 'A':
            if comparison[guess] > comparison['B']:
                print("Correct")
                i += 1
            else:
                print("You've lost")
                win = False
        if guess == 'B':
            if comparison[guess] > comparison['A']:
                print("Correct")
                i += 1
            else:
                win = False
                print("You've lost")
    print(f"Your final score is {i}")

play()