print("Welcome to Simple Calculator, please enter two numbers")

while True:
    print("Enter your choice of operation: ")
    print("add , subtract , multiply , divide, exit")
    operation = input("provide the operation: ")
    if operation == "exit":
        break
    else:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 1st number: "))

        if operation == "add":
            print(f"Addition of both numbers is: {num1 + num2}")
        elif operation == "subtract":
            print(f"Subtraction of both numbers is: {num1 - num2}")
        elif operation == "multiply":
            print(f"Multiplication of both numbers is: {num1 * num2}")
        else:
            print(f"Division of both numbers is: {num1 / num2}")
