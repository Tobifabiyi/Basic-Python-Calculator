def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero")


def calculator():
    print("Welcome to the Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = addition(num1, num2)
        print("Result: ", result)
    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = subtraction(num1, num2)
        print("Result: ", result)
    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = multiplication(num1, num2)
        print("Result: ", result)
    elif choice == '4':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = division(num1, num2)
        if result is not None:
            print("Result: ", result)
    elif choice == '5':
        print("Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")

    calculator()

    
calculator()
