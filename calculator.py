def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
    


def convert_number(str):
    pass


def is_valid_operator(operator):
    operatorS = ('+', '-', '*', '/')
    return operator in operatorS
    


def ask_for_a_number(force_valid_input):
    while True:
        inp = input("Please provide a number! ")
        if is_number(inp):
            return float(inp)
        else:
            if not force_valid_input:
                return None
            print("This didn't look like a number, try again.")
    


def ask_for_an_operator(force_valid_input):
    while True:
        operator = input("Please provide an operator (one of +, -, *, /)! ")
        if is_valid_operator(operator):
            return operator
        else:
            if not force_valid_input:
                return None
            print("Unknown operator.")
    


def calc(operator, a, b):
    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return None
    result = None
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b != 0:
            result = a / b
        else:
            print("Error: Division by zero")
            return None
    return result


def simple_calculator():
    while True:
        a = ask_for_a_number(force_valid_input=False)
        if a is None:
            break
        op = ask_for_an_operator(force_valid_input=True)
        b = ask_for_a_number(force_valid_input=True)
        result = calc(op, a, b)
        if result is not None:
            print(f"The result is {result}")
    


if __name__ == '__main__':
    simple_calculator()
