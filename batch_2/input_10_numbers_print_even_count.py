# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# initialize a value
even_count = 0

# input
for i in range(10): # ask user 10 times
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0: # checks if number is divisible by 2, if yes, even_count adds by 1
        even_count+=1
        
# output
print(f"There are {even_count} even numbers")