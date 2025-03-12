# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate

# initialize an empty list for storing empty numbers
entered_numbers = []

# ask user infinite times until input is invalid
while True:
    # try-except for error handling
    try: 
        num = int(input("Enter a number: "))
        
        # process
        if num in entered_numbers:
            print("Duplicate!") # output
        else:
            print("Unique!")
            entered_numbers.append(num) # output
            
    except ValueError:
        print("Invalid input, please enter a number!")
        break # the loop will stop if user input is invalid
        
    



