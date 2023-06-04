print("WELCOME TO CALCULATOR".center(95))
while True:

    while True:
        try:
            first_number = float(input("Enter First Number: "))
            break

        except ValueError:
            print("Enter an integer!")


    while True:
        operation = input("Choose an operator. e.g (+, -, /, *, **): ")

        if operation in ['+', '-', '*', '/', '**']:
            break

        else:
            print('Enter a Valid Operator!')


    while True:
        try:
            second_number = float(input("Enter Second Number: "))
            break
        except ValueError:
            print("Enter an integer!")



    if operation == '+':
        print(f"Sum of the values is: {first_number + second_number}")

    elif operation == '-':
        print(f"Difference of the values is: {first_number - second_number}")

    elif operation == '/':
        if second_number != 0:
            print(f"Quotient of the values is: {first_number / second_number}")
        else:
            print("Cannot divide by 0!")

    elif operation == '*':
        print(f"Product of the values is: {first_number * second_number}")

    elif operation == '**':
        print(f"Product of the values is: {first_number ** second_number}")
    else:
        print("Invalid Operator")

    ask = input("Do you want to continue? y/n: ")

    if ask.upper() == 'N':
        break
print("Thanks for using calculator!".center(95))
