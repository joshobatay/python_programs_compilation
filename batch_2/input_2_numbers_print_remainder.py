# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

# try-except for error handling
try:
    
    # input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # process
    remainder = num1 % num2 

    # output
    print(f"The remainder of {num1} and {num2} is {remainder}")

except ValueError:
    print("Invalid input!")