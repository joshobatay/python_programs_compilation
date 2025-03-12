# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# initialize an empty set for storing entered numbers
entered_numbers = []

# ask user infinite times
while True:
    try:
        
        # process
        num = int(input("Enter a number: "))
        entered_numbers.append(num)
        print(f"The highest number so far: {max(entered_numbers)}") # displays the highest number

    except ValueError:
        print("Invalid input, enter a valid number!")
        break

