# Password generator

import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['!', '@', '#', '$', '%', '^', '*', ')', '(', '?']

alp = int(input('Please enter the number of "alphabets" you want: '))
numb = int(input("Please enter the number of 'numbers' you want: "))
chars = int(input("PLease enter the number of 'characters' you want: "))

alph = ''
numbs = ''
charss = ''

al = 0
n = 0
c = 0

for al in range(0, alp):
    rando = random.randint(0, len(alphabets) - 1)
    alph = alph + alphabets[rando]
    al += 1

for nu in range(0, numb):
    rando = random.randint(0, len(numbers) - 1)
    numbs = numbs + numbers[rando]
    nu += 1

for c in range(0, chars):
    rando = random.randint(0, len(characters) - 1)
    charss = charss + characters[rando]
    c += 1

print(alph + numbs + charss)