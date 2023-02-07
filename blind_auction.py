# blind auction calculator

def auction_calc():
    auction_dict = {}
    name = input("What is your name: ")
    bid = int(input("What's your bid: "))
    auction_dict[name] = bid
    any_other = input("Is there anyone else who wants to bid? (y) (n): ")

    if any_other == 'y':
        while any_other != "n":
            name = input("What is your name: ")
            bid = int(input("What's your bid: "))
            auction_dict[name] = bid
            any_other = input("Is there anyone else who wants to bid? (y) (n): ")
    
    won = max(auction_dict, key=auction_dict.get)
    
    
    print(f" {won} has won with the highest bid of: ${auction_dict[won]}")
    

    
auction_calc()