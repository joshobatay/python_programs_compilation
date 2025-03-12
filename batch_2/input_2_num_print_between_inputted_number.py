# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# input
num1 = int(input("Enter first number: "))
num2 = int(input('Enter second number: '))

# process
if num2 < num1:
    num1, num2 = num2, num1

# output
for i in range(num1 + 1, num2):
    print(i, end=" ") 
