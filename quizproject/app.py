# Give the user a question
# Ask for an answer
# If answer is correct increase score count
# Else take out a life they have
# Give a total of 3 choices
# End the game if the score is more than 20
# What will I need: A dataset that has the data

from data import question_data
from ux import logo
from game import Game
import random

print(logo)

game = Game()

while game.lives > 0 or game.num > 11:
    q_and_a = game.generate_rando()
    print(q_and_a[0])
    ans = input("What do you think: ").lower()
    if ans == q_and_a[1]:
        game.score += 1
    else:
        game.lives -= 1
    game.num += 1
    
    print(f"Lives Left: {game.lives}")
    print(f"Total Score: {game.score}")