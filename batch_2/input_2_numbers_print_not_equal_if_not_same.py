# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# try-except for error handling
try: 

    # input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # process
    if num1 != num2:
        print("Not equal!") # output
    else:
        print('Equal!') # output

except ValueError:
    print("Invalid input")
