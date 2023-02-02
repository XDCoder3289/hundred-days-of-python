# Random heads or tails

import random

num = random.randint(0, 10)
name = input("Who's picking?: ")
decide = input("What do you choose? Heads or Tails!: ").lower()


if num % 2 == 0:
    if decide == "heads":
        print(f"{name} it's heads! You win.")
    else:
        print(f"{name} it's heads..... You lose.")
if num % 2 != 0:
    if decide == "tails":
        print(f"{name} it's tails! You win.")
    else:
        print(f"{name} it's tails..... You lose.")
