from replit import clear
from art import logo


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}


def calculator():
    print(logo)
    continue_calculating = True
    result = 0
    num1 = float(input("What's the first number?\n"))

    while continue_calculating:
        operation_symbol = input("Pick an operation: Addition (+), subtraction (-), multiplication (*), division (/)\n")
        num2 = float(input("What's the second number?\n"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "n":
            continue_calculating = False
            clear()
            calculator()
        else:
            num1 = answer


if __name__ == '__main__':
    calculator()
