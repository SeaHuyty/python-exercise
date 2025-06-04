# Exercise: print the following pattern.
#           1 
#           1 2 
#           1 2 3 
#           1 2 3 4 
#           1 2 3 4 5
row = 5
# 1 at the end is step.
for i in range(1, row + 1, 1):
    # Run inner loop i+1 time
    for j in range (1, i+1):
        print(j, end=' ')
    # Empty line after each row
    print("")