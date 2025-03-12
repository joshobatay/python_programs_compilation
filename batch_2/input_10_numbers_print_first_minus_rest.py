# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# try-except for error handling
try:

    # initialize an empty list
    numbers = []

    # input
    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num) # adds the number to the list

    # process
    result = numbers[0] - sum(numbers[1:])

    # output
    print(f"The result of the first number minus all the remaining numbers is: {result}")

except ValueError:
    print("Invalid input!")