# Tip calculator

print("Welcome to the tip calculator")
print("What was your total bill? ")
bill = int(input())

print("How many guys went to lunch with you? ")
people = int(input())

print("How much percentage would you like to tip: ")
tip = int(input())

zero_tip = 0
extra_tip = 0

if tip == 0:
    zero_tip = round(bill / people, 2)
    print("Each person should pay: " + str(zero_tip))
else:
    extra_tip = round((((tip * bill) / 100) + bill) / people, 2)
    print("Each person should pay: " + str(extra_tip))

# Typer conversions were necessary for this code to work