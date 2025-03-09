# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

# ask user to input 2 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# process quotient
if num2 == 0:
    print("Cannot divide by zero")
else:
    quotient = num1 / num2
    # print result
    print(f"The quotient of {num1} and {num2} is {quotient}")


    