# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

# try-except for error handling
try:
    
    # ask user to input 2 numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # process numbers
    power = num1 ** num2

    # print result
    print(f"{num1} raised to the power of {num2} is {power}")
    
except ValueError:
    print("Please enter a valid number")