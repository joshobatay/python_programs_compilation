# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# initialize an empty list for storing entered number
entered_numbers = []

# ask user 10 numbers
for i in range(10):
    num = int(input(f"Enter a number {i + 1}: "))
    entered_numbers.append(num)

# Initialize an empty list to store numbers while keeping only first entry of a duplicate
display_numbers = []

# process
for num in entered_numbers:
    if num not in display_numbers:
        display_numbers.append(num)

# outputs numbers, and duplicates for once only