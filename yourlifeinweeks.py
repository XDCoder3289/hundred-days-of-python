# Calculate the number of days left in your life

name = input("Hey! What's your name: ")
age = int(input("What's your age: "))

num_of_days = 365
num_of_weeks = 52
num_of_months = 12
average_age = 90

num_of_weeks_lived = age * num_of_weeks
num_of_weeks_left = (average_age * num_of_weeks) - age * num_of_weeks

print("You've lived " + str(num_of_weeks_lived) +" weeks")
print("You're left with " + str(num_of_weeks_left) +" weeks")