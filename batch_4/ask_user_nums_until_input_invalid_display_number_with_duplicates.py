# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate

# initialize an empty list for storing entered number
entered_numbers = []

# ask user infinite times
while True:

        num = int(input('Enter number: '))
        entered_numbers.append(num)
    
        # process, finds the number with the most duplicates
        unique_numbers = set(entered_numbers) # a set that find unique numbers
        most_frequent = max(unique_numbers, key=entered_numbers.count) # finds the most common number
        count = entered_numbers.count(most_frequent) # counts the number of times a number appears
        
        # outputs the number with most duplicates
        print(f"number {most_frequent}, appeared {count} times")
        
    
  




