# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# try-except for error handling
try: 
    # initialize an empty list for storing entered number
    entered_numbers = []

    # ask user 10 numbers
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        entered_numbers.append(num)

    # initialize an empty list for counting non-duplicate numbers
    unique_numbers = []

    # process
    for num in entered_numbers:
        if entered_numbers.count(num) == 1:
            unique_numbers.append(num)

    # print numbers that dont have duplicate
    print(f"The numbers that do not have duplicates are: {unique_numbers}")

except ValueError:
    print("Invalid input!")