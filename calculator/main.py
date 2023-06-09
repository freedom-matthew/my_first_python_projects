from art import logo


def add(n_1, n_2):
    return n_1 + n_2


def subtract(n_1, n_2):
    return n_1 - n_2


def multiply(n_1, n_2):
    return n_1 * n_2


def divide(n_1, n_2):
    return n_1 / n_2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation (+, -, *, /): ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
