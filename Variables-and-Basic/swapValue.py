# Exercise:  Ask the user to input two values to store in 2 variables a and b, perform the swapping, and then print 
#            the new values of the variables. Example: if a=5 and b=10, after swap operation the value of a=10 and b=5
print("Please enter 2 integer and we'll swap the number")
a = input("a = ")
b = input("b = ")
c = a
a = b
b = c
print(f"After the swap operation, we have a = {a} and b = {b}")