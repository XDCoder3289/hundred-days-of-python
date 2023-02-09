# Tell the number of days in a month
# Program flexible for leap year

year = int(input("Please enter the year you want to check: "))

number_of_days_month = {

    'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 
    'June': 30, 'July': 31, 'August': 31, 'September': 30, 
    'October': 31, 'November': 30, 'December': 31

}

number_of_days_leap = {

    'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 
    'June': 30, 'July': 31, 'August': 31, 'September': 30, 
    'October': 31, 'November': 30, 'December': 31

}

def leap_year():
    leap = 0
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = 1
                return leap
            else:
                return leap
        else:
            leap = 1
            return leap
    else:
        return leap

def number_of_days():
    if leap_year() == 1:
        for key in number_of_days_leap:
            print(f"{key}: {number_of_days_leap[key]}")
    elif leap_year() == 0:
        for key in number_of_days_month:
            print(f"{key}: {number_of_days_month[key]}")

number_of_days()
