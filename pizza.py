# Small Pizza = $15
# medium pizza = $20
# large pizza = $25

# Pepperoni for small pizza = $2
# Pepperoni for medium or large pizza = $3
# extra cheese for any pizza = $1

print("Welcome to Misha Salman's Pizza")

size = input("What size pizza would you like to order (s, m, l): ")
add_pepperoni = input("Do you want pepperoni? (y, n): ")
extra_cheese = input("Do you want extra cheese? (y, n): ")

small = 15
medium = 20
large = 25
pep_for_small = 2
pep_for_lm = 3
e_cheese = 1
total = 0

if size == 's':
    if add_pepperoni == 'y':
        small += pep_for_small

    if extra_cheese == 'y':
        small += e_cheese

    print(f"Your total bill is ${small}")

if size == 'm':
    if add_pepperoni == 'y':
        medium += pep_for_lm

    if extra_cheese == 'y':
        medium += e_cheese

    print(f"Your total bill is ${medium}")

if size == 'l':
    if add_pepperoni == 'y':
        large += pep_for_lm

    if extra_cheese == 'y':
        large += e_cheese

    print(f"Your total bill is ${large}")