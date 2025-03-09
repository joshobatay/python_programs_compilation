# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# process
i = 0
while i <= 100:
    # check if i is not divisible by 10 and 5, if yes, print i
    if i % 10 != 0 and i % 5 != 0:
        # output
        print(i) 
    # after i prints, i will increment by 1
    i += 1

