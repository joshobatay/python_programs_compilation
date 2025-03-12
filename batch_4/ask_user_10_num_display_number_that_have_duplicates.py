# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# initialize an empty list for storing entered number
entered_numbers = []

# ask user 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    entered_numbers.append(num)

# initialize an empty list for counting duplicate numbers
duplicate_numbers = []

# process
for num in entered_numbers:
    if entered_numbers.count(num) > 1 and num not in duplicate_numbers:
        duplicate_numbers.append(num)

# display numbers that have duplicate
print(f"The numbers that have duplicates are {duplicate_numbers}")

