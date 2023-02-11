# This game is about guessing numbers based on the difficulty the user has selected

import random

def game():
    difficulty = input("Please enter the difficulty you want (hard) (easy): ")
    rando = random.randint(0, 100)
    if difficulty == "hard":
        print("You've got 5 attempts")
        win = 0
        i = 0
        while i < 5:
            print(f"Attempt {i + 1}")
            guess = int(input("Please guess a number: "))
            if rando < guess:
                print("Too high")
            if rando > guess:
                print("Too low")
            if rando == guess:
                win = True
                break
            i += 1
        if win:
            print("You've won")
        else:
            print("You've lost")


    if difficulty == "easy":
        print("You've got 10 attempts")
        i = 0
        win = 0
        while i < 10:
            print(f"Attempt {i + 1}")
            guess = int(input("Please guess a number: "))
            if rando < guess:
                print("Too high")
            if rando > guess:
                print("Too low")
            if rando == guess:
                win = True
                break
            i += 1
        if win:
            print("You've won")
        else:
            print(f"You've lost the number was {rando}")


game()
