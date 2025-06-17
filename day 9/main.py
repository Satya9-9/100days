from art import *

print(calculator_art)

print("Welcome to calculator")

def add(first_number, next_number):
    return first_number + next_number

def subtract(first_number, next_number):
    return first_number - next_number

def multiply(first_number, next_number):
    return first_number * next_number

def divide(first_number, next_number):
    return first_number / next_number

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



def calculator(first_number = None):
    if first_number is None:
        first_number = float(input("What is your first number? "))


    operator = input("What is your operator? '+', '-' , '/' , and '*' ")
    next_number = float(input("What is your next number? "))
    result = 0
    if operator == "+":
        result = operation[operator](first_number, next_number)
        print(f'{first_number} {operator} {next_number} = {result}')

    elif operator == "-":
        result = subtract(first_number, next_number)
        print(f'{first_number} {operator} {next_number} = {result}')

    elif operator == "*":
        result = multiply(first_number, next_number)
        print(f'{first_number} {operator} {next_number} = {result}')

    elif operator == "/":
        result = divide(first_number, next_number)
        print(f'{first_number} {operator} {next_number} = {result}')

    else:
        print("Invalid operator")

    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to,"
                   f"start a new calculation or OFF: ")

    if choice == "n":
        print(calculator_art)
        calculator()

    elif choice == "OFF":
        print("Thank you for playing!")

    else:
        calculator(result)

calculator()





