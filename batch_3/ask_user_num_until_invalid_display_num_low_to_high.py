# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# initialize an empty list for the numbers to be stored
entered_numbers = []

# ask user for number infinite times
while True:
    # process
    
        num = int(input("Enter a number: "))
        entered_numbers.append(num)
        entered_numbers.sort() # sorts the numbers 
        print(f"Entered numbers (lowest to highest): {entered_numbers}") # outputs the numbers



