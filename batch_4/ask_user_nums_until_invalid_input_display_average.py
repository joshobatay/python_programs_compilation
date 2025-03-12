# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

import statistics # built in module of python for getting average

# initialize an empty set for storing entered numbers
entered_number = []

# ask user infinite times
while True:
    
    # process
    num = int(input("Enter a number: "))
    entered_number.append(num)
    average = statistics.mean(entered_number) # calculates the average

# display average
