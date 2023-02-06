# Prime number checker

num = int(input("Please enter a number: "))

def prime(num):
    check = [2,3,4,5,6,7,8,9]
    check_two = []
    for c in check:
        if num % c == 0:
            check_two.append(num % c)
        elif num == c:
            continue
    if len(check_two) > 1:
        print(f"{num} is not a prime")
    else:
        print(f"{num} is a prime")
prime(num)