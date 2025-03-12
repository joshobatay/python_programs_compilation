# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# Initialize an empty list to store numbers
entered_numbers = []

while True:
    try:
        num = int(input("Enter a number: "))  # Ask for a number
        entered_numbers.append(num)  # Stores the number
        print(f"Lowest number so far: {min(entered_numbers)}")  # Show the lowest number
        
    except ValueError:
        print("Program stopped, please input valid number")
        break # stops the program if invalid input
    


