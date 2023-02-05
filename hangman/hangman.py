import random
from wordlist import word_list_final
from asciii import hangman
from asciii import welcome

print(welcome)
print('')
hangman_ascii = hangman
word_list = word_list_final

chosen_word = random.choice(word_list)
chosen_word_list = []
chances = []

for c in chosen_word:
    chosen_word_list.append(c)
    chances += "_"

print(chances)
print("")

i = 0

while chances != chosen_word_list:
    guess = input('Please enter the letter: ')
    k = 0
    for letter in chosen_word:
        if letter == guess:
            chances[k] = letter
        k += 1
   
    kill = chosen_word_list.count(guess)
    if kill == 0:
        print(hangman_ascii[i])
        i += 1
        if i == 7:
            print("You've lost")
            break

    if chances == chosen_word_list:
        print("You've won")
        break

    print(chances)