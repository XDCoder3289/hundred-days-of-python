# randomly spit out a name from the list and the guy has to pay the bill

import random
names = input("Please enter the names of the people who're with you? ")
names = names.split(',')

num = random.randint(0, len(names))

print(names[num])

