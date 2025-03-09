# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# try-except for error handling
try:
    
    # 1. get 2 numbers from user
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))

    # 2. print bigger number
    if num1 > num2:
        print(f'Bigger number is: {num1}')
    elif num2 > num1:
        print(f'Bigger number is: {num2}')
    else:
        print('Both numbers are equal!')

except ValueError:
    print('Please enter valid numbers!')