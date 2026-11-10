
# Functions 


def arithmeticCalc(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    print(f'{num1} + {num2} = {addition}')
    print(f'{num1} - {num2} = {subtraction}')
    print(f'{num1} x {num2} = {multiplication}')

    try:
        division = num1 / num2
        print(f'{num1} / {num2} = {division}')
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

arithmeticCalc(first_number, second_number)
