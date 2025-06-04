# Exercise: Write a program that asks the user for a number. Check and print "Positive" if it's greater 
#           than 0, "Negative" if less than 0, and "Zero" if it's exactly 0.
print("This code will determine whether the number you input is a positive number or a negative.")
deter = float(input("Please enter a number: "))
if deter == 0:
    print("It's a zero")
elif deter > 0:
    print(f"{deter} a positive number")
else:
    print(f"{deter} a negative number")