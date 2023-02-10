# blackjack game

import random

print(''' 
_     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 
''')

cards = [2,3,4,5,6,7,8,9,10,10,10,10]

def play():
    computer = []
    player = []
    i = 0
    while i < 2:
        rando = random.randint(0, 11)
        computer.append(cards[rando])
        rando = random.randint(0, 11)
        player.append(cards[rando])
        i += 1
    scores = {
        'player': player,
        'computer': computer,
    }
    return scores

def logic():
    scores = play()
    player = scores['player']
    computer = scores['computer']
    if sum(computer) < 17:
        computer.append(cards[random.randint(0, 11)])
    if sum(computer) > 21:
        print(f"Player wins with cards: {player}")
        print(f"Computer has cards: {computer}")
        return
    total_player = 0
    total_computer = 0

    print(f"Player has cards: {player}")
    print(f"Computer has a card: {computer[0]}")

    more = input("Do you want to draw more: ")

    if more == 'y':
        rando = random.randint(0, 11)
        player.append(cards[rando])
        total_player = sum(player)
        total_computer = sum(computer)
        
        if total_player > total_computer and total_computer < 22:
            print(f"Player wins with {player} cards")
            print(f"Computer has cards {computer}")
        else:
            print(f"computer wins with {computer} cards")
            print(f"Player has cards {player}")
        
    if more != 'y':
        total_player = sum(player)
        total_computer = sum(computer)
        if total_player > total_computer and total_computer < 22:
            print(f"Player wins with {player} cards")
            print(f"Computer has cards {computer}")
        else:
            print(f"computer wins with {computer} cards")
            print(f"Player has cards {player}")
        
        

logic()