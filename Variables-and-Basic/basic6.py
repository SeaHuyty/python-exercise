# Exercise: Prompts the user to input 3 decimal numbers, assigning them to variables 'a', 'b', and 'c' respectively.
#           Calculate their sum and average and then print the results.
print("We'll provide you the sum and average of 3 numbers you input")
a = input("a = ")
b = input("b = ")
c = input("c = ")
sum = int(a) + int(b) + int(c)
print(f"Sum of {a} + {b} + {c} = {sum}")
print(f"Average of {a}, {b}, {c} = {(sum) / 3}")