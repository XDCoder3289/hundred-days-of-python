# coffee machine

# espresso = 50 ml water, 18g coffee, $1.5
# latte = 200 ml water, 24g coffee, 150ml Milk, $2.5
# cappuccino = 250 ml water, 24g coffee, 100ml Milk, $3.0

# resources => 300 ml water, 200 ml milk, 100g coffee



#  Print Report (resources), ask for what they want, print resources


resource = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

coffee = {

    'espresso': {
        'water': 250,
        'milk': 0,
        'coffee': 18,
        'cost': 1.5,
    },
    'latte': {
        'water': 200,
        'milk': 150,
        'coffee': 24,
        'cost': 2.5,
    },
    'cappuccino': {
        'water': 250,
        'milk': 100,
        'coffee': 24,
        'cost': 3.0,
    }

}

requirement = input("What do you need (Espresso), (Latte), (Cappucino): ").lower()

def money():
    penny  = 0.01
    nickel = 0.05
    dime = 0.1
    quarter = 0.25
    inserted_penny = float(input("How many pennies do you want to add: ")) * penny
    inserted_nickel = float(input("How many nickel do you want to add: ")) * nickel
    inserted_dime = float(input("How many dime do you want to add: ")) * dime
    inserted_quarter = float(input("How many quarter do you want to add: ")) * quarter
    total = round(inserted_penny + inserted_dime + inserted_nickel + inserted_quarter, 2)
    return total

def resources():
    new_coffee = coffee[requirement]
    water_left = resource['water'] - new_coffee['water']
    milk_left = resource['milk'] - new_coffee['milk']
    coffee_left = resource['coffee'] - new_coffee['coffee']

    resource['water'] = water_left
    resource['milk'] = milk_left
    resource['coffee'] = coffee_left
    
    new_dict = {

        'water': water_left,
        'milk': milk_left,
        'coffee': coffee_left,

    }
    
    if water_left < 0 or milk_left < 0 or coffee_left < 0:
        print("You need more resources")
        print(f"Water: {water_left}, Milk: {milk_left}, Coffee: {coffee_left}")
    
    return resource


def machine():
    check = resources()
    while check != 0:
        if requirement == 'espresso':
            print("Espresso costs $1.5")
            inserted = money()
            espresso = coffee['espresso']
            cost = float(espresso['cost'])
            change = round(inserted - cost, 2)

            print(f"Your change is: ${change}, here's your coffee")
    
        if requirement == 'latte':
            print("Latte costs $2.5")
            inserted = money()
            latte = coffee['latte']
            cost = float(latte['cost'])
            change = round(inserted - cost, 2)
            print(f"Your change is: ${change}, here's your coffee")
    
        if requirement == 'cappucino':
            print("Espresso costs $3.0")
            inserted = money()
            cappuccino = coffee['cappuccino']
            cost = float(cappuccino['cost'])
            change = round(inserted - cost, 2)
            print(f"Your change is: ${change}, here's your coffee")
        
        check = resources()
        
        print(check)


    
machine()