# Check if people can buy a ticket of a slide

height = float(input("Please enter your height in feet: "))

minimum_height = float(5.5)

if height >= minimum_height:
    age = float(input("What is your age: "))
    if age >= float(18):
        print("Please pay 1000 PKR")
    elif age < float(7):
        print("You're way too young.")
    else:
        print("Please pay 200 PKR")

elif height == float(5.3):
    print("You are way too short, fuck off!!!")

else:
    print("Please try later")