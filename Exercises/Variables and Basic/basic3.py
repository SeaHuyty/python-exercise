# Exercise: Give user to input two float numbers and output the value from summing those numbers.
x = input("First: ")
y = input("Second: ")
print("Sum:", float(x) + float(y))
# Or we can write in another way.
x = float(input("First: ")) # We can use float function with integer numbers but not integer function with float numbers.
y = float(input("Second: "))
print("Sum:", x + y)
# Or in another way.
x = input("First: ")
y = input("Second: ")
z = float(x) + float(y) 
print("Sum:", str(z)) # (z) is a string because (z) is the combination of (x) and (y).