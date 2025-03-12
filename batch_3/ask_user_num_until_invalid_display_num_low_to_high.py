# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# initialize an empty list for the numbers to be stored
entered_numbers = []

# ask user for number infinite times
while True:
    try:
        num = int(input("Enter a number: "))
        entered_numbers.append(num) # stores the numbers to the list
        entered_numbers.sort() # sorts the numbers 
        print(f"Entered numbers (lowest to highest): {entered_numbers}") # outputs the numbers
        
    except ValueError:
        print("Invalid input, program will stop")
        break # stops the program from an infinite loop
    



