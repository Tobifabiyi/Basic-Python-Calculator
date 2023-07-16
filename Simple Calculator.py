print('What is your name?')
name = input()
print('Hi ' + name + ', welcome to Simmath')


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
        print('Error: Division by zero')


def calculator():
    print('Welcome to Simmath')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Factorial')
    print('6. Greatest Common Divisor (GCD)')
    print('7. Quit')

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        result = addition(num1, num2)
        print("Result: ", result)
    elif choice == '2':
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        result = subtraction(num1, num2)
        print('Result: ', result)
    elif choice == '3':
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        result = multiplication(num1, num2)
        print('Result: ', result)
    elif choice == '4':
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        result = division(num1, num2)
        if result is not None:
            print('Result: ', result)
    elif choice == '5':
        num = int(input('Enter a number: '))
        result = factorial(num)
        print('Factorial: ', result)
    elif choice == '6':
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        result = gcd(num1, num2)
        print('GCD: ', result)
    elif choice == '7':
        print('Thank you. Goodbye!')
    else:
        print('Invalid response')
calculator()
