import math

# This function adds two numbers
def add(a,b):
    return(a + b)

# This function subtracts two numbers
def sub(a,b):
    return(a - b)

# This function multiplies two numbers
def mul(a,b):
    return(a * b)

# This function divides two numbers
def div(a,b):
    return(a / b)

while True:
    print("select operation ")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")

# Get the input
    choice = input("Enter choice(1 or 2 or 3 or 4):")

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2,"=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        else:
            print("Invalid input")
    except ValueError:
        print("please provide integers")
    except ZeroDivisionError:
        print("NUM2 must not be zero")