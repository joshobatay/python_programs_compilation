# Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

# try-except for error handling
try: 
    # ask 2 numbers from user
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))

    # process sum
    sum = num1 + num2

    # print sum
    print(f'Sum of {num1} and {num2} is: {sum}')
except ValueError:
    print('Please enter valid numbers!')