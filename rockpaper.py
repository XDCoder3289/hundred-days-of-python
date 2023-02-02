import random

intro = '''
______           _       ______                       _____      _                        
| ___ \         | |      | ___ \                     /  ___|    (_)                       
| |_/ /___   ___| | __   | |_/ /_ _ _ __   ___ _ __  \ `--.  ___ _  ___ ___ ___  _ __ ___ 
|    // _ \ / __| |/ /   |  __/ _` | '_ \ / _ \ '__|  `--. \/ __| |/ __/ __/ _ \| '__/ __|
| |\ \ (_) | (__|   < _  | | | (_| | |_) |  __/ |_   /\__/ / (__| | (_| (_| (_) | |  \__ \\
\_| \_\___/ \___|_|\_( ) \_|  \__,_| .__/ \___|_( )  \____/ \___|_|\___\___\___/|_|  |___/
                     |/            | |          |/                                        
                                   |_|                                                    


          _______  _        _        _______ 
|\     /|(  ____ \( \      ( \      (  ___  )
| )   ( || (    \/| (      | (      | (   ) |
| (___) || (__    | |      | |      | |   | |
|  ___  ||  __)   | |      | |      | |   | |
| (   ) || (      | |      | |      | |   | |
| )   ( || (____/\| (____/\| (____/\| (___) |
|/     \|(_______/(_______/(_______/(_______)

'''
print(intro)

sign = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
, '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''' ]


ans = ['rock', 'paper', 'scissor']

print("Please enter your choice:\n-------------------------------------------\n 1 for Rock, 2 for paper, 3 for Sciccors")

choice = int(input()) - 1
rando = random.randint(0, 2)

print("You chose: ")
print(sign[choice])

if choice == rando:
    print('The computer chose: ')
    print(sign[rando])
    print("It's a draw! Fuck you both")

if choice == 0 and rando == 1:
    print('The computer chose: ')
    print(sign[rando])
    print('the computer wins, Fuck you')

if choice == 0 and rando == 2:
    print('The computer chose: ')
    print(sign[rando])
    print('You win but still Fuck You')

if choice == 1 and rando == 0:
    print('The computer chose: ')
    print(sign[rando])
    print('You win but still Fuck You')

if choice == 1 and rando == 2:
    print('The computer chose: ')
    print(sign[rando])
    print('The computer wins, Fuck You')

if choice == 2 and rando == 0:
    print('The computer chose: ')
    print(sign[rando])
    print('The computer wins, Fuck You')

if choice == 2 and rando == 1:
    print('The computer chose: ')
    print(sign[rando])
    print('You win but still Fuck You')

