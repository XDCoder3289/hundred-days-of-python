# This is a calculator for basic operations
from calculator_ascii import calc_ascii, word_ascii

print(calc_ascii + word_ascii)

def start():
    num_1 = float(input("First number: "))
    num_2 = float(input("Second number: "))
    operation = str(input("What operation do you want '+', '-', '/', '*': "))
    num = 0
    if operation == "+":
        num = add(num_1, num_2)
        return num
    if operation == "-":
        num = subtract(num_1, num_2)
        return num
    if operation == "*":
        num = multiply(num_1, num_2)
        return num
    if operation == "/":
        num = divide(num_1, num_2)
        return num

def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b
    return c

def multiply(a, b):
    c = a * b
    return c

def divide(a, b):
    c = a / b
    return c

def run():
    num = start()
    print(num)
    again = input(f"Do you want more operations on {num}: ")
    while again == 'y':
        if again == 'y':
            new_number = float(input("What numer do you want to use: "))
            operand = str(input("what operation do you want: "))
            if operand == "+":
                num = add(num, new_number)
                print(num)
            if operand == "-":
                num = subtract(num, new_number)
                print(num)
            if operand == "*":
                num = multiply(num, new_number)
                print(num)
            if operand == "/":
                num = divide(num, new_number)
                print(num)
        again = input(f"Do you want more operations on {num}: ")

run()