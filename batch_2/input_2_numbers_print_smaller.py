# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

# try-except for error handling
try:

    # input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # process
    if num1 < num2:
        print(f"{num1} is smaller than {num2}") # output
        
    elif num2 < num1:
        print(f"{num2} is smaller than {num1}") # output
    else:
        
        print("Both numbers are equal") # output

except ValueError:
    print('Invalid input!')