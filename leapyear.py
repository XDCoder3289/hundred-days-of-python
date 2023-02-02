# A program to check if a year is a leap year

year = int(input("Please enter the year you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is NOT a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")
# Adding a comment
# adding another comment
# Checking if contributions calendaar is tracking correctly
