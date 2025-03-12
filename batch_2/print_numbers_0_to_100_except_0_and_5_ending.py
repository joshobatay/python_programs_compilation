# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# process
for i in range(100): # loops from 0 to 100
    if i % 2 != 0 and i % 5 != 0:
        print(i, end=" ") # outputs the numbers
