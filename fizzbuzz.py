# make a game called Fizzbuzz
# if a number is divisible by 3 print fizz
# if a number is divisible by 5 print buzz
# print fizzbuzz if a number is divisible by both 3 and 5

for n in range(1, 101):
    if n % 3 == 0:
        print(f"{n} divisible by 3: Fizz!")
    if n % 5 == 0:
        print(f"{n} divisible by 5: Buzz")
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} divisible by 3 and 5: FizzBuzz")
    if n % 3 != 0 and n % 5 != 0:
        print(n)
