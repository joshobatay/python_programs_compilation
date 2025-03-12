# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# input
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

# process
difference = num1 // num2 # use // for floor division (no decimal points)

# output
print(f"The difference of {num1} and {num2} is {difference}")

