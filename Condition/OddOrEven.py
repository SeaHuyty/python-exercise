# Exercise: Get input an integer number then check if the number is odd or even.
print("We are going to determine if the number you input is an odd or an even number. Note: Input integer")
user = input("Enter the number: ")
if (int(user) % 2 == 0):
    print(f"{user} is an even number!!") # Since zero divided by 2 equals zero with no remainder, zero is classified as an even number.
else:
    print(f"{user} is an odd number!!")