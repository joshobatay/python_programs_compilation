# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# initialize an empty list for the numbers to be stored
entered_number = []

# ask user for number infinite times
while True:
    try:
    
        num = int(input("Enter a number: "))
        entered_number.append(num)
        entered_number.sort(reverse = True) # reverses the sort order
        print(f"Entered numbers (highest to lowest): {entered_number}") # output numbers from highest to lowest
    
    except ValueError:
        print("Invalid input, enter a valid number!")
        break
