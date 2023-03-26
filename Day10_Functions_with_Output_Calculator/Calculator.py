logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
print()


def calculator(_first_number, _operation, _next_number):
    if _operation == "+":
        _result = float(_first_number + _next_number)
    elif _operation == "-":
        _result = float(_first_number - _next_number)
    elif _operation == "*":
        _result = float(_first_number * _next_number)
    elif _operation == "/":
        _result = float(_first_number / _next_number)
    else:
        print("Ops! Error!")
        _result = "Error!"

    return _result


continue_calculus = None
first_number = None
second_number = None
operation = None

while continue_calculus != "q":
    if continue_calculus is None or continue_calculus == "n":
        print("*" * 100)
        first_number = None
        continue_calculus = "continue"
        while first_number is None:
            try:
                first_number = float(input("What's the first number?:   "))
            except ValueError:
                print("Please, enter a valid number!")

    if continue_calculus == "y":
        first_number = result
        continue_calculus = None

    operation = None

    while operation != "+" and operation != "-" and operation != "*" and operation != "/":
        print("+\n-\n*\n/")
        operation = input("Pick an operation:   ")

    second_number = None

    while second_number is None:
        try:
            second_number = float(input("What's the second number?:   "))
        except ValueError:
            print("Please, enter a valid number!")

    result = calculator(first_number, operation, second_number)

    print(f"{first_number} {operation} {second_number} = {result}")

    while continue_calculus != "y" and continue_calculus != "n" and continue_calculus != "q":
        print()
        continue_calculus = input(f"Type 'y' to continue calculating with {result},\n"
                                  f"or type 'n' to start a new calculation,\n"
                                  f"or type 'q' to quit:   ").lower()
